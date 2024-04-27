while true:

user1 = input["Выберите действия каменть, ножнецы, бумага"]
possible_variants = ('камень' , 'ножнецы' , 'бумага')
user2 = input[possible_variants]
print(f'/n you chose {user1} second player chose {user2}. \n')

if user1 == user2:
   print(f'both players selected {user1} its a tie')
elif user1 == 'камень':
   if user2 == 'ножнецы':
      print('user1, вы выйграли, user2, вы пройграли')
else:
      print('user1, вы пройграли, user2, вы выйграли')
elif user1 == 'камень':
if   user2 == 'бумага':
    print('user1, вы пройграли, user2, вы выйграли')
else:
    print('user1, вы выйграли, user2, вы выйграли')
elif user1 == 'камень':
if   user2 == 'камень':
    print('играйте заново')
else:
    print('ERROR')
elif user1 == 'ножнецы':
if user2 == 'камень':
    print('user1, вы пройграли, user2, вы выйграли')
else:
    print('user1, вы выйграли, user2, вы пройграли')
elif user1 == 'ножнецы':
if user2 == 'бумага':
      print('user1, вы выйграли, user2, вы пройграли')
else:
      print('user1, вы пройграли, user2, вы выйграли')
elif user1 == 'ножнецы':
if user2 == 'ножнецы':
     print('играйте заново')
  else:
    print('ERROR')
elif user1 == 'бумага':
if user2 == 'камень':
   print('user1, вы выйграли, user2, вы пройграли')
else:
    print('user1, вы пройграли, user2, вы выйграли')
    elif user1 == 'бумага':
if user2 == 'ножнецы':
   print('user1, вы пройграли, user2, вы выйграли')
else:
    print('user1, вы выйграли, user2, вы пройграли')
elif user1 == 'бумага':
if   user2 == 'бумага':
    print('играйте заново')
else:
    print('ERROR')
