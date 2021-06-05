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
    - ```AndroidManifest.xml```: 안드로이드 메니페스트는 다 합쳐주는 거같음 (환경 설정)
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
      - colors.xml
        - 주요 색깔 볼 수 있음
        - 색깔 표현하는 단위
      - strings.xml
        - <string name = "app_name">Test28</string> 
      - style.xml - color에서 연결해주는 애임
        - <item name = "colorPrimary">@color/colorPrimary</item>

![image](https://user-images.githubusercontent.com/72767245/120889913-751a6900-c63a-11eb-8524-2cc4ee09bf03.png)

#### 어플의 아이콘
- Res > drawable > IC_launcher_background.xml + IC_launcher_foreground.xml

- ```xml```파일 형식은 아무리 확대를 해도 픽셀이 뭉개지지 않음
- Mipmap 내 IC_launcher의 XML은 drawable 내의 xml 합친 것


---

-> ```AndroidManifest.xml``` 내에 모두 포함
```xml
<application
             android:allowBackup="true" //앱이 파괴되었을 때, 백업을 허용하냐 안하냐
             android:icon = "@mipmap/ic_launcher" // 앱 아이콘 (여러개 중 핸드폰에 맞는걸 알아서 선택)
             android:label = "@string/app_name" //string.xml안에 있는 그 string 뜻하는듯 . 앱 이름
             android:roundIcon = "@mipmap/ic_launcher_round" //앱 아이콘인데 동그란거 (이것도 알아서 선택)
             android:supportsRtl = "true" //Right to Left로 해줌
             android:theme = "@style/AppTheme"> //테마(색깔 입힘)
  
  //Java 내 Mainactivity 실행 
    <activity android:name = ".MainActivity"> 
        <intent-filter>
           <action android:name="android.intent.action.MAIN"/> //Java 내 Mainactivity 실행 
           <category android:name = "android.intent.category.LAUNCHER"/>
        </intent-filter>
    </activity>
   
</application>
  
  
```
```xml
<?xml version = "1.0" encoding = "utf-8"?> // xml의 버전이랑, 한글 지원해줌
<manifest xmlns:android="https://schemas.android.com/apk/res/android" package = "com.test.test28"> //패키지는 고유의 패키지(중복 안됨) 전부 소문자여야 함
```
### AndroidManifest.xml을 통해서 아래 모든 것 제어 가능

