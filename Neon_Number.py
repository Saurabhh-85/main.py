n = int(input())
square = n * n
digit_sum = 0

while square > 0:
    digit_sum += square % 10
    square = square // 10


if digit_sum == n:
    print(n, "is a Neon number.")
else:
    print(n, "isn't a Neon number.")
