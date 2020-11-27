def get_cost(t: int) -> int:
	total_cost = 0
	for i, ai in enumerate(a):
		cost = abs(ai - t)
		cost -= 1 if cost else 0
		total_cost += cost
	return total_cost

n = int(input())
a = list(map(int, input().split()))

a.sort()
min_cost = -1
t = a[0]

for tmp_t in range(a[0], a[-1]+1):
	tmp_cost = get_cost(tmp_t)
	if tmp_cost < min_cost or min_cost == -1:
		min_cost = tmp_cost
		t = tmp_t
	 
print(f'{t} {min_cost}')

