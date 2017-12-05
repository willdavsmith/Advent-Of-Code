def straightdownsteps (n):
	total = 0
	while (n != 0):
		total = total + ((8 * n) - 1)
		n = n - 1
	return((1 + total))
print(straightdownsteps(1))
def steps (n):
	x = 0
	while (n > 1):
		n = n - straightdownsteps(x + 1)
		x = x + 1
	print(x)

steps(26)