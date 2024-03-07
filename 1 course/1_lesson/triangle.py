l = sorted(map(int,[input() for _ in range(3)]))
print("YES" if ((l[0]**2 + l[1]**2) >= l[2]**2) else "NO")