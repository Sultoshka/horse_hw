nums = (1,101)
m = [i for i in nums]
print(m)

name = 'BMW 7 SERIES'
n = [item for item in name]
print(n)

Name = 'MERCEDES S CLASS'
N = [x for x in Name]
print(N)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
newlist = [x if x != "banana" else "orange" for x in fruits]
print (newlist)


BMW_MODELS = ["1 series", '2 series', '3 series', '4 series', '5 series' , '6 series', '7 series']
order = [x for x in BMW_MODELS if '7 series' in BMW_MODELS]
order = [x if x != '7 series' else '8 series' for x in order]
order.append('M series')
print(order)

names = 'jordan'
i = [x for x in names]
print(i)

nums = [n for n in range(101)]
print(nums)




