# android_study
android_study 

### Empty Activity
최소한의 구성요소만 포함된 레이아웃 파일 & 코드 파일 지원
####  두개의 파일 생성
- **```activity_main.xml```** : ConstraintLayout에 Text view 하나가 추가된 XML 레이아웃 파일
- **```MainActivity.java```** : OnCreate 메소드만 추가되어 있는 Activity Class가 포함된 자바 코드 파일

```java
package com.example.myapplication;

# androidx로 시작하는 패키지를 import 함
import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        # 자바 코드는 하나의 Activity로 사용할 Layout 파일을 지정하고 있음
        setContentView(R.layout.activity_main);
    }
}

```
#### 프로젝트 폴더와 파일 설명
안드로이드 프로젝트 구조는 ```안드로이드 뷰```와 ```프로젝트 뷰```로 볼 수 있음

![image](https://user-images.githubusercontent.com/72767245/106718276-2fc23c80-6644-11eb-8084-06137406fba4.png)


1. app/**manifests**
  - ```AndroidManifest.xml``` : app 모듈의 manifest 파일
    - manifest 파일에는 안드로이드 시스템이 **앱을 실행하기 위한 필요한 정보**를 정의한다
    - (앱에 대한 고유 식별자 역할) package 이름, Activity 관련 설정, 서비스 등과 같은 앱의 구성요소, 시스템 기능을 사용하기 위한 필요한 permission 선언, 테마 등을 포함
    
2. app/**java**
  app 모듈의 자바 코드 파일. 패키지 이름으로 분류
  - ```MainActivity.java```
    - Activity에 대한 클래스 정의가 되어있는 java 파일(Activity의 동작을 코드로 작성)
    - ```MainActivity 클래스```는 default로 앱 실행이 시작되는 Activity
      - 앱의 실행이 시작되는 코드로 여기에서 지정한 레이아웃을 화면에 처음 보여줌
    
3. app/**res**
  app 모듈에서 사용되는 모든 리소스 파일들이 종류별로 저장
  - drawable
    - 앱에서 사용되는 이미지 파일과 관련 파일
    
  - layout
    - 액티비티의 레이아웃을 정의한 xml 파일 
      - activity_main.xml
        - 액티비티의 레이아웃을 정의한 xml 파일 
        - 이 파일에 추가한 UI 컨포넌트들이 화면에 보여지게 된다
   - mipmap
     - 런처 아이콘에 사용되는 이미지가 디바이스 해상도 별로 저장
     - 안드로이드 디바이스에서 해당 앱을 실행하기 위한 터치할 때 보이는 아이콘
  - values
     앱에서 사용되는 리소스 관련 상수를 정의한 파일들로 저장 ID로 참조하게 된다
     - colors.xml
       - 앱에서 사용되는 색의 값을(16진수 값)으로 정의해놓습니다
     - strings.xml
       - 앱에서 사용되는 문자열을 정의해놓습니다.
     - styles.xml
       - 뷰나 윈도우의 모습을 위한 속성을 지정해 줄 수 있습니다.
4. Gradle Scipts
  **Grandle** 빌드 시스템에서 앱을 컴파일 및 빌드시 사용되는 파일
    - ```build.grandle (Project: HelloWorld)```
      - 전체 프로젝트를 위한 파일, 모든 모듈에 적용되는 빌드 구성을 정의
    - ```build.grandle (Module:app)
      - 프로젝트에 포함되어 있는 app 모듈을 위한 파일. 모듈 별로 하나씩 존재하며 각 모듈에 대한 빌드 구성을 정의
      - 빌드에 사용되는 SDK와 Tools에 대한 버전이 설정
