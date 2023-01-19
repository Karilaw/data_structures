# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this

my_expenses_list = [2200, 2350, 2600, 2130, 2190]
print(my_expenses_list[1] - my_expenses_list[0])

first_quarter_expen = my_expenses_list[0:3]
print(sum(first_quarter_expen))


for expense in my_expenses_list:
    if expense == 2000:
        print('There 2000 is present ')
    else:
        print('There is no 2000')

june = 1980
my_expenses_list.append(june)
print(my_expenses_list)


my_april_expense = my_expenses_list[3] - 200
print(my_april_expense)
my_expenses_list.remove(2130)
my_expenses_list.insert(3, my_april_expense)
print(my_expenses_list)

# You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,

# 1. Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(len(heros))

heros.append('black panther')
print(heros)

heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)

my_exempt = ['thor', 'hulk']

heros[1:3] = ['doctor strange']
print(heros)

heros.sort()
print(heros)

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
max = int(input('Enter maxmum number'))
odd_number = []
for i in range(1, max):
    if i % 2 != 0:
        odd_number.append(i)
print(odd_number)
