# 머신러닝
- ```Colab```이용
  - Colab은 Linux의 ```Ubuntu``` 기반임
  - ```!python --version``` => ```python 3.6.9```
  - ```!pip list``` 하면 colab 내에 설치되어있는 파일들 확인 가능
    - deeplearning library: tensorflow[Google] & torch[Pytorch]
    - Keras backend로 tensorflow 사용(theano 예전에 많이 쓰임)

  - ```fbprophet```: facebook에서 만든것으로 시계열 데이터를 다루는데 사용되는 패키지
  - ```kaggle```: 데이터셋 사용할때의 kaggle API
  - ```keras```: 딥러닝 라이브러리 (Tensorflow 내)
  - ```lightgbm```: 마이크로소프트에서 제공. ```xgboost```그라디언트 부스팅 패키지(머신러닝 패키지) 의 light 버전
  - ```numpy```: 숫자를 계산하기 위한 라이브러리
    - numpy는 리스트가 아닌 배열로 각 원소별로 계산 가능
  - ```opencv```: open computer library  (동영상, 이미지 처리)
  - ```pandas```: R 언어의 DataFrame - 통계적인 계산에 유용
     - ```df = pd.DataFrame(data = {id: col_id, 'Team': col_team})```
     - ```df.set_index('Id', inplace = True)```
     - groupby라는 함수를 사용
     - ```df.groupby('Team').mean()```
  - ```matplotlib```: 그림
    - ```fig = plt.figure()```
    - ```ax = fig.gca()```
    - ```ax.plot(x, y, 'r-')```
    - ```fig.show()```
  - ```scikit-learn```: 머신러닝 알고리즘
  - ```seaborn```: 그림그리는 애 - 분석하는 것
    - ```import seaborn as sns```
    - ```sns.histplot(x = 'Score', data = df)```
    - ```sns.boxplot(y = 'Score', x = 'team', data = df)```
  - ```tensorflow```: 딥러닝
  - ```theano```: 딥러닝 (요즘은 Tensorflow 씀)
  - ```torch```: 딥러닝
  - ```xgboost```: 머신러닝 패키지
  - ```yellowbrick```: 
### Kaggle
- 본인의 고유 Kaggle Key 다운로드
- 다운로드할 데이터의 ```Copy API command```

```python
import os
os.environ['KAGGLE_USERNAME'] = 'fastcampus'
os.environ['KAGGLE_KEY'] = 'c939a37~'

!kaggle datasets download ~ // API command의 명령어

```
## EDA 및 분류문제 (+SQL)
## EDA 및 회귀문제 (+ Prophet)
## 의사결정나무, Random Forest, Support Vector Machine
## Boosting, Clustering, Principal Component
## 비선형 패턴, Kernel PCA
## Clustering: K-means, RMF 분석, DBSCAN 알고리즘
## CF-based MF-based, Point-wise

https://drive.google.com/drive/u/0/folders/1gzQKyxgpNmMSxT6-_q7Wa2LEAwzCoI5o
