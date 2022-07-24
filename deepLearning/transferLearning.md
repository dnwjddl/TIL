## Transfer Learning
pretrained 된 모델을 사용할려면 ```torchvision```과 ```timm```에서 여러 SOTA model를 공유해주게 된다.

```python
# torchvision example
import torchvision 
model = torchvision.models.resnet18(pretrained = True)
data = torch.Tensor(1,3,224,224)
output= model(output)
print(output.shape) # ([1, 10000]) -> ImageNet Dataset Classes가 10000
```

```timm```을 이용하면 비교적 최신 모델을 사용할 수도 있음  
```python
import timm
model = timm.create_model('resnet18', pretrained = True, num_classes = 10)
print(model)
```



