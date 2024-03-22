from django.urls import path
from . import views

# Django -> Main API
# FAST API -> Sub API (Micro Service)

urlpatterns = [
    path('', views.SubscriptionList.as_view(), name='sub-list'), # api/v1/sub
    path('<int:pk>', views.SubscriptionDetail.as_view(), name='sub-detail') #api/v1/sub/{pk}
]

# docker-compose run --rm app sh -c 'python manage.py makemigrations'
# docker-compose run --rm app sh -c 'python manage.py migrate'
# docker-compose run --rm app sh -c 'python manage.py test subscriptions'