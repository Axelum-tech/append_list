user={
    'username': 'johny777',
    'online': True,
    'email': 'johny777@lucky.me',
    'rating': int(input("How many like do you have?")) ,
    'friends':[
        'Marry888',
        'Bob555', 
        'Vera111',]
        
}


print(user['username'])
print(user['email'])





if user['rating']>=1 and user['rating']<=999:
    print(user["rating"])
elif user['rating']>=1000 and user['rating']<=999999:
    print(round(user['rating']/1000),"K Likes")
elif user['rating']>=1000000 and user['rating']<=999999999:
    print(round(user['rating']/1000000),"M Likes")
elif user['rating']>=1000000000 and user['rating']<=10000000000:
    print(round(user['rating']/10000000),"T Likes")


user['friends'].append(input("Add a friend:"))

for i in range(len(user['friends'])):
    print(user['friends'])

