# 첫번째 방법
## Activation Visualization

## Weight Visualization

## Activation Maximization

## Maximally Activating Images

## Maximization by Optimization


# 두번째 방법 (Attribution)
## Saliency Map

## Class Activation Map
최종 prediction layer 직전에 위치한 layer의 각 feature map에 대하여 GAP(Global Average Pooling) 수행하도록 설계  


```Activation Visualization```이 feature map의 시각화 결과를 각각 시각화하는 방법  
```Class Activation Map```은 prediction layer 직전의 **weights를 사용**하여 해당 feature map들의 가중 합을 계산한 결과물만을 시각화함으로써, **특정 예측 클래스에 대한 전체 feature map들의 평균적인 활성화 결과를 확인하는 방법**  

- ```Saliency Map```이 입력 이미지 상에서 Attribution을 수행하여 다소 산개된 점 형태의 결과물을 도출한다면, ```Class Activation Map```은 컨볼루션 layer상에서 Attribution을 수행하기 때문에 상대적으로 부드러운 Attribution 결과를 보여준다는 특징이 있음



## Dataset Visualization 
```Attribution```이 단일 입력 이미지에 대한 컨볼루션 신경망의 에측 결과에 대한 설명을 제공  
```Dataset Visualization```은 데이터 상에 포함된 전체 이미지들에 대한 컨볼루션 신경망의 예측 결과의 일반적인 경향성에 대한 설명 제공

---

하나의 컨볼루션 layer을 관찰 대상으로 고정해 놓고, 데이터 상의 이미지들을 하나씩 이볅하여 이들 각각에 대한 feature map을 산출한 뒤, 여기에 ```Dimensionality Reduction```방법을 적용하여 2D 또는 3D feature space 상의 점으로 도시할 수 있음  

![image](https://user-images.githubusercontent.com/72767245/163310119-9e864250-8430-41e0-8a5e-c75cb2075d02.png)


- DataVisualization을 위한 ```Dimensionality Reduction``` 방법
  - PCA(principal component analysis)
  - t-SNE(t-distributed stochastic neighbor embedding)
  - UMAP(uniform mainfold approximation and projection




# Conclusion
```Activation Visualization```  
- 컨볼루션 신경망의 예측 결과에 대한 해석을 위한 가장 단순하고 직관적인 방법  
- **Feature map을 직접 이미지 형태로 시각화**
- (-) 늘 한 번에 많은 수의 Feature map들을 동시에 관찰하면서 각각이 커버하는 시각적 특징이 무엇인지 추정해야 한다는 단점
