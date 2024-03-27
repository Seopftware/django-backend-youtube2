# one-password에서 가져와서 직접 .env 파일 생성 필요.
DB_NAME=youtube
DB_USER=inseop
DB_PASS=password123

# Django의 SECRET_KEY는 어떤 역활을 하죠?
DJANGO_SECRET_KEY=test # django 기본 인증 시 - session

# 민호님 생각하시기에 JWT를 사용하는 이유가 뭐라고 생각하시는지요!? 
# Token방식 인증은 -> 토큰이 어디에 저장되죠? -> (인규) 서버 -> Django에 부하가 걸린다.
# JWT -> 서버에 저장X -> 시크릿키만 갖고 있으면 JWT 데이터 해독이 가능하다.

# EC2 생성 후 추가
DJANGO_ALLOWED_HOSTS=*