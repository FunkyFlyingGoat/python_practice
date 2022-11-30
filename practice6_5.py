#遍历字典
rivers = {
    'nile':'egypt',
    'Yellow River':'china',
    'Yalu River':'North Korea',
    }
for river,country in rivers.items():
    print (f"The {river} runs through {country}")
for river in rivers.keys():
    print (river)
for river in sorted(rivers.values()):
    print (river)

#字典嵌套列表
people = []
yangyang = {
    'first_name':'yang',
    'last_name':'yang',
    'age':'32',
    'city':'hangzhou',
    }
zhouying ={
    'first_name':'ying',
    'last_name':'zhou',
    'age':'32',
    'city':'hangzhou',
    }
people.append(yangyang)
people.append(zhouying)
for a in people:
    print (a)