num = int(input("Enter a number "))
n = num
total = 0
while n != 0:
    r = n % 10
    total = total * 10 + r
    n = n // 10

print(total)
if total == num:
    print("Palindrome")
else:
    print("not palindrome")
