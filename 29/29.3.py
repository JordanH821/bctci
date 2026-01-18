def solution(array: list[int]) -> int:
	l = 0
	r = len(array)-1
	if len(array) == 2:
		return min(array[l], array[r])
	elif array[l] > array[r]:
		return array[r]
	while r-l > 1:
		mid = (l + r) // 2
		if array[mid] <= array[0]:
			l = mid
		else:
			r = mid
	return array[l] 

print(solution([6,5,4,7,9])) # 4
print(solution([5,6,7])) # 5
print(solution([7,6,5])) # 5
print(solution([5,6])) # 5
print(solution([3,2,4])) # 2
print(solution([6,5])) # 5
