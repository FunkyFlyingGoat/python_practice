#用变量表示人名,并输出一段话
name = "yangyang"
message = f"Hello {name},would you like to learn some Python today?"
print (message)

#将人名大小写调整后,再次输出一段话
message = f"Hello {name.title()},would you like to learn some Python today?"
print (message)

#将人名赋予一个变量,他说的话赋予一个变量,并输出一段话
name = "albert einstein"
message = "A person who never made a mmistake never tride anything new"
print (f"{name.title()} noce said,'{message}'")

#将print 简化成print (message)
message = f"{name.title()} noce said,'A person who never made a mmistake never tride anything new'"
print (message)