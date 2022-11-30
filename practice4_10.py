#使用切片输出部分内容
destinations = ['tokyo','Singapore','Turkey','Belgium','dunhuang']
print (f'The first three items in the list are:')
for destination in destinations[0:3]:
    print (destination)
for destination in destinations[1:4]:
    print (destination)
for destination in destinations[-3:]:
    print (destination)