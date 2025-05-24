n = int(input("Enter how many numbers, you want to print: "))

a, b = 0, 1
count = 0

while count < n:
    if a <= 1:
        isPrime = False
    else:
        isPrime = True
        for i in range(2, a):
            if a % i == 0:
                isPrime = False
                break
        
    if isPrime:
        print(a, end = " ")
        count += 1

    a, b = b, a + b
