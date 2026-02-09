def roof(n) -> int:
	if n == 1:
		return 1
	return 2 * roof(n-1) +1

def solution(n: int) -> int:
	memo = dict()
	def roof(n):
			if n == 1:
				return 1
			elif n in memo:
				return memo[n]
			else:
				value: int = 2 * roof(n-1) + 1
				memo[n] = value
				return value
	def helper(n):
		if n == 0:
			return 0
		if n ==1:
			return 1
		return 2 * solution(n-1) + roof(n)
	return helper(n)

for i in range(5):
	print(solution(i))