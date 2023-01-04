def fbi():
    num1, num2 = 1, 1
    while True:
        num3 = num1 + num2
        yield num3
        num1, num2 = num2, num3

result = fbi()
for i in range(20):
    print(next(result))
