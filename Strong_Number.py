Number = int(input())
Sum = 0
Temp = Number

while(Temp > 0):
    Factorial = 1
    i = 1
    Reminder = Temp % 10

    while(i <= Reminder):
        Factorial = Factorial * i
        i = i + 1


    Sum = Sum + Factorial
    Temp = Temp // 10
if (Sum == Number):
    print("The number %d is a strong number" %Number)
else:
    print("The number %d is not a strong number" %Number)