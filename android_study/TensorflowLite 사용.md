## Model 생성
example

```python
import tensorflow as tf

# 데이터 로드
mnist = tf.keras.datasets.mnist

# 데이터 정규화
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test/255.0

# 모델
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation = tf.nn.relu),
  ..
])

# 모델 컴파일
model.compile(optimizer = 'adam',
              loss = 'sparse_categorical_crossentropy',
              metrics = ['accuracy'])

# 모델 학습
model.fit(x_train, y_train, epochs = 5)

# 모델 평가
model.evaluate(x_test, y_test)
```
```python
# 모델 converter
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# 모델 저장
open('mnist.tflite', 'wb').write(tflite_model)
```


## 안드로이드 스튜디오에서 사용
```assets``` 파일 내에 ```mnist_tflite``` 파일 옮기기  
```app``` 모듈의 ```build.grandle```에 ```tensorflowlite```패키지를 추가해야 함

```html
dependencies {
    implementation 'org.tensorflow:tensorflow-lite:1.13.1'
}
```

```MainActivity``` 에서는 카메라로부터 캡처된 이미지를 가공하여 바이너리 이미지로 변환  
```Classifier```에서 이미지로부터 숫자를 예측  
```MainActivity``에서 예측된 숫자를 출력
