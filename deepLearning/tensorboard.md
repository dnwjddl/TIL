## Pytorch로 Tensorboard 사용하기

```python
import torch
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter()
```

writer는 기본적으로 ```./runs/``` 디렉토리에 출력

## Scalar 기록하기
- 스칼라는 각 학습단계(step)에서의 손실 값이나 각 에폭 이후의 정확도를 저장하는데 도움을 줌
- 스칼라의 값을 기록하려면 ```add_scalar(tag, scalar_value, global_step = None, walltime = None)```을 사용해야함

```python
x = torch.arange(-5, 5, 0.1).view(-1, 1)
y = -5 * x + 0.1 * torch.randn(x.size())

model = torch.nn.Linear(1, 1)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.1)

def train_model(iter):
    for epoch in range(iter):
        y1 = model(x)
        loss = criterion(y1, y)
        writer.add_scalar("Loss/train", loss, epoch)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

train_model(10)
writer.flush()
```

모든 보류중인 pending 이벤트가 디스크에 기록되었는지 확인하려면 ```flush()```메소드를 호출해야 함  
Summary writer가 더이상 필요하지 않으면 ```close()```메소드를 호출

```python
writer.close()
```

### Tensorboard 실행하기
```
$ pip install tensorboard
```

- 위에서 사용한 루트 로그 디렉토리를 지정하여 Tensorboard 시작
- logdir 인자는 Tensorboard가 출력할 수 있는 이벤트 파일들을 찾을 디렉토리를 가리킴

```
$ tensorboard --logdir=runs
```

제공하는 URL로 이동하거나 https://localhost:6006/으로 이동
