num = input()
sum = 0
prod = 1
for i in num:
    sum += int(i)
    prod *= int(i)
if sum == prod:
    print(num, "is a spy number.")
else:
    print(num, "isn't a spy number.")
