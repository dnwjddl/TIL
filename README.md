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

                            ##################################
                            ############## TRAIN #############
                            ##################################
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
  
