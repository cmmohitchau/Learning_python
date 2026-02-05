def sum_of_digits(n):
    digits = 0
    while n > 0:
        last_digit = n % 10
        digits += last_digit
        n = int(n/10)
    
    return digits

def max_of_three_nums(a):
    a.sort()
    return a[2]

n = int(input("Enter digits"))
a = []
for i in range(n):
    a.append(int(input("Enter num : ")))

print("max of nums : " , max_of_three_nums(a))