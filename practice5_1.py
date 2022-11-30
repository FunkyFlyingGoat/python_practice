from ctypes import alignment


car = 'subaru'
print ("Is car == 'subaru'? I predict True.")
print (car == 'subaru')

print ("\nIs car == 'audi'? I predict True")
print (car == 'audi')

#外星人颜色
alien_color = 'green'
if alien_color == 'green':
    print ("got 5 point")
else:
    print ('')

#外星人2
alien_color = 'green'
if alien_color == 'green':
    print ("got 5 point")
else:
    print ('got 10 point')

#外星人3
alien_color = 'green'
if alien_color == 'green':
    print ("got 5 point")
elif alien_color == 'yellow':
    print ("got 10 point")
else:
    print ('got 15 point')