# declare some variables for use later
n = tvm.var('n')
m = tvm.var('m')

# declare a matrix element-wise multiply
A = tvm.placeholder((m, n), name='A')
B = tvm.placeholder((m, n), name='B')
C = tvm.compute((m, n), lambda i, j: A[i, j] * B[i, j], name='C')

s = tvm.create_schedule([C.op])
# lower will transform the computation from definition to the real
# callable function. With argument `simple_mode=True`, it will
# return you a readable C like statement, we use it here to print the
# schedule result.
print(tvm.lower(s, [A, B, C], simple_mode=True))


Out:
produce C {
  for (i, 0, m) {
    for (j, 0, n) {
      C[((i*n) + j)] = (A[((i*n) + j)]*B[((i*n) + j)])
    }
  }
}



A = tvm.placeholder((m,), name='A')
B = tvm.compute((m,), lambda i: A[i]*2, name='B')

s = tvm.create_schedule(B.op)
xo, xi = s[B].split(B.op.axis[0], factor=32)
print(tvm.lower(s, [A, B], simple_mode=True))


Out:
produce B {
  for (i.outer, 0, ((m + 31)/32)) {
    for (i.inner, 0, 32) {
      if (likely(((i.outer*32) < (m - i.inner)))) {
        B[((i.outer*32) + i.inner)] = (A[((i.outer*32) + i.inner)]*2.000000f)
      }
    }
  }
}


A = tvm.placeholder((m,), name='A')
B = tvm.compute((m,), lambda i: A[i], name='B')

s = tvm.create_schedule(B.op)
bx, tx = s[B].split(B.op.axis[0], nparts=32)
print(tvm.lower(s, [A, B], simple_mode=True))


Out:
produce B {
  for (i.outer, 0, 32) {
    for (i.inner, 0, ((m + 31)/32)) {
      if (likely(((i.outer*((m + 31)/32)) < (m - i.inner)))) {
        if (likely(((0 - i.inner) <= (i.outer*((m + 31)/32))))) {
          B[((i.outer*((m + 31)/32)) + i.inner)] = A[((i.outer*((m + 31)/32)) + i.inner)]
        }
      }
    }
  }
}


A = tvm.placeholder((m, n), name='A')
B = tvm.compute((m, n), lambda i, j: A[i, j], name='B')

s = tvm.create_schedule(B.op)
xo, yo, xi, yi = s[B].tile(B.op.axis[0], B.op.axis[1], x_factor=10, y_factor=5)
print(tvm.lower(s, [A, B], simple_mode=True))


Out:
produce B {
  for (i.outer, 0, ((m + 9)/10)) {
    for (j.outer, 0, ((n + 4)/5)) {
      for (i.inner, 0, 10) {
        for (j.inner, 0, 5) {
          if (likely(((i.outer*10) < (m - i.inner)))) {
            if (likely(((j.outer*5) < (n - j.inner)))) {
              B[(((j.outer*5) + (((i.outer*10) + i.inner)*n)) + j.inner)] 
                  = A[(((j.outer*5) + (((i.outer*10) + i.inner)*n)) + j.inner)]
            }
          }
        }
      }
    }
  }
}


A = tvm.placeholder((m, n), name='A')
B = tvm.compute((m, n), lambda i, j: A[i, j], name='B')

s = tvm.create_schedule(B.op)
# tile to four axises first: (i.outer, j.outer, i.inner, j.inner)
xo, yo, xi, yi = s[B].tile(B.op.axis[0], B.op.axis[1], x_factor=10, y_factor=5)
# then fuse (i.inner, j.inner) into one axis: (i.inner.j.inner.fused)
fused = s[B].fuse(xi, yi)
print(tvm.lower(s, [A, B], simple_mode=True))

