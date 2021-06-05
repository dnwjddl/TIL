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
  <Button
          android:layout_width= "wrap_content"
          android:layout_height="wrap_content"
          android:text="클릭해주세요"
          />
    <EditText
          android:layout_width = "wrap_content"
          android:layout_width = "wrap_content"
          android:hint = "무엇을 적을까요?" />

</LinearLayout>

```
