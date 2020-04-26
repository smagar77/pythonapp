#from tasks import *
#rev = reverse.delay('sachin')
#print(rev.status)
import time

from fcelery import add_user
for i in range(1, 100):
    time.sleep(5)
    data = {
        'username' : 'user'+str(i),
        'password' : 'user14'+str(i),
        'first_name' : 'user14Fname'+str(i),
        'last_name' : 'user14Lname'+str(i),
        'email' : 'user14@yopmail.com'+str(i)
    }
    res = add_user.delay(**data)
    print(res.status)