#创建一个包含姓名的列表,并打印一条消息来邀请其中的人共进晚餐
name_list = ['zhouying','jiaotang','tubing','coco']
message = f'Holle {name_list[0].title()},would you like to have a dinner with me ?'
print (message)

#遍历后向每个人发送邀请信息
for name in name_list:
    message = f'Holle {name.title()},would you like to have a dinner with me ?'
    print (message)

#表达名单中谁无法参加,并用新加入的姓名进行替换
name_list = ['zhouying','jiaotang','tubing','coco']
print ("I've invited 3 peple:")
for name in name_list:
     print (f"{name}")
print (f"But {name_list[3]} will be missing")
name_list[3] = 'zaotang'
print (name_list)
print (f'there are {len(name_list)} guests,will be here')