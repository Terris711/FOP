#
# comprehension.py - Question 3c
#


# Question 3c - i
numlist = [25,106,170,79,135,101,85,91]
num = 0
newlist = []

for i in range(len(numlist)):
    if numlist[i] > 100:
        num = numlist[i]
        newlist.append(num)

print(newlist)


# Question 3c - iii
wordlist = ["Papaya", "guava", "Mango", "Grapes"] 
g_list = []
g_word = 0

for i in range(len(wordlist)):
    if wordlist[i][0] == "G" or wordlist[i][0] == "g":
        g_word = wordlist[i]
        g_list.append(g_word)

print(g_list)

