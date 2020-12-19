import math     # 수학 모듈 사용

# 절댓값 알고리즘 1(부호판단)
# 입력: 실수 a
# 출력: a의 절댓값
def abs_sign(a):
    if a>=0:
        return a
    else:
        return -a

# 절댓값 알고리즘 2(제곱-제곱근)
# 입력: 실수 a
# 출력: a의 절댓값
def abs_square(a):
    b=a*a
    return math.sqrt(b)     # 수학 모듈의 제곱근 함수

# 제곱수의 제곱근을 검출하는 알고리즘
# 입력: 정수 a
# 출력: a의 제곱근
def square_joseon(a):
    record=int(a)
    a=a/2
    b=1
    while True:
        if a-b>0:
            a=a-b
            b=b+1
        else:
            a=a*2
            a=int(a)
            if(record==a*a):
                print(record+"의 제곱근: ")
                return a
            else:
                print("제곱수가 아님")
                return a


print(abs_sign(5))
print(abs_sign(-3))
print()
print(abs_square(5))
print(abs_square(-3))
print()
print(square_joseon(25))
print(square_joseon(6))