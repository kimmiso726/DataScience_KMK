# split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 
#공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다.
a = 'asdf adfd asef'
print(a.split())

# b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 
#괄호 안의 값을 구분자로 해서 문자열을 나누어 준다.
b = 'asdf-adfd-asef'
print(b.split('-'))