Out:
produce B {
  for (i.outer, 0, ((m + 9)/10)) {
    for (j.outer, 0, ((n + 4)/5)) {
      for (i.inner.j.inner.fused, 0, 50) {
        if (likely(((i.outer*10) < (m - (i.inner.j.inner.fused/5))))) {
          if (likely(((j.outer*5) < (n - (i.inner.j.inner.fused % 5))))) {
            B[(((j.outer*5) + (i.inner.j.inner.fused % 5)) + (((i.outer*10) 
            + (i.inner.j.inner.fused/5))*n))] = A[(((j.outer*5) + (i.inner.j.inner.fused % 5)) 
            + (((i.outer*10) + (i.inner.j.inner.fused/5))*n))]
          }
        }
      }
    }
  }
}


A = tvm.placeholder((m, n), name='A')
B = tvm.compute((m, n), lambda i, j: A[i, j], name='B')

s = tvm.create_schedule(B.op)
# tile to four axises first: (i.outer, j.outer, i.inner, j.inner)
xo, yo, xi, yi = s[B].tile(B.op.axis[0], B.op.axis[1], x_factor=10, y_factor=5)
# then reorder the axises: (i.inner, j.outer, i.outer, j.inner)
s[B].reorder(xi, yo, xo, yi)
print(tvm.lower(s, [A, B], simple_mode=True))


Out:
produce B {
  for (i.inner, 0, 10) {
    for (j.outer, 0, ((n + 4)/5)) {
      for (i.outer, 0, ((m + 9)/10)) {
        for (j.inner, 0, 5) {
          if (likely((i.inner < (m - (i.outer*10))))) {
            if (likely(((j.outer*5) < (n - j.inner)))) {
              B[(((j.outer*5) + ((i.inner + (i.outer*10))*n)) + j.inner)] 
              = A[(((j.outer*5) + ((i.inner + (i.outer*10))*n)) + j.inner)]
            }
          }
        }
      }
    }
  }
}


A = tvm.placeholder((n,), name='A')
B = tvm.compute(A.shape, lambda i: A[i] * 2, name='B')

s = tvm.create_schedule(B.op)
bx, tx = s[B].split(B.op.axis[0], factor=64)
s[B].bind(bx, tvm.thread_axis("blockIdx.x"))
s[B].bind(tx, tvm.thread_axis("threadIdx.x"))
print(tvm.lower(s, [A, B], simple_mode=True))

Out:
produce B {
  // attr [iter_var(blockIdx.x, , blockIdx.x)] thread_extent = ((n + 63)/64)
  // attr [iter_var(threadIdx.x, , threadIdx.x)] thread_extent = 64
  if (likely(((blockIdx.x*64) < (n - threadIdx.x)))) {
    B[((blockIdx.x*64) + threadIdx.x)] 
    = (A[((blockIdx.x*64) + threadIdx.x)]*2.000000f)
  }
}


A = tvm.placeholder((m,), name='A')
B = tvm.compute((m,), lambda i: A[i]+1, name='B')
C = tvm.compute((m,), lambda i: B[i]*2, name='C')

s = tvm.create_schedule(C.op)
print(tvm.lower(s, [A, B, C], simple_mode=True))

Out:
produce B {
  for (i, 0, m) {
    B[i] = (A[i] + 1.000000f)
  }
}
produce C {
  for (i, 0, m) {
    C[i] = (B[i]*2.000000f)
  }
}


A = tvm.placeholder((m,), name='A')
B = tvm.compute((m,), lambda i: A[i]+1, name='B')
C = tvm.compute((m,), lambda i: B[i]*2, name='C')

s = tvm.create_schedule(C.op)
s[B].compute_at(s[C], C.op.axis[0])
print(tvm.lower(s, [A, B, C], simple_mode=True))

Out:
produce C {
  for (i, 0, m) {
    produce B {
      B[i] = (A[i] + 1.000000f)
    }
    C[i] = (B[i]*2.000000f)
  }
}

A = tvm.placeholder((m,), name='A')
B = tvm.compute((m,), lambda i: A[i]+1, name='B')
C = tvm.compute((m,), lambda i: B[i]*2, name='C')

s = tvm.create_schedule(C.op)
s[B].compute_inline()
print(tvm.lower(s, [A, B, C], simple_mode=True))

