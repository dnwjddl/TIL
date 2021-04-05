# LossFunction(Cross Entropy, MSE)

## Cross Entropy Loss : Classification
- Linear model을 통해서 최종값(Logit or score)
- Softmax 함수를 통해 값의 범위는 [0, 1], 총 합이 1이 되도록
- ```Cross-entropy Loss```을 통해서 구함
- BCELoss 에서는 CrossEntropyLoss와 같이 softmax를 포함한 것이 아닌, Cross Entropy만 구함
  - Categorical Cross-Entropy: Multi-class Classification [Softmax 후 사용하는 Loss]
  - Binary Cross-Entropy: Binary-label classification [sigmoid 후 사용하는 loss function]

```python
torch.nn.CrossEntropyLoss(weight = None, size_average = None,ignore_index = -100, reduce = None, reduction = 'mean)

import torch.nn as nn
criterion = nn.CrossEntropyLoss()
loss = criterion(input, target)

## Binary Case(class가 두개인 경우)
torch.nn.BCELoss(weight = None, size_average = None, reduce = None, reduction= 'mean')
```

## Mean Squared Error: Classification, Denoising(image restoration task의 이미지 간의 차이), segmentation(mask간의 차이)
- 두 점 사이의 거리

```python
torch.nn.MSELoss(size_average = None, reduce = None, reduction = 'mean')

import torch.nn as nn
criterion = nn.MSELoss()

loss = criterion(input, target)
```
