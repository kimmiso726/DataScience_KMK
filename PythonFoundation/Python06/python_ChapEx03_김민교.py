'''
Q3. 홍길동 씨의 주민등록번호는 881120-1068234이다.

홍길동씨의 주민등록번호를 연월일(YYYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.

'''

pin = input("주민등록번호를 입력해주세요.(ex.881120-1068234) :  ")

yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
if int(pin[7]) == 1 or int(pin[7]) == 2:
	print("19%s년 %s월 %s일"%(pin[0:2], pin[2:4], pin[4:6]))
else:
	print("20%s년 %s월 %s일"%(pin[0:2], pin[2:4], pin[4:6]))

