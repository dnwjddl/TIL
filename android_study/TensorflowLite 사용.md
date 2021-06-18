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
# 모델 convwerter
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# 모델 저장
open(mnist.tflite', 'wb').write(tflite_model)
```
