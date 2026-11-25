s1 = int(input())
s2 = int(input())
s3 = int(input())
if s1 + s2 <= s3 or s1 + s3 <= s2 or s2 + s3 <= s1:
    print("not a triangle")
elif s1 == s2 == s3:
    print("equilateral")
elif s1 == s2 or s1 == s3 or s2 == s3:
    print("isocles")
else:
    print("scalene")