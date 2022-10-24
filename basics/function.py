# python is intendication language
# one intendation equals to 4 spaces
# def keyword is used to define function:


def set_name():
    name=input("Set your name\n")
    print(name)

#setting undefined length argument
def name_list(*names):
    print(names) 

def sum(one,two):
    return(one+two)

set_name()
name_list("umais",12,15)
print(sum(2,3))