from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass   



# Video 세부 내용 REST API에서 댓글 내용도 볼 수 있도록 업데이트
# - comment model 정의
# - 
# - 

# 장고를 활용한 채팅 구현
# -socket, channel...

# 10년차. 1년을 10번 반복 => 1년차.
# 1년차.  3년,5년 => 5년차 연봉을
# IT업계. 계급장 다 때고, 실력으로.
# 마이스터고 출신의 고딩들이 나보다 더 높은 자리, 연봉, 실력 (산업근무요원)
# - 초딩때부터.. 부모님 개발자.