#以特殊方式跟管理员打招呼
from hashlib import new


user_names = ['admin','yangyang','zhouying','coco','jiaotang']
for user_name in user_names:
    if user_name == 'admin':
        print (f"Hello {user_name}, would you like tu see a status report?")
    else:
        print (f"Hello {user_name},thank you for logging in again.")

#处理没有用户的情况
user_names = []
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print (f"Hello {user_name}, would you like tu see a status report?")
        else:
            print (f"Hello {user_name},thank you for logging in again.")
else:
    print ('We need to find some users!')

#检查用户名
current_users = ['Admin','yangyang','zhouying','coco','jiaotang']
new_users = ['admin','yangyang','zaotang','tubin','xiaoxiaoka']
current_users_lower = []
for user_name in current_users:
    current_users_lower.append(user_name.lower())
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print (f"This user name: {new_user} have been used,try another one ")
    else:
        print (f"This user name: {new_user} have not been used")

#序数
numbers = list(range(1,10))
for number in numbers:
    if number == numbers[0]:
        print (f"This number:{number} is the 1st number in the list")
    elif number == numbers[1]:
        print (f"This number:{number} is the 2nd number in the list")
    elif number == numbers[2]:
        print (f"This number:{number} is the 3rd number in the list")
    elif number == numbers[3]:
        print (f"This number:{number} is the 4th number in the list")   
    elif number == numbers[4]:
        print (f"This number:{number} is the 5th number in the list") 
    elif number == numbers[5]:
        print (f"This number:{number} is the 6th number in the list") 
    elif number == numbers[6]:
        print (f"This number:{number} is the 7th number in the list") 
    elif number == numbers[7]:
        print (f"This number:{number} is the 8th number in the list") 
    elif number == numbers[8]:
        print (f"This number:{number} is the 9th number in the list") 