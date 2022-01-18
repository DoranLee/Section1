'''
    변수 이름을 짓는 규칙(naming rule)
        1. 알파벳, _ , 숫자
        2. 대소문자 구분
        3. 변수명은 중복 X
        4. 변수명은 첫글자로 숫자를 사용할 수 X
        5. 키워드와 동일하면 안됨
        6. 한글 등 기타 언어는 비추

    데이터 타입
        숫자, 문자열(텍스트), 논리값, 빈데이터
'''
text = 'Hello World'
num = 10
bool = False
obj = None
pi = 3.141592

print(type(text))  # str : 문자열 (string)
print(type(num))   # int : 정수 (intager)
print(type(bool))  # bool : 논리값 (boolean)
print(type(obj))   # NoneType : 빈 값
print(type(pi))    # float : 실수

