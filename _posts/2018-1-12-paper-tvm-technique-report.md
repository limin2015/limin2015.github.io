---
layout:     post
title:      paper-TVM: End-to-End Optimization Stack for Deep Learning
keywords:   paper-TVM-technique-report
category:   [paper]
tags:       [paper]
---

总结一下tvm的paper。




# 解决的问题：



# 主要内容：


## 优化计算图：


### kernel融合

- elementwise-elementwise的融合:eg, add->sqrt


- elementwise-reduction融合： eg, exp->sum

- 一个operator的后面是一个elemwise操作，则可以把elementwise合并到前面的operator中: eg, conv->bn->relu



### Data Layout Transformation
