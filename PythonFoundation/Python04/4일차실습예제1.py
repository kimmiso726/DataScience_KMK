'''
**소수 판별 프로그램 작성
소수 요약:
	1과 자기 자신만으로 나누어 떨어지는 1보다 큰 양의 정수.
	이를 테면 2,3,5,7,11,13,17,19,23,29,31... 등은 소수이다.

	조건]  사용자로부터 20이상의 수를 입력 받는다.
		- 이하인 경우: '숫자를 확인하세요'
		- 이상인 경우: 소수 판별 출력한다.

'''
dev = []

while True:
	sosu = int(input('20이상의 수를 입력하세요 [Exit: 0]'))
	if sosu >= 20:
		for i in range(2, sosu+1):
			for j in range(2, sosu +1):
				if i % j == 0:
					dev.append[i]
					if count(dev) == 1:
						print('소수 O')
					else:
						print('소수 X')
					continue	
	elif sosu == 0:
		break
	else :
		print("숫자를 확인하세요.")
