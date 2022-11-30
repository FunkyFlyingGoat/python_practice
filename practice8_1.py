#编写一个函数来输出在第八章学的是什么
def display_message():
    print ("这章学怎么编写函数和储存运用函数")
display_message()

#编写一个含形参的函数
def favorite_book(title):
    print (f"One of my favorite books is {title.title()}")
favorite_book('alice in wonderland')

#编写一个T恤的函数
def make_shirt(size,logo):
    print (f"The shirt's size is {size},zhe logo of shirt is {logo}")
make_shirt('m','I love jo')

#编写一个含有默认值的T恤的函数
def make_shirt(size='L',logo='I LOVE PYTHON'):
    print (f"The shirt's size is {size},zhe logo of shirt is {logo}")
make_shirt()
make_shirt(size='M')
make_shirt('M','holle world')