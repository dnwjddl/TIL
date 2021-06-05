## Main activity
```java
public class MainActivity extends AppCompatActivity{ //AppCompatActivity를 MainActivity가 상속 받고 있음
  @Override
  protected void OnCreate(Bundle savedInstanceState){ //onCreate는 앱 처음 실행할때의 함수
    super.onCreate(savedInstanceState); //현재 UI를 일단 저장해놓는 코드
    setcontentView(R.layout.activity_main); //R은 Resources의 약자임
}
//Ctrl + O 를 치면 함수들 구성 가능
//Android Studio Life Cycle 내의 함수들 구경 가능

```


### Life Cycle

![image](https://user-images.githubusercontent.com/72767245/120891045-62576280-c641-11eb-8e9f-7fd6a5fc102a.png)

- ```onCreate()```: 앱 시작
- ```onStart()```: 앱 시작하고 바로 시행
- ```onResume()```: 돌아옴
- ```onStop()```:뒤로 가기등
- ```onRestart()```: 아예 끄지않고 다시 실행하면 onRestart 후 onStart()로 이동
