'''
Q1. 홍길동씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해보자.
과목  점수
국어  80
영어  75
수학  55
'''

Grade = [90, 75, 55]

Sum = 0

for i in range(len(Grade)):
	Sum = Sum + int(Grade[i])
print(f'홍길동씨의 평균 점수는 {Sum/len(Grade):2.2f}입니다.')