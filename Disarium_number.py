Number = int(input())
length = len(str(Number))

Temp = Number
Sum = 0
rem = 0

while Temp > 0:
    rem = Temp % 10
    Sum = Sum + int(rem**length)
    Temp = Temp // 10
    length = length - 1


if Sum == Number:
    print("True")
else:
    print("False")