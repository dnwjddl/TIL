# TMUX
tmux을 사용하면 한 터미널에 있는 여러 프로그램 간에 쉽게 전환할 수 있으며, 프로그램을 분리한 다음 다른 터미널에 다시 연결할 수 있음  
tmux 세션은 지속적이므로, 연결이 끊겨도 tmux에서 실행중인 프로그램이 계속 실행됨  
tmux의 모든 명령은 접두사로 시작되며, 기본적으로 ```Ctrl+b```  

### 사용 흐름
- 터미널에서 tmux 세션 띄우기 > 세션 내 윈도우 생성 > 윈도우로 작업(pane으로 나누던가 안나누던가)

```
#세션 생성
$ tmux
$ tmux new -s <session_name> -n <window-name>

#세션 종료
$ exit

#세션 다시 시작
$ tmux attach -t <session_number> (or session_name)

# 세션 중단하기
(ctrl+b) d


```


---

**TMUX 용어**

- ```Session(세션)```: tmux가 관리하는 가장 큰 실행단위, tmux는 세션에 attach/detach할 수 있음. Tmux가 detach한 세션은 종료되지 않고 백그라운드에서 실행을 계속 진행할 수 있음. 세션은 여러 window로 구성됨
- ```window(윈도우)```: 사용자가 보는 터미널 화면, 세션에서 여러 개의 윈도우가 탭처럼 존재. 세션에서 윈도우를 전환하면 새로운 윈도우로 화면이 전환된다
- ```pane(팬)```: 하나의 윈도우를 분할한 단위. 윈도우 하나를 여러번 분할해서 여러개의 팬을 갖게 할 수 있다. 가로 혹은 세로로 화면을 분할해가면서 팬을 생성함. 윈도우를 전환하면 팬 구성도 새로운 윈도우의 구성으로 전환


---

session 하나에 두개의 window  

-> 현재는 1번 윈도우가 활성화되어있으며, 0번 윈도우로 전환하면 1번 윈도우의 화면은 백그라운드로 전환

![image](https://user-images.githubusercontent.com/72767245/127642626-3c8828b0-dae0-494b-9f84-bc285d515db2.png)



---

하나의 윈도우는 여러개의 팬(Pane)으로 분할해서 사용 가능  
각각의 팬은 별도의 터미널처럼 사용가능  

![image](https://user-images.githubusercontent.com/72767245/127642822-5e4e2e75-bcbd-4f57-a76d-6c3e4a34b0a6.png)

1번 팬에서 vi을 열어서 소스코드를 보는 동시에 2번 팬에서 컴파일을 하고 3번 팬에서 로그를 열어볼 수 있음

---


### Session 관련 tmux 명령어

```
# 세션 생성(이름은 숫자로 생성)
$ tmux

# 이름을 지정하여 세션 생성
$ tmux new -s <session_name>
$ tmux new-session -s <session_name>

# 세션 이름 수정
[Ctrl] + b,  $

# 세션 detach
[Ctrl] + b,  d

# 세션 리스트보기
$ tmux ls

# 세션 attach
$ tmux attach -t <session number 혹은 session name>

# 세션 종료, 세션의 마지막 윈도우, 마지막 팬에서 실행
$ exit 

# 세션 종료, 세션 밖에서 실행
$ tmux kill-session -t session_name

```

### Window 관련 tmux 명령어

```
# 윈도우 생성
[Ctrl] + b, c

# 세션 생성과 함께 윈도우 생성
$ tmux new -s <session-name> -n <window-name>

# 윈도우 이름 변경
[Ctrl] + b, ,

# 윈도우 종료
[Ctrl] + b, &
[Ctrl] + d

# 다음 윈도우(Next Window)로 이동
[Ctrl] + b, n

# 이전 윈도우(Previous Window)로 이동
[Ctrl] + b, p

# 마지막 윈도우(Last Window)로 이동
[Ctrl] + b, l

# 특정 윈도우로 이동 (몇 번째 윈도우인지)
[Ctrl] + b, 0-9 

# 특정 윈도우로 이동 (이름으로 이동)
[Ctrl] + b, f

# 윈도우 리스트 보기
[Ctrl] + b, w
```


### Pane 관련 tmux 명령어

```
# 세로 화면 분할
[Ctrl] + b, %

# 가로 화면 분할
[Ctrl] + b, "

# 팬 이동 - 화면에 나오는 숫자로 이동
[Ctrl] + b, q 

# 팬 이동 - 순서대로 이동
[Ctrl] + b, o

# 팬 이동 - 방향키로 이동
[Ctrl] + b, <방향키>

# 팬 삭제
[Ctrl] + d
[Ctrl] + b, x

# 팬 사이즈 조절 - 현재 포커스된 팬 전체화면(한번 더 실행하면 윈상복구)
[Ctrl] + b, z

# 팬 사이즈 조절 [Ctrl] + b 를 누른 후 :
[Ctrl] + b, :
resize-pane -L <Size> or -R <Size> or -U <Size> -D <Size>                  

# 팬 레이아웃 변경 (다양한 레이아웃으로 자동 전환)
[Ctrl] + b, spacebar
```

### 단축키 명령어
```
# 단축키 목록
$ [Ctrl] + b, ?

# 키 바인딩 및 언바인딩
[Ctrl] + b, :
bind-key [-cnr] [-t key-table] key command [arguments]
unbind-key [-acn] [-t key-table] key

# 옵션 설정 - set-option
[Ctrl] + b, :
set -g <option-name> <option-value>

# 옵션 설정 - set-window-option
[Ctrl] + b, :
setw -g <option-name> <option-value>

# 열려있는 모든 팬에 동시 입력하기
[Ctrl] + b, :
setw synchronize-panes on
```



---


$ ctrl + b + d    # hide

Panes(Split)
- Panes는 한 윈도우에서 화면분할을 할 때 사용

```
# horizontal split
#          |
#     1    |    2
#          |
$ ctrl + b + %

# vertical split
#           1
# ---------------------
#           2
$ ctrl + b + "



````
