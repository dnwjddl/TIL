# TIL  
Today I Learned     

## DeepLearning
### Pytorch version

```python
# 1. Data Load
data_dir = 'data'
annotation_dir = f'{data_dir}/Annotation'

# 2. Data Loader
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
              
    

```
  
