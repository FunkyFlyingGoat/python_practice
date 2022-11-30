#用字典来储存信息
yangyang = {
    'first_name':'yang',
    'last_name':'yang',
    'age':'32',
    'city':'hangzhou',
    }
print (yangyang['first_name'])
print (yangyang['last_name'])
print (yangyang['age'])
print (yangyang['city'])

#不同人喜欢不同的数字
favourite_numbers = {
    'jo':'13',
    'yangyang':'7',
    'coco':'26',
    'jiaotang':'22',
    'tubing':'16',
    }
for name,number in favourite_numbers.items():
    print (f"{name}'s favourite number is {number}")