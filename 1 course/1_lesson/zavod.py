def zavod(n, k, m):
    k_count = 0
    m_count = 0
    
    while  n >= k and n >= m and k >= m:
        k_count = n // k
        n = n % k + (k % m) * k_count
        m_count += (k // m ) * k_count
    return m_count
    
n, k, m = map(int, input().split())
print(zavod(n, k, m))