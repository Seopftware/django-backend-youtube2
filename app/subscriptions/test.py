# Q&A 세션
        # 질문: 현민
        # 직접 함수를 만들어서
        # *arg, **kwargs
        # - arg: 위치 기반
        # - kwargs: 키워드 기반

def func(*args):
    for arg in args:
        print(arg)

# func(1, 2, 3)와 같이 콤마로 구분된 위치 기반 인자를 전달할 때 사용
func(1, 2, 3)  # 출력: 1, 2, 3

def func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# func(a=1, b=2)와 같이 키워드=값 형태의 인자를 전달할 때 사용
func(a=1, b=2)  # 출력: a: 1, b: 2

def func(*args, **kwargs):
    print(args)  # 위치 기반 인자
    print(kwargs)  # 키워드 인자

func(1, 2, a=3, b=4)  # 출력: (1, 2), {'a': 3, 'b': 4}