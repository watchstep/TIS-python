import sys; input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

def recurr(t):
	if t == S:
		print(1)
		sys.exit()
	if not t:
		return 0
	if t[-1] == 'A':
		recurr(t[:-1])
	if t[0] == 'B':
		recurr(t[1:][::-1])

recurr(T)
print(0)