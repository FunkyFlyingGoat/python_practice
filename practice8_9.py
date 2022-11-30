#创建一个列表把它传递给一个函数
def show_messages(messages):
    for message in messages:
        print (f'{message}')
messages = ['Holle world','I love jo']
show_messages(messages)

#编写两个函数
def show_messages(messages):
    for message in messages:
        print (f'{message}')

def send_messages(messages):
    for message in messages:
        sent_messages.append(message)
        print (message)
sent_messages=[]
messages = ['Holle world','I love jo']
send_messages(messages)
send_messages(messages)