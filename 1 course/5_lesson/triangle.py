n = int(input())
p = [] 
n = int(input())
for i in range(n):
    m, k = map(int, input().split())
    p.append((m, k))

ans = 0
for i in range(n):
	used_vec = set()
	neig = []
	for j in range(n):
		vec_x = p[i][0] - p[j][0]
		vec_y = p[i][1] - p[j][1]
		len_vec = vec_x ** 2 + vec_y ** 2
		neig.append(len_vec)
		if (vec_x, vec_y) in used_vec:
			ans -= 1
		used_vec.add((-vec_x, -vec_y))

	neig.sort()
	r = 0
	for l in range(len(neig)):
		while r < len(neig) and neig[l] == neig[r]:
			r += 1
		ans += r - l - 1

print(ans)