#
# bucket2.py - bucket list builder
#
print('\nBUCKET LIST BUILDER\n')

bucket = []

choice = input('Enter selection: e(X)it, (A)dd, (L)ist, (D)elete...')
choice = choice.upper()
while choice[0] != 'X':
    if choice[0] == 'A':
        print('Enter list item...')
        newitem = input()
        bucket.append(newitem)
    elif choice[0] == 'L':
        for item in bucket:
            print(' ','-',item)
    elif choice[0] == 'D':
        for index in range (len(bucket)):
            print(' ',index,'-', bucket[index])
        delitem = input('Please select item you want to delete: ')
        del bucket[int(delitem)]
    else:
         print('Invalid selection.')
    choice = input('Enter selection: e(X)it, (A)dd, (L)ist, (D)elete..').upper()

print('\nGOOGBYE!\n')



