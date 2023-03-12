file = open('demo.txt','r')
print(file.read())
print(file.readline())

file1 = open('demo.txt','a')
file1.write('This is me sazid')
print(file.read())