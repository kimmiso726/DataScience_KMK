# 리스트에 포함된 요소 X의 개수 세기(count)
a = [1,2,3,1,1,2]
print(a.count(1))
print('-'*20)

'''
리스트 확장 extend
extend(X)에서 X에는 리스트만 올 수 있으며
원래의 a 리스트에 X리스트를 더한다.
'''

a = [1,2,3]
a.extend([4,5])
print(a)

# a.extend([4,5])는 =+랑 같음
# 파이썬은 모든 자료형을 객체로 본다. ??근데 객체가 뭐?