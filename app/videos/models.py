from django.db import models
from common.models import CommonModel
from users.models import User

class Video(CommonModel):
    title = models.CharField(max_length=30, required=True)
    description = models.TextField(blank=True)
    link = models.URLField()
    category = models.CharField(max_length=20)
    views_count = models.PositiveIntegerField(default=0)
    thumbnail = models.URLField() # S3 Bucket -> Save File -> URL -> Save URL
    video_file = models.FileField(upload_to='storage/') # 파일을 저장하는 방법
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) # 운영의 문제
    # 해외 진출 -> 데이터 저장 이슈 (유로6)

    # 플젝 경험 => 이직 할 때.
    # 연봉ㅔㅐ
        # - 연봉 2~3천 시작: 3천 3~5%/동결 -> 3천1백50 -> 5천가는데 10년. (3천 = 대체 가능)
        # - 연봉 4~5천 시작: 4000 -> 5500 -> 7000~8000 -> 1억 (5년)
        # - 연봉 1억: 절대 잡무를 시키지 않습니다. 양질의 프로젝트를 맡겨요. => 이직도 쉽고, 연봉이 더 잘 올라.
        # 남성: 소개팅 100번. => 메타인지.  50번째 부터는 애프터 계속 받을 자신있다.
        # 나의 기술로 연봉 => 소프트 스킬 (나의 매력) -> 내 앞에 앉아있는 면접관 2명 설득하는 거
    
    # 입사 후 기술 발전(=프로젝트 경력)은 어떻게 하신건지 여쭤보다도 될까용?
        # - 저 백엔드코드 리뷰하고 싶어요. (python) => 쌩PYTHON , C++, Go Lang
        # - 안드로이드SDK => WEB SDK, Flutter SDK (연봉 내껄로 가져오고)
        # - 코드가 익숙해지면 시간이 좀 남아요.


# User:Video => 1:N
    # => User : Video, Video, Video, Video, Video => O
    # => Video: User, User, User (유튜버 3명이 찍은 영상) => X