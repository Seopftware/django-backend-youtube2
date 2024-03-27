from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'password123')
DEBUG = bool(int(os.environ.get('DEBUG', 0))) # 0: False
ALLOWED_HOSTS = ['*'] # ec2-123-123-123

# EC2: Git, Docker Install -> docker-compose-deploy up

DJANGO_SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
 
CUSTOM_USER_APPS = [
    'users.apps.UsersConfig', # Config: label 변경할 일이 많다.
    'videos.apps.VideosConfig',
    'comments.apps.CommentsConfig',
    'subscriptions.apps.SubscriptionsConfig',
    'reactions.apps.ReactionsConfig',
    'rest_framework',
    'drf_spectacular',
    'channels',
    'chat.apps.ChatConfig',
    'daphne',
]

INSTALLED_APPS = CUSTOM_USER_APPS + DJANGO_SYSTEM_APPS

# Channels를 사용하기 위한 설정
ASGI_APPLICATION = 'app.route.application' # Socket (비동기 처리) + HTTP(동기)
# => FAST API (비동기) + (동기)

# 웹소켓 채팅 구현했습니다. => 오 대단한데요. 웹소켓의 원리가 뭔가요? (질문의도) - 면접관 본인이 알고 있어서.
# HTTP(단방향) 와 웹소켓(양방향)의 차이점은 뭐죠?
# HTTP - http://
# SOCKET - ws://, Hand Shake 양방향 통신이 가능해진다, Low Overhead, Frame(웹소켓에서 데이터를 나누는 단위)
# STREAMING - 영상 파일은 어떻게 보낼꺼냐? TCP/UDP, 3 ways hand shake
WSGI_APPLICATION = 'app.wsgi.application' # HTTP Base - REST API (동기 처리)

# 동기와 비동기
# 스타벅스에 들어갔어요.
# 내 앞에 사람이 녹차프라프치노휘핑크림7번시럽7번+옵션+벤티(만드는데 오래걸리겠죠.)
# 직원이 1명이야 (동기) -> 녹차프라프치노휘핑크림7번시럽7번 만들어야 -> 그 다음 내차례 (동기)
# 직원이 2명 이상 (비동기) -> 아아주세요 -> 아아주세요 -> 따듯한게 나와.

# Worker => FAST API
# 월, 화 - Django를 활용한 실시간 채팅(소켓) + AWS EC2에 배포(깃+도커)
# 기능/기술
# 강의 사이트 구현
# - 채팅(소켓, CS bot), 음성 스트리밍-영상 스트리밍(RSTP.RTMP)
# - 유튜브, 강의 추천 알고리즘(AI,모델링) - AI Engineer(점프) -> 대기업
# + REST API(30%)
# - 파이썬 백엔드 개발자 - AI(algorithms)
# - 회사 다니시면서 야간제 대학원(AI) // 돈이 없습니다. // 주말에 코딩 과외

# (수) => FAST API (매력에 빠지게 된다.) => 쉬워서.



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

import os
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS')
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/


STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django의 Custom UserModel - 기존 장고의 유저 인증 기능을 가져온다.
AUTH_USER_MODEL = 'users.User' # users 폴더의 User모델

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema'
}

CHANNEL_LAYERS = {
    "default": {
        "BACKEND" : "channels.layers.InMemoryChannelLayer"
    }
}