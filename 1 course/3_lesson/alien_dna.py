def alien_dna(s1, s2):
    dna_2_base = set()
    for i in range(len(s2) - 1):
        dna_2_base.add(s2[i] + s2[i + 1])
    count = 0
    for i in range(len(s1) - 1):
        if s1[i] + s1[i + 1] in dna_2_base:
            count += 1
    return count

s1 = input()
s2 = input()
print(alien_dna(s1, s2))