Out:
produce C {
  for (i, 0, m) {
    C[i] = ((A[i]*2.000000f) + 2.000000f)
  }
}

A = tvm.placeholder((m,), name='A')
B = tvm.compute((m,), lambda i: A[i]+1, name='B')
C = tvm.compute((m,), lambda i: B[i]*2, name='C')

s = tvm.create_schedule(C.op)
s[B].compute_at(s[C], C.op.axis[0])
s[B].compute_root()
print(tvm.lower(s, [A, B, C], simple_mode=True))

Out:
produce B {
  for (i, 0, m) {
    B[i] = (A[i] + 1.000000f)
  }
}
produce C {
  for (i, 0, m) {
    C[i] = (B[i]*2.000000f)
  }
}


import numpy as np
import tvm

# The sizes of inputs and filters
batch = 256
in_channel = 256
out_channel = 512
in_size = 14
kernel = 3
pad = 1
stride = 1

# Algorithm
A = tvm.placeholder((in_size, in_size, in_channel, batch), name='A')
W = tvm.placeholder((kernel, kernel, in_channel, out_channel), name='W')
out_size = (in_size - kernel + 2*pad) // stride + 1
# Pad input
Apad = tvm.compute(
    (in_size + 2*pad, in_size + 2*pad, in_channel, batch),
    lambda yy, xx, cc, nn: tvm.select(
        tvm.all(yy >= pad, yy - pad < in_size,
                xx >= pad, xx - pad < in_size),
        A[yy - pad, xx - pad, cc, nn], tvm.const(0.)),
    name='Apad')
# Create reduction variables
rc = tvm.reduce_axis((0, in_channel), name='rc')
ry = tvm.reduce_axis((0, kernel), name='ry')
rx = tvm.reduce_axis((0, kernel), name='rx')
# Compute the convolution
B = tvm.compute(
    (out_size, out_size, out_channel, batch),
    lambda yy, xx, ff, nn: tvm.sum(
        Apad[yy * stride + ry, xx * stride + rx, rc, nn] * W[ry, rx, rc, ff],
        axis=[ry, rx, rc]),
    name='B')





// attr [Apad] storage_scope = "global"
allocate Apad[float32 * 16 * 16 * 256 * 256]
produce Apad {
  for (yy, 0, 16) {
    for (xx, 0, 16) {
      for (cc, 0, 256) {
        for (nn, 0, 256) {
          Apad[((((((yy*16) + xx)*256) + cc)*256) + nn)] 
          = tvm_if_then_else(((((1 <= yy) && (yy < 15)) && (1 <= xx)) 
          && (xx < 15)), A[(((((((yy*14) + xx)*256) + cc)*256) + nn) + -983040)], 0.000000f)
        }
      }
    }
  }
}
produce B {
  for (yy, 0, 14) {
    for (xx, 0, 14) {
      for (ff, 0, 512) {
        for (nn, 0, 256) {
          B[((((((yy*14) + xx)*512) + ff)*256) + nn)] = 0.000000f
          for (ry, 0, 3) {
            for (rx, 0, 3) {
              for (rc, 0, 256) {
                B[((((((yy*14) + xx)*512) + ff)*256) + nn)] 
                = (B[((((((yy*14) + xx)*512) + ff)*256) + nn)] + (Apad[(((((((yy*16) + xx)*65536) + nn) 
                + (ry*1048576)) + (rx*65536)) + (rc*256))]*W[(((ff + (ry*393216)) + (rx*131072)) + (rc*512))]))
              }
            }
          }
        }
      }
    }
  }
}



from __future__ import absolute_import, print_function
import tvm
import numpy as np

n = tvm.var("n")
A = tvm.placeholder((n,), name='A')
B = tvm.placeholder((n,), name='B')
C = tvm.compute(A.shape, lambda i: A[i] + B[i], name="C")
s = tvm.create_schedule(C.op)
bx, tx = s[C].split(C.op.axis[0], factor=64)
s[C].bind(bx, tvm.thread_axis("blockIdx.x"))
s[C].bind(tx, tvm.thread_axis("threadIdx.x"))

