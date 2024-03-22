from django.db import models
from common.models import CommonModel
from django.db.models import Count, Q

# - User: FK
# - Video: Fk
# - reaction (like, dislike, cancel) => choice

# 갯수를 불러와야해 => Video REST API

# 러닝커브 -> 본질 강화가 된다. 개발 5년하면 여러분들 REST API, AUTH => 생산성이 증가. => 연봉.
# 기술이 새로 나오잖아요? 공부해야지.... ㄷㄷㄷ
# Fast API , GPT -> Prompt Engineering, 탈옥
# 웹툰 => 결국 끝까지가면 내가 다 이겨
# 50명 -> 20명 정도만 개발자. 다른거 하는 거 같아요. 
# 3년정도 -> PM. 창업.마케터.솔루션 아키텍처(성과) - 창업/교육

class Reaction(CommonModel):
    # circular import error
    # user = models.ForeignKey(User, ) 
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTON_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )

    # column: reactions -> migration -> reaction -> migration
    reaction = models.IntegerField(
        choices=REACTON_CHOICES,
        default=NO_REACTION
    )
    
    @staticmethod # ORM depth2 모델.obejcts.get, filter().aggregate() # SQL: JOIN QUERY
    def get_video_reaction(video): # 1번 비디오 - 좋아요/싫어요 갯수 궁금
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE))
        )
        
        return reactions
    
    # 모르는 상태로 프로젝트를 한~참 진행해서 복잡해진후에 발견하면. 어찌하는지.
    # - 테이블많고, 컬럼많고. 데이터 많이 쌓여있고.
    # - 컬럼추가해서 기존컬럼 데이터 살리면서 새로운 컬럼으로 옮길 수도 있고.
    # 그 변수명에 연결된 코드들이 많을 때도 있고 다양한 일이 생길것 같아서요.
    # Postmortem(회고), Code Refactoring, Code Review


    # BE_02_신현민질문이 있는데요. 
    # 싫어요 같은경우에 좋아요를 줄이는것도 맞지만 좋아요 보다 싫어요가 많은 경우도 있을텐데요. 
    # 시청자는 안보이지만 유튜버는 확인 가능하지 않나요? 제가 유튜버가 아니라 정확하진 않지만.

    # BE_02_김민정유저 한명당 좋아요든 싫어요든 한번만 할 수 있게도 해야할거 같아요

# BE_02_윤소희주말에 복습 몰아서 하려고 그러는데 아예 처음부터 다 하는게 좋을까요 
# 아님 어디부터 하면 좋을거다 추천하는 쪽 있으실까요 ? 갑자기 뜬금없는 질문이긴 하지만,,ㅋㅋㅠ
# - 2배속으로 한번 쭉 들으거 같긴해요. (프로젝트까지 기간이 좀 남아있으시잖아요.)    
    


# BE_02_윤소희소문자, 대문자 사용해야할 때가 헷갈리네여ㅠ,ㅠ
# - 클래스명 지을 때 -> Camel Case => TestCase
    