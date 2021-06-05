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
