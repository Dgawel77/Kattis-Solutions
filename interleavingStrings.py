def aux(s1, s2, s3):
    if len(s1) == 0:
        return True if s2 == s3 else False
    if len(s2) == 0:
        return True if s1 == s3 else False
    if s1[0] == s3[0] and s2[0] != s3[0]:
        return aux(s1[1:], s2, s3[1:])
    if s1[0] != s3[0] and s2[0] == s3[0]:
        return aux(s1, s2[1:], s3[1:])
    if s1[0] == s3[0] and s2[0] == s3[0]:
        return aux(s1, s2[1:], s3[1:]) or aux(s1[1:], s2, s3[1:])
    if s1[0] != s3[0] and s2[0] != s3[0]:
        return False

print(aux("aabcc", "dbbca", "aadbbcbcac"))