target = "rocm"
fadd_rocm = tvm.build(s, [A, B, C], target, target_host="llvm", name="myadd")
ctx = tvm.rocm(0)

n = 1024
a = tvm.nd.array(np.random.uniform(size=n).astype(A.dtype), ctx)
b = tvm.nd.array(np.random.uniform(size=n).astype(B.dtype), ctx)
c = tvm.nd.array(np.zeros(n, dtype=C.dtype), ctx)

fadd_rocm(a, b, c)
np.testing.assert_allclose(c.asnumpy(), a.asnumpy() + b.asnumpy())


view LLVM IR that TVM generates in the following way:

dev_module = fadd_rocm.imported_modules[0]
print(dev_module.get_source("llvm"))


view GPU assembly that ROCm backend generates：

print(dev_module.get_source("asm"))


void BatchedGemm(input A, input B, output C, M, N, K, batch_dimension) {
  for (int i = 0; i < batch_dimension; ++i)  {
    DoGemm(A[i],B[i],C[i],M,K,N)
  }
}


# computation representation
A = tvm.placeholder((batch, M, K), name='A')
B = tvm.placeholder((batch, K, N), name='B')
k = tvm.reduce_axis((0, K), 'k')
C = tvm.compute((batch, M, N),
         lambda b, y, x: tvm.sum(A[b, y, k] * B[b, k, x], axis = k),
         name = 'C')



# thread indices
block_y = tvm.thread_axis("blockIdx.y")
block_x = tvm.thread_axis("blockIdx.x")
thread_y = tvm.thread_axis((0, num_thread_y), "threadIdx.y")
thread_x = tvm.thread_axis((0, num_thread_x), "threadIdx.x")
thread_yz = tvm.thread_axis((0, vthread_y), "vthread", name="vy")
thread_xz = tvm.thread_axis((0, vthread_x), "vthread", name="vx")

# block partitioning
BB, FF, MM, PP = s[C].op.axis
BBFF = s[C].fuse(BB, FF)
MMPP = s[C].fuse(MM, PP)
by, ty_block = s[C].split(BBFF, factor = num_thread_y * vthread_y)
bx, tx_block = s[C].split(MMPP, factor = num_thread_x * vthread_x)
s[C].bind(by, block_y)
s[C].bind(bx, block_x)
vty, ty = s[C].split(ty_block, nparts = vthread_y)
vtx, tx = s[C].split(tx_block, nparts = vthread_x)
s[C].reorder(by, bx, vty, vtx, ty, tx)
s[C].reorder(by, bx, ty, tx)
s[C].bind(ty, thread_y)
s[C].bind(tx, thread_x)
s[C].bind(vty, thread_yz)
s[C].bind(vtx, thread_xz)        


Batch matmul and broadcast add fusion computation

# computation representation
A = tvm.placeholder((batch_size, features, M, K), name='A')
# the shape of B is (N, K) other than (K, N) is because B is transposed is this fusion pattern
B = tvm.placeholder((batch_size, features, N, K), name='B')
ENTER = tvm.placeholder((batch_size, 1, M, N), name = 'ENTER')
k = tvm.reduce_axis((0, K), 'k')
C = tvm.compute(
           (batch_size, features, M, N),
           lambda yb, yf, m, x: tvm.sum(A[yb, yf, m, k] * B[yb, yf, x, k], axis = k),
           name = 'C')
D = topi.broadcast_add(C, ENTER)


Batch matmul and transpose fusion computation can be declared as:

# computation representation
A = tvm.placeholder((batch_size, features, M, K), name='A')
B = tvm.placeholder((batch_size, features, K, N), name='B')
k = tvm.reduce_axis((0, K), 'k')
C = tvm.compute(
           (batch_size, M, features, N),
           lambda yb, m, yf, x: tvm.sum(A[yb, yf, m, k] * B[yb, yf, k, x], axis = k),
           name = 'C')