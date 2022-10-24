# reading files r is read only,w is write,a
# read file
file=open("/home/sam/Python/basics/files/country_list.txt","r")
for item in file.readlines():
    print(item)
file.close
# write file
file=open("readme.txt","w")
file.write('this is new file')
file.close
# append file
file=open("readme.txt","a")
file.write('this is new line')
file.close