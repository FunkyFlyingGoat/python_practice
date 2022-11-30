#数到20,使用for循环打印数1~20(含)
for value in range(1,21):
    print (value)
#创建一个1~1000000的列表,并复核最大最小以及总和
nume = list(range(1,1000001))
print(min(nume))
print(max(nume))
print(sum(nume))
#创建一个1~20的奇数列表
nume = list(range(1,20,2))
for value in nume:
    print (value)
#创建一个1~10的立方结果的列表
nume = [value**3 for value in range(1,11)]
for number in nume:
    print (number)