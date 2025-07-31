# 심화반 프로젝트 기획서
## 메뉴판 도우미



## 주제 및 선정배경

해외 여행에서 현지 언어로 쓰인 메뉴판을 알아보기 힘들 때 한국말로 설명해주는 앱.

메뉴판 이미지를 업로드 하면 메뉴판에 있는 음식들을 한국말로 설명해주고 구글 이미지 검색 api를 이용하여 음식 사진을 보여준다.


## 사용기술
* Python, PyQt5, Qthread
* OpenAI API
* Google Image Search API



## 전체흐름
1. 메뉴판 이미지 업로드
2. GPT API를 호출하여 메뉴판 이미지 분석 요청
3. Google Image Search API 호출하여 이미지 검색 요청
4. 분석 결과를 텍스트와 하이퍼 링크 형태로 표시
5. [사진보기]를 클릭하면 기본 웹 브라우저로 사진을 볼 수 있다



## 시스템 구성도(Architecture)

```
[ 사용자 ]
   ↓
[ PyQt5 GUI ]
   ↓
[ 이미지 ]
   ↓
[ GPT API 호출 ]
   ↓
[ Google Image Search API 호출 ]
   ↓
[ 결과 출력 ]
```


## 디렉터리 구조

```
project/
├─ gui/
│   └──main.app.py
├─ api/
│   └──openai_api.py
│   └──google_image_search_api.py
├─ utils/
│   └──file_handler.py
│   └──config.py
├─ main.py
├─ .env
```


## 예시 시나리오

1. 현지 음식점에 가서 찍은 메뉴판 사진을 업로드 한다.
2. 자동으로 GPT 검색 및 이미지 검색 결과를 화면에 출력한다.
3. 음식 사진을 확인하고 싶은 메뉴를 클릭하여 사진을 확인할 수 있다.