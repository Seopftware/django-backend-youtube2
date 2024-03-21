from django.db import models
from common.models import CommonModel
from users.models import User

# - User: FK => subscriber (내가 구독한 사람) 100명 (잇섭이 채널을 삭제했어) -> 99명
# - User: FK => subscribed_to (나를 구독한 사람) 1만명 -> 9999명

# User:Subscrition => User(subscriber) => subscriber, subscriber, subscriber(FK)
# User:Subscrition => User(subscribed_to) => subscribed_to, ,subscribed_to, subscribed_to(FK)

class Subscription(CommonModel):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    subscribed_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')

    # subscriber_set -> subscriptions (내가 구독한 사람들)
    # subscribed_to_set -> subscribers (나를 구독한 사람들)