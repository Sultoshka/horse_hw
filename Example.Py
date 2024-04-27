Order = 'bigmac'
Order2 = 'cheese'
Order3 = 'carolina reaper'
print("Hi can i get a %s with extra %s and with a %s please!" %(Order, Order2, Order3))

food = ['bigmac ,cheese ,carolina reaper']
order = [i for i in food if i in food]
print(order)

numbers = [25,50,75]
Range = [i for i in range(1, 100) if i in numbers]
print(Range)

x = {'name':'pasha','job':'TGbot creator'}
print(x['name'])
print(x['job'])
data = {
'name': ['jordan', 'pavel'],
'age': (12, 21),
'job': 'programmers'
}
data.pop('name')
print(data)
data.popitem()
print(data)
data.clear()
print(data)


instructor = {'name':'jordan','age':21,'job':'programmer'}
print(instructor.values())
print(instructor.keys())
print(instructor.items())

if 21 in instructor.keys():
    print('да, есть')
else:
    print('Не понимаю о чем вы')

users = {}
users['name'] = 'jordan'

print(users)
print(users['name'])

my_dict = {'name': 'jordan'}
my_dict['name'] = 'pasha'
print(my_dict)

user = [
    'posts', 'likes', 'comments', 'followers','following', 'saves','stories'
    ]

user1 = {}.fromkeys(user,0)
print(user)

Instructor = dict(name ='jordan', age=21, job='programmer')

for i in Instructor.keys():
    print(i)

for e in Instructor.values():
    print(e)

for k, v in Instructor.items():
    print(k, v)

    all_products = {'весь склад': {}}
for i in all_products:
    admin = input("Что вы хотите сделать?")
    all_products.append = input('Какой именно продукт вы хотели добавить')

    if __name__ == '__main__':
        __name__ == "Hello, World"
print(__name__)

First_Name = 'Ross'
last_Name = 'Taylor'
print('Hello %s %s! You just delved into python'%(First_Name, last_Name))