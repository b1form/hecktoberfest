# list of numbers to search from
lst=[4,5,3,2,1,2,3,4]

# number to check in list
check= 1

for i in lst:
    if i== check:
        print("Found!!")
        exit()
print("Not Found!!")