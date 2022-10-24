countries=['pakistan','united states',"KSA","Algeria",'brazil']
# printing all countries
print(countries)
# getting index 1
print(countries[1]+'\n')
# getting index 1 and letter index 0
print(countries[1][0]+'\n')
# printing specifc range 
print(countries[1:])
# printing specifc range between
print(countries[1:2])
# get variable type
print(type(countries))
print(type(countries[1]))
# length of list
print(len(countries))
# list intialization alternative
cat=list(("apple","banana",'orange'))
print(cat)
# join two lists
countries.extend(cat)
print(countries)
# adding item to list
cat.append("mangoe")
# specific index insertion
cat.insert(1,"cherry")
print(cat)

# remove particular value
cat.remove("cherry")
print(cat)
# get index number of item
print(cat.index("apple"))
print(cat)
# count specific value
cat.count("apple")
# delete list
cat.clear
print(cat)
# sort list
listOfNumber=[3,2,45,21,23]
listOfNumber.sort()
# remove item
listOfNumber.pop(1)
del listOfNumber[0]
print(listOfNumber)
