# 외장함수
## sys
파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈  

## pickle
외장함수에서 객체의 형태는 그대로 유지하면서 파일을 저장하고 불러올수 있게 하는 모듈이다.

dump는 저장하는 것이고, load는 파일을 불러오는 것이다.

## os함수

```
import os
os.environ
environ({'PROGRAMFILES':'C:\User\user\PycharmProjects\study'})
```
내 컴퓨터의 기본 환경변수를 알수 있다.

☆ 디렉터리 위치 돌려받기
os.getcwd() 디렉터리 위치 돌려받기

os함수 종류  
mkdir -> 디렉터리 생성  
rmdir -> 디렉터리 삭제  
unlink ->  파일을 지운다.  
rename(a,b) -> a를 b로 바꾼다.  

# 함수종류

○ glob -> 파일을 리스트로 만들기
○ tempfile -> 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려줌
○ time ->현재 시간 알려주는 함수
localtime은 년,월,일,시를 알려준다.  
asctime -> 튜플형태로 알려준다.  

## calendar
파이썬에서 달력을 볼수 있게 해주는 모듈이다.

## sys.argv
인자값을 받을수 있는 방법을 제공한다. 
sys.argv 는 배열이다. 기본적으로 python 실행파일의 경로가 담겨있다. 

예 ) python tabto4.py minyoung kim
되어있으면 파일 다음에 적힌 파라미터가 argv[]에 들어가게 된다.
그래서 argv[1] 에는 minyoung 이들어가고, argv[2] 에는 kim 이 들어간다.  
