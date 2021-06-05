## Create New Project

![image](https://user-images.githubusercontent.com/72767245/120886196-b2c1c680-c627-11eb-875f-9f77a7fb16f8.png)

- package name은 무조건 소문자
- Language는 ```Java``` 와 ```Kotlin```중 고를 수 있다.


#### 가상 핸드폰 띄우기
Tools > AVD Manager > Create Virtual Device > System Image select (Q가 기본) > Finish

- 1080 x 1920 기본 
- Play를 통해서 되는지 확인 (에러뜰 수 도 있음 -> path 관련해서)


## Play

- play를 하면 핸드폰(Emulator) 뜸

## 구조
- app 폴더 내
  - manifests
  - java
    - ```main activity```
    - (test)로 되어있는 애들은 볼 필요없음 지워도 됨
  - java(generated) : 볼 이유도 수정할 이유도 없는 친구
  - res : 코드 형식도 있고 그림 형식도 있음
    - drawable
      - 코드를 이해할 필요는 없음. 있다는 것만 알면 됨
    - layout
      - Activity_main 있음 : 화면 구상 가능
      - 앱 최초의 형식 볼 수 있음
    - mipmap
      - ic_launcher: 그림 볼 수 있음
      - ic_launcher_round
    - values
      - 주요 색깔 볼 수 있음
      - 색깔 표현하는 단위

![image](https://user-images.githubusercontent.com/72767245/120889913-751a6900-c63a-11eb-8524-2cc4ee09bf03.png)

#### 어플의 아이콘
- Res > drawable > IC_launcher_background.xml + IC_launcher_foreground.xml

- ```xml```파일 형식은 아무리 확대를 해도 픽셀이 뭉개지지 않음
- Mipmap 내 IC_launcher의 XML은 drawable 내의 xml 합친 것

### Layout>Activity_main
- Constraint는 어려울 수 있으므로, Linear Layout으로 바꿈

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
  
  <Button -> 만 해도 필요한 코드 나옴>

</LinearLayout>

```

