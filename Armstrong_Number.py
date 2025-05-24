 n = int(input())
 s = str(n)
 sum = 0
 length = len(s)
 for i in s:
     sum += int(i)**length
 if sum == n:
     print(n, "is an Armstrong number.")
 else:
     print(n, "isn't an Armstrong number.")
