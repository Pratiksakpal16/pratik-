try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a/b
    print("answer is",c)
except ValueError as v:
    print(v)

finally:
    print("Message")
