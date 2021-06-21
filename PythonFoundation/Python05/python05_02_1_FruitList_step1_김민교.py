
A = 0
M = 0
S = 0
G = 0

Fruit = []

while True:
	num = int(input("10이상의 수를 입력하세요.[exit: 0 ] >>>>"))
	if num >= 10:
		for i in range(1, num+1):
			if i %3 == 0:
				print("%-2d.  [Apple]"%i)
				Fruit.append("Apple")
				A = A + 1
			if i % 8 == 0:
				print("%-2d.  [StrawBarry]"%i)
				Fruit.append("StrawBerry")
				S = S + 1
			if i % 4 == 0:
				print("%-2d.  [Melon]"%i)
				Fruit.append("Melon")
				M = M + 1
			if i % 5 == 0:
				print("%-2d.  [Grape]"%i)
				Fruit.append("Grape")
				G = G + 1
			else:
				print("%-2d.  -"%i)
			print(Fruit)
			Fruit = []

		print("="*1, "<< Fruit Count List >>", "="*2)
		print("%-10s"%"Apple", ' : ', "%10d회"%A)
		print("%-10s"%"Melon", ' : ', "%10d회"%M)
		print("%-10s"%"Grape", ' : ', "%10d회"%G)
		print("%-10s"%"StrawBerry", ' : ', "%10d회"%S)
		print('='*27)
		break

	elif num == 0:
		print('종료!!')
		break

	else:
		print("^10이상의 숫자를 확인하세요.")
		continue