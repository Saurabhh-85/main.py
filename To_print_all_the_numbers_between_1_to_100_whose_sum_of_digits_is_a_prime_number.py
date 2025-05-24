 for i in range(1, 101):
 sum_of_digits = 0
 number = i
 # Calculate the sum of digits of the number i
 while number != 0:
    sum_of_digits += number % 10
    number = number // 10
    
 # Check if the sum of digits is prime
 if sum_of_digits > 1:
    is_prime = True
    for j in range(2, int(sum_of_digits ** 0.5) + 1):  # Check divisibility up to the square root of sum_of_digits
        if sum_of_digits % j == 0:
            is_prime = False
            break
        
 # If the sum of digits is prime, print the number i
    if is_prime:
        print(i)
