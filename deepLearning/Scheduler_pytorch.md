# Learning Rate Scheduler

```python
import torch
import torch.nn as nn
import torch.optim as optim

class Model(nn.Module):
  def __init__(self):
    super(Model, self).__init__()
    ...
  def forward(self, x):
    return self.activation(self.linear(x))
    
    
# Dataset
train = Dataset(img_dir, transform = transforms.ToTensor())
# DataLoader
dataloader = {'train': torch.utils.data.DataLoader(train, batch_size = 32, shuffle = True)
# Model
model = Model()
# Loss
loss = nn.MSELoss()
# optimizer
optimizer = optim.Adam(model.paramteters(), lr = 1e-3)
#scheduler
scheduler = optim.lr_scheduler.LambdaLR(optimizer = optimizer, lr_lambda = lambda epoch = 0.95 ** epoch, last_epoch = -1, verbose = False)

...

epochs = 100
for epoch in range(epochs):
  for i, (data) in enumerate(data_loader):
    x_data, y_data = data
    opeimizer.zero_grad()
    
    estimated_y = model(x_data)
    loss = loss(y_data, estimated_y)
    loss.backward()
    
    optimizer.step()
    scheduler.step()

```

## LabdalLR
- Lambda 표현식으로 작성한 함수를 통해 learning rate 조절
- 초기 learning rate에 lambda 함수에서 나온 값을 곱해져서 learning rate 계산

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
scheduler = optim.lr_scheduler.LambdaLR(optimizer=optimizer,
                                lr_lambda=lambda epoch: 0.95 ** epoch)
```
## MultiplicativelLR
- Lambda 표현식으로 작성한 함수를 통해 learning rate를 조절
- 초기 learning rate에 lambda 함수에서 나온 값을 누적 곱해서 learning rate를 조절
```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
scheduler = optim.lr_scheduler.MultiplicativeLR(optimizer=optimizer,
                                lr_lambda=lambda epoch: 0.95 ** epoch)
```

## StepLR
- Step size마다 gamma 비율로 lr 감소
```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.5)
```
## MultiStepLR
- step size가 아니라 learning rate를 감소시킬 epoch를 지정
```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
scheduler = optim.lr_scheduler.MultiStepLR(optimizer, milestones=[30,80], gamma=0.5)
```

## ExponentialLR
- learning rate decay가 exponential 함수를 따름
```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
scheduler = optim.lr_scheduler.ExponentialLR(optimizer, gamma=0.5)
```
## ConsineAnnealingLR
- learning rate가 cos 함수를 따라서 eat_min까지 떨어짐
- 다시 초기 learning rate까지올라옴
```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50, eta_min=0)
```

## ReduceLROnPlateau
- 성능이 향상이 없을 때 learning rate를 감소
- validation loss나 metrics을 learing rate step 함수의 input을 넣어주어야함
- 그 이후에는 learning rate를 줄인다.

```python
optimizer = torch.optim.SGD(model.parameters(), lr=0.1, momentum=0.9)
scheduler = ReduceLROnPlateau(optimizer, 'min')
for epoch in range(100):
     train(...)
     val_loss = validate(...)
     # Note that step should be called after validate()
     scheduler.step(val_loss)
```

## CyclicLR
- 성능이 향상이 없을 때 learning rate를 감소시킴
- validation loss나 metrics 을 learning rate step함수의 input으로 넣어주어야 함
- 그래서 metirc이 향상되지 않을 때, patience 횟수 만큼 참고 그 이후에는 learing rate를 줄인다.
- optimizer에 momentum을 설정해야 사용 가능
- 
```pythnon
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
scheduler = torch.optim.lr_scheduler.CyclicLR(optimizer, base_lr=0.00005, 
                                              step_size_up=5, max_lr=0.0001, 
                                              gamma=0.5, mode='exp_range')
```

## OneCycleLR
- 초기 learning rate에서 1Cycle Annealing하는 scheduler

## ConvisneAnnealingWarmRestarts
- Consine annealing함수를 따르면서 Tiepoch마다 다시 시작

```python

optimizer = torch.optim.SGD(model.parameters(), lr=0.0001)
scheduler = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(optimizer, T_0=10, 
                                                                T_mult=1, eta_min=0.00001)
```
