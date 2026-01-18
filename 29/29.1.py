def solution(target: int, array: list[int]):
	l: int = 0
	r: int = len(array)-1
	while l <= r:
		mid = (l + r ) // 2
		print(mid, l, r)
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			r = mid - 1
		else:
			l = mid + 1
	return -1

array_1 = [ -2, 0, 3, 4, 7, 9, 11]
print(solution(3, array_1))
print(solution(2, array_1))
	
