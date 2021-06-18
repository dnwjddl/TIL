## Button Click Event

### ```activity_sub.xml```
- ```res``` > ```layout``` > ```activity_sub.xml```

```xml
<?xml version = "1.0" encoding = "utf-8"?>
<LinearLayout
            xmlns:android="http://schemas.android.com/apk/res/android"
            android:layout_width = "match_parent"
            android:layout_height = "match_parent"
            android:oriteation = "horizontal"
            android:weightSum = "1">
  <Button
          android:layout_width = "wrap_content"
          android:layout_height = "wrap_content"
          android:text = "Button1"
          android:onClick = "BtnClick"
          />
  
```

저기서 말한 BtnClick -> 눌렀을 때 실행할 수 있게 하는거

```java
//SubAcitivity.java

public class SubAcitivity extends AppCompatAcitivity{
  @Override
  protected void onCreate(Bundle saved InstanceState){
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
  }
  
    public void Btn1Click(View v){
        Toast.makeText(this, "ㅋㅋ", Toast.LENGTH_SHORT).show();
    }
}

```

>> 이러면 button1을 클릭하면 Btn1Click이라는게 실행돼서 "ㅋㅋ"가 Toast로 뜨게 된다

```Toast```: 알림이 떴다가 사라지는 글씨

### 원하는 위치로 바꾸기
#### 기존

```java
public void Btn1Click(View v){
   Toast.makeText(this, "ㅋㅋ", Toast.LENGTH_SHORT).show();
}
```

#### 바뀐 위치
```java
public void Btn1Click(View v){
   Toast toast = Toast.makeText(this, "ㅋㅋ", Toast.LENGTH_SHORT); //객체 생성, LENGTH_SHORT: 빠르게 사라짐, LENTH_LONG: 길게 있다가 사라짐
   toast.setGravity(Gravity.END | Gravity.BOTTOM, ```xOffset``:10, ```yOffset```:10); //x랑 y 정함(END, BOTTOM)
   toast.show();
}
```

### layout에서 xml로 Button 만들기
```xml
<Button
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"
   android:text="버튼2"
   android:id="@+id/Btn2" />
```

```java
@Override
protected void onCreate(Bundle savedInstanceState){
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    
    View Btn2 = findViewById(R.id.Btn2); //View 형식으로 받게 됨
    //id로 받아옴(id는 버튼에 부여함)
}
```

- button은 View 보다 상위개념
- ctrl+ space
- import 안되어있을때 alt+enter


```java
@Override
protected void onCreate(Bundle savedInstanceState){
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    
    Button Btn2 = findViewById(R.id.Btn2); //View 상위 Button
    Btn2.setOnClickkListener(new View.OnClickListener(){
           @Override
           public void onClick(View view){
                Log.d("태그", "값"); //값을 log로 print함
           }
    }
}
```

### Button3으로 MainActivity 넘어가기
