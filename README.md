# TIL 
Today I Learned


## DeepLearning   
### Pytorch version  

```python
# 1. Data Load
data_dir = 'data'
annotation_dir = f'{data_dir}/Annotation'

# 2. Dataset 
class Dataset(Dataset):
  def __init__(self, img_dir, datalist ,transform = None):
    self.transform = transform
    with open(datalist) as f:
      self.datalist = f.readlines()
   
   def __len__(self): 
     return len(self.datalist)
     
   def __getitem__(self, idx):
      item = self.datalist[idx].split(',')
      ..
      
      return {'image': img, 
              'img_type': img_type,
              'action': action,
              'frame_no': frame_no}
              
# 3. Model
class model_CNN(nn.Module):
  def __init__(self, num_cls = 45):
    super(model_CNN, self).__init__()
    self.conv1 = nn.Conv2D(3, 32, 5)
    ...
    
  def forward(self, x):
    x = self.relu(self.maxpool(self.conv1(x)))
    ...
    return x

# 4. Criterions
def cls_criterion(cls_pred, label):
  loss = nn.CrossEntropyLoss()
  return loss(cls_pred, label)
  
# 5. train 
def train(dataloader, checkpoint_path):
  model.train()
  train_loss_min = np.Inf
  
  for epoch in range(EPOCH):
    train_loss = 0.0
    accuracy = 0
    pbar = tqdm(enumerate(dataloader), total = len(dataloader))
    for batch_idx, data in pbar:
      optimizer.zero_grad()
      image = data['image'].cuda()
      ..
      loss = cls_criterion(cls_pred, type)
      loss = lambda_ + loss
      ..
      loss.backward()
      optimizer.step()
      scheduler.step()
    train_loss = train_loss/len(dataloader)
    train_acc = accuracy/len(dataloader)
    print(f'EPOCH:{epoch+1} train loss: {train_loss} train accuracy: {train_acc}')
    checkpoint = {
        'epoch' : epoch+1,
        'train_loss' : train_loss,
        'train_acc': train_acc,
        'state_dict': model.state_dict(),
        'optimizer':optimizer.state_dict()
    }
    if train_loss <= train_loss_min:
      train_loss_min = train_loss
      torch.save(checkpoint, checkpoint_path)

# 6. TEST
def test(dataloader, checkpoint_path):
  checkpoint = torch.load(checkpoint_path)
  model.load_state_dict(checkpoint['state_dict'])
  optimizer.load_state_dict(checkpoint['optimizer'])
  
  model.eval()
  val_loss = 0.0
  accuracy = 0.0
  
  with torch.no_grad():
    pbar = tqdm(enumerate(dataloader), total = len(dataloader))
    for batch_idx, data in pbar:
      image = data['type'].cuda()
      cls_pred = model(image)
      ..
   return val_loss, val_acc


 ################################################ TRAIN  ################################################

EPOCH = 100
RL = 0.001
BSZ = 128
lambda_ = 0.1

model = model_CNN(num_cls = 45)
model.cuda()
optimizer = torch.optim.SGD(model.parameters(), lr = RL)
sceduler = torch.optim.lr_scheduler.LambdaLR(optimizer=optimizer, lr_lambda = lambda epoch:0.95**epoch, last_epoch = -1)

train_ds = Dataset(image_dir, train_list_file, transform = transforms.ToTensor())
test_ds = Dataset(image_dir, test_list_file, transform = transforms.ToTensor())
dataloader = {'train': torch.utils.data.DataLoader(train_ds, batch_size = BSZ, shuffle = True),
              'test': torch.utils.data.DataLoader(test_ds, batch_size = BSZ, shuffle = False)}
train(dataloader['train'], checkpoint_path)
test(dataloader['test'], checkpoint_path)
```
### Keras version    
**Custom data generator**을 만들때는 ```keras.utils.Sequence```클래스를 상속   
Sequence는 __getitem__, __len__, on_epoch_end, __iter__를 sub method로 가짐   

```on_epoch_end```메소드는 각 epoch의 맨 처음과 맨 끝에 실행
[keras Datagenerator](http://www.kwangsiklee.com/2018/11/keras%EC%97%90%EC%84%9C-sequence%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%98%EC%97%AC-%EB%8C%80%EC%9A%A9%EB%9F%89-%EB%8D%B0%EC%9D%B4%ED%84%B0%EC%85%8B-%EC%B2%98%EB%A6%AC%ED%95%98%EA%B8%B0/)
```python
from tensorflow.keras.utils import Sequence
class DataLoader(Sequence):
  def __init__(self, datalist, batch_size, dim, n_channels):
    super(DataLoader, self).__init__()
    self.data_list = np.array_list(data_list, len(data_list)//batch_size)
    ...
    
  def on_epoch_end(self):
    self.indexes == np.arange(len(self.X))
    if self.shuffle:
      np.random.shuffle(self.indexes)
      
   def __len__(self):
     return len(self.data_list)
     
   def __getitem__(self, index):
      return self.data_list[index]
 
 if __name__ == "__main__":
    model = Model()
    data_list = getDataList()
    batch_size = 16
    
    data_loader = DataLoader(data_list, batch_size)
    model.fit(data_loader)
```
```python
from keras_dataloader.dataloader import DataGenerator
from keras_dataloader.dataset import Dataset


class TensorDataset(Dataset):

    def __getitem__(self, index):
        # time.sleep(np.random.randint(1, 3))
        return np.random.rand(3), np.array([index])

    def __len__(self):
        return 100
        
model = Sequential()
model.add(Dense(units=4, input_dim=3))
model.add(Dense(units=1))
model.compile('adam', loss='mse')

data_loader = DataGenerator(TensorDataset(), batch_size=20, num_workers=0)

model.fit_generator(generator=data_loader, epochs=1, verbose=1)
```
https://github.com/GlassyWing/keras_dataloader


## Computer Vision문제 
- Object Detection & Recognition
- Scene Understanding
- 3D reconstruction
- Tracking
- Image/Video Restoration
- Segmentation
