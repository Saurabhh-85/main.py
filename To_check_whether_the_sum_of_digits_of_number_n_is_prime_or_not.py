n = int(input())
sum  = 0
isPrime = 1
while n != 0:
    rem = n % 10
    sum += rem
    n = n // 10
    if sum == 1:
        isPrime = 0
        break
for i in range(2, sum):
    if sum % i == 0:
        isPrime = 0
        break
    else:
        pass
if isPrime == 1:
    print("Prime.")
else:
    print("Not Prime.")
