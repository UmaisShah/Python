# if else & if elseif else
from list import countries

a=1
b=3
if a>b:
    print(str(a)+"is greater"+str(b));
elif a==1:
    print(a)
else:
    print(str(b)+"is greater"+str(a));

# while loops
i=1
# while i<10 or i==10:
while i<5 and i==10:

    i+=1
    print('values is:'+str(i))

# For loops for words
for letter in 'Monday':
    print(letter)
# iterating list
for obj in countries:
    if(obj=="pakistan"):
        print(obj)
        break
# printing range values
for value in range(4,7):
    print(value)
#else with for loop 
else:
    print('looping terminated')


# nested loops with 2d list
my_list=[
    [1,2,4],
    [12,13,14],
    [21,22,24]
]
for item in my_list:
    for row in item:
        print(row)