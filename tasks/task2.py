num = int(input("Enter a number "))
diff = 17 - num
if diff > 0:
    print(diff)
else:
    print(-2 * diff)


fp = open("hello.txt", "w")
try:
    fp.write("Hello World")
except:
    print("Sth Went Wrong")
finally:
    fp.close()
