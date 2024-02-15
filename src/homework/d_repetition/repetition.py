def get_factorial(num):
    factorial = num
    
    for i in range(num - 1):
        factorial = factorial * (i + 1)

    return factorial

def sum_odd_numbers(num):
    i = 0
    oddSum = 0

    while (i <= num):
        if i % 2 != 0:
            oddSum += i
        
        i += 1
    
    return oddSum