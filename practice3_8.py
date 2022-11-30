#列出5个想去旅游的地方
destinations = ['tokyo','Singapore','Turkey','Belgium','dunhuang']
#打印原始排列顺序的列表
print (destinations)
#使用sorted按字母顺序打印列表,由于大小写不一致,优先调整大小写后排序
destination_title = []
for destination in destinations:
    destination_title.append(destination.title())
print (sorted(destination_title))
#再次打印列表,已证明列表未被永久修改
print (destination_title)
#使用sorted按字母反序打印列表
print (sorted(destination_title,reverse=True))
#再次打印列表,已证明列表未被永久修改
print(destination_title)
#使用reverse修改列表排序
destination_title.reverse()
print (destination_title)
#再次使用reverse还原列表,并复核
destination_title.reverse()
print(destination_title)