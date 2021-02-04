#### [특강_SW개발] API를 사용하여 요리를 만드는 법
## 서버, 클라이언트

- 클라이언트 -(크롬, 익스플로어를 이용하여)-> 서버 (ex. 유튜브)
- 서버의 컴퓨터 주소는 IP주소(193.221...)
- 서버의 도메인은 nolan.com

페이지 클릭 할 때마다 모든 정보를 서버에서 보내니 서비스가 느려짐
- 페이지가 뀌어도 그대로인 데이터는 서버가 아닌 핸드폰에 저장하여 보낼 데이터양을 줄임
- 컴퓨터에선 ```프로그램 설치``` & 스마트폰에선 ```앱설치```
- 단 클라이언트 데이터는 "수정이 어렵다"

서버와 클라이언트의 대화하는 규칙(API, JSON)
- 대화의 규칙: API
- 메세지 포맷: JSON
대화의 규칙이 있다면 서버가 일을 하기 훨씬 수월하다.  

#### REQUEST
- POST: 올려줘
- GET: 불러와줘
- PUT/PATCH: 수정해줘
- DELETE: 지워줘

#### RESPONSE
- 200: 좋아
- 400: 니가 잘못해서 싫어
- 500: 내가 잘못해서 안돼

**함께 만든 통일된 대화 규칙을 REST API라고 부른다**



## API(Application Programming Interface)
- 일반적으로 API는 프로그램이나 서비스를 만들 때 사용하는 인터페이스
- 종류
  - Open API
    - 외부에서도 사용하도록 공개한 API들(ex. 주소 검색, 번역)
  - REST API
    - HTTP 메소드로 접근 가능한 API
    
[API 더 알아보기](https://brunch.co.kr/@businessinsight/65)  

[GET API](https://api.github.com/search/repositories?q=hackathon)  

[GITHUB API](https://github.com/sahat/hackathon-starter)  

### API 사용하는 방법
#### REST API
- REST API는 POST/GET/PUT/DELETE 등 HTTP 메소드를 이용해서 호출 (GET, POST 쓰는 경우가 대부분)
- GET
  - shell에서 curl로 요청 가능
  - Browser에서 해당 주소를 입력하면 GET으로 요청됨
- POST
  - 사진과 같이 파일을 요청에 함께 보내거나, 발급받은 사용키(API-Key)를 같이 보내야 한다면 보통 POST 요청으로 보냄
  - **```Postman```** 사용하여 Post 사용가능
  
