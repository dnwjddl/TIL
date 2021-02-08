```
git clone https://github.com/tensorflow/examples
```

# 실행화면
![image](https://user-images.githubusercontent.com/72767245/106785994-65d9dd80-6691-11eb-85c9-9d5aef6c5fdc.png)
![image](https://user-images.githubusercontent.com/72767245/106786082-7f7b2500-6691-11eb-8a57-915564601e9e.png)

# 코드 분석
## 🦕Gradle Scripts
### 🤩Tensorflow lite 사용🤩 
```build.gradle(Module)``` 

```java
dependencies {
    ...
    // TF Lite
    implementation 'org.tensorflow:tensorflow-lite:0.0.0-nightly-SNAPSHOT'
    ...
}
```
### 글씨작성
```build.gradle(Module)``` 

```java
dependencies {
    ...
    // AndroidDraw Library
    implementation 'com.github.divyanshub024:AndroidDraw:v0.1'
    ...
}
```
```build.gradle(Project)```  
Android Draw라는 깃헙의 라이브러리는 maven을 꼭 작성하게 되어있다

```java
// maven은 꼭 작성해주어야 함
allprojects {
    repositories {
        google()
        jcenter()
        maven { url 'https://jitpack.io' }
    }
}
```
# Source 코드 확인
- ```manifests```
    - ```AndroidManifest.xml```: 전체적인 프로젝트 구조
- ```java```
    - org.tensorflow.lite.examples.digitclassifier
        - ```DigitClassifier```
        - ```MainActivity```
- ```assets```
- ```res```: resource 가지고 있음 (아이콘, 레이아웃 구현)
    - drawable
    - layout
    - mipmap
    - values : color values, strings values, styles values

## AndroidManifest.xml
Activity가 여러개일수도 있음 (해당 예시는 Main Activity내에서 모든 Activity 결정
```xml
...
    <activity android:name=".MainActivity"
                  android:exported="true">
...
```

## MainActivity
package 정의, 필요한 class 가지고 옴
```java
package org.tensorflow.lite.examples.digitclassifier

import android.annotation.SuppressLint
import android.graphics.Color
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.util.Log
import android.view.MotionEvent
import android.widget.Button
import android.widget.TextView
import com.divyanshu.draw.widget.DrawView
```
```java
// 네가지 행위
// 그리기, 지우기, 보여주기, 예측하기
class MainActivity : AppCompatActivity() {

  private var drawView: DrawView? = null
  private var clearButton: Button? = null
  private var predictedTextView: TextView? = null
  private var digitClassifier = DigitClassifier(this)
```

```java
 @SuppressLint("ClickableViewAccessibility")
 //onCreate(생성자): 생성이 될때 이런 행동을 해라
 override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    // res폴더/layout폴더/tfe_dc_activity_main.xml 파일
    setContentView(R.layout.tfe_dc_activity_main)
    
    // Setup view instances
    // layout에서 보면 각 화면은 id를 가지고 있음(ex.draw_view)
    drawView = findViewById(R.id.draw_view)
    drawView?.setStrokeWidth(70.0f)
    drawView?.setColor(Color.WHITE)
    drawView?.setBackgroundColor(Color.BLACK)
    clearButton = findViewById(R.id.clear_button)
    predictedTextView = findViewById(R.id.predicted_text)
    
    // Setup clear drawing button
    // EVENT을 준다
    clearButton?.setOnClickListener {
      drawView?.clearCanvas()
      predictedTextView?.text = getString(R.string.tfe_dc_prediction_text_placeholder)
    }
    
    
    // MAIN LOGIC
    drawView?.setOnTouchListener { _, event -> drawView?.onTouchEvent(event)
      if (event.action == MotionEvent.ACTION_UP) {
        classifyDrawing()
      }
      true
    }
 ```
 Digit Classifier 초기화
 ```java
   // Setup digit classifier
   digitClassifier
     .initialize()
     .addOnFailureListener { e -> Log.e(TAG, "Error to setting up digit classifier.", e) }
  ```
  Digit Classifier 실행
  - bitmap은 Draw한 그림
  ```java
    private fun classifyDrawing() {
    val bitmap = drawView?.getBitmap()

    if ((bitmap != null) && (digitClassifier.isInitialized)) {
      digitClassifier
        .classifyAsync(bitmap)
        .addOnSuccessListener { resultText -> predictedTextView?.text = resultText }
        .addOnFailureListener { e ->
          predictedTextView?.text = getString(
            R.string.tfe_dc_classification_error_message,
            e.localizedMessage
          )
          Log.e(TAG, "Error classifying drawing.", e)
        }
    }
  }

  companion object {
    private const val TAG = "MainActivity"
  }
}
```
  
  프로그램 종료
  
```java
override fun onDestroy() {
    digitClassifier.close()
    super.onDestroy()
  }
 ```
  
 ### Digit Classifier
 - 실제 프로그램 돌릴때에는(MainActivity에서는) ```digitClassifier.classifyAsync(bitmap)```으로 실행
  ```java
  import org.tensorflow.lite.Interpreter
  ```
  
  ```java
  class DigitClassifier(private val context: Context) {
    private var interpreter: Interpreter? = null
    var isInitialized = false
        private set
  ```
```java
fun initialize(): Task<Void> {
    val task = TaskCompletionSource<Void>()
    executorService.execute {
      try {
        initializeInterpreter() //이 함수 사용
        task.setResult(null)
      } catch (e: IOException) {
        task.setException(e)
      }
    }
    return task.task
  }
```
initializaInterpreter 함수 : interpreter을 준비시켜주는 함수
- asset 폴더 안에 mnist.tflite파일 존재
- loadModelFile을 사용하여 model 불러오기
- interpreter에 model, options 가지고와서 model 돌려주기
```java
 @Throws(IOException::class)
 private fun initializeInterpreter() {
    // assetManager을 이용하여 TF Lite model load
    val assetManager = context.assets
    val model = loadModelFile(assetManager)

    // Initialize TF Lite Interpreter with NNAPI enabled
    val options = Interpreter.Options()
    options.setUseNNAPI(true)
    val interpreter = Interpreter(model, options)

    // Read input shape from model file
    val inputShape = interpreter.getInputTensor(0).shape()
    inputImageWidth = inputShape[1]
    inputImageHeight = inputShape[2]
    modelInputSize = FLOAT_TYPE_SIZE * inputImageWidth * inputImageHeight * PIXEL_SIZE

    // Finish interpreter initialization
    this.interpreter = interpreter
    isInitialized = true
    Log.d(TAG, "Initialized TFLite interpreter.")
  }
```
initializeInterpreter() 내에 있는 loadModelFile함수
```java
@Throws(IOException::class)
 private fun loadModelFile(assetManager: AssetManager): ByteBuffer {
    val fileDescriptor = assetManager.openFd(MODEL_FILE)
    val inputStream = FileInputStream(fileDescriptor.fileDescriptor)
    val fileChannel = inputStream.channel
    val startOffset = fileDescriptor.startOffset
    val declaredLength = fileDescriptor.declaredLength
    return fileChannel.map(FileChannel.MapMode.READ_ONLY, startOffset, declaredLength)
  }
```
실제 실행할때 사용하는 classifityAsync
- executerService에서 classifier 하는 것
- result 는 ```classifiy(bitmap)``` 임
```java
fun classifyAsync(bitmap: Bitmap): Task<String> {
    val task = TaskCompletionSource<String>()
    executorService.execute {
      val result = classify(bitmap)
      task.setResult(result)
    }
    return task.task
  }
```
상수들 선언

```java
companion object {
    private const val TAG = "DigitClassifier"

    private const val MODEL_FILE = "mnist.tflite"

    private const val FLOAT_TYPE_SIZE = 4
    private const val PIXEL_SIZE = 1

    private const val OUTPUT_CLASSES_COUNT = 10
  }
```
classifiy
```java
private fun classify(bitmap: Bitmap): String {
    if (!isInitialized) {
      throw IllegalStateException("TF Lite Interpreter is not initialized yet.")
    }

    var startTime: Long
    var elapsedTime: Long

    // Preprocessing: resize the input
    startTime = System.nanoTime()
    
    //전처리
    val resizedImage = Bitmap.createScaledBitmap(bitmap, inputImageWidth, inputImageHeight, true)
    val byteBuffer = convertBitmapToByteBuffer(resizedImage)
    
    elapsedTime = (System.nanoTime() - startTime) / 1000000
    Log.d(TAG, "Preprocessing time = " + elapsedTime + "ms")

    startTime = System.nanoTime()
    val result = Array(1) { FloatArray(OUTPUT_CLASSES_COUNT) }
    interpreter?.run(byteBuffer, result)
    elapsedTime = (System.nanoTime() - startTime) / 1000000
    Log.d(TAG, "Inference time = " + elapsedTime + "ms")

    return getOutputString(result[0])
  }

```
bitmap을 bytebuffer 형식으로 바꾸어준다
```java
private fun convertBitmapToByteBuffer(bitmap: Bitmap): ByteBuffer {
    val byteBuffer = ByteBuffer.allocateDirect(modelInputSize)
    byteBuffer.order(ByteOrder.nativeOrder())

    val pixels = IntArray(inputImageWidth * inputImageHeight)
    bitmap.getPixels(pixels, 0, bitmap.width, 0, 0, bitmap.width, bitmap.height)

    for (pixelValue in pixels) {
      val r = (pixelValue shr 16 and 0xFF)
      val g = (pixelValue shr 8 and 0xFF)
      val b = (pixelValue and 0xFF)

      // Convert RGB to grayscale and normalize pixel value to [0..1]
      val normalizedPixelValue = (r + g + b) / 3.0f / 255.0f
      byteBuffer.putFloat(normalizedPixelValue)
    }

    return byteBuffer
  }

```
가장 큰 값을 return, 출력을 보여주는 함수 (Main Activity에서 이어짐 Text)
```java
private fun getOutputString(output: FloatArray): String {
    val maxIndex = output.indices.maxBy { output[it] } ?: -1
    return "Prediction Result: %d\nConfidence: %2f".format(maxIndex, output[maxIndex])
  }
```
