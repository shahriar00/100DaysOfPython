
sumation = 0
number = int(input("Enter any number:"))
for x in range(1,11):
    sum = number*x
    print(number,"X",x ," = ",sum)

while number<10:
    sumation = sumation+number
    number = number+1
print(sumation)

