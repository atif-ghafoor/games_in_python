# function to print uderscore between last and first character of randow word
def dashes(ran):
    r = ran
    r_list = list(r)
    r_len = len(r)
    for i in range(1, r_len-1):
        r_list[i] = '_'
    r = ''.join(r_list)
    return r
# function to replace character
def rep(ran1, ran, alph):
    ran = list(ran)
    ran1 = list(ran1)
    occurence = ran.count(alph)
    for i in range(occurence):
        index1 = ran.index(alph)
        ran1[index1] = alph
        ran[index1] = ''
    r = ''.join(ran1)
    return r

import random
list_alph = ['a', 'b', "c", 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list_words = ['Arham','Zayan','Azlan','Ali','Saad','Adnan','Sahil','Fahad','Ayaz','Usman','Zaid','Taha','Maaz','Ahnaf','Salaar','Aliyar','Ayesha','Anabia','Arham','Ayan','Ayaan','Inaya','Sana','Fatima','Zayan','Aryan','Anas','Ayat','Aaira','Rehan','Zoya','Aiza','Zara','Huzaifa','Zain','Naira','Ayat','Aiza','Abeeha','Ali','Ayra','Aqsa','Saad','Adnan','Usman','Taha','Maaz']
# ran  = random.choice(list_words)
ran = 'ayaz'
underscores = dashes(ran)
len_u = len(ran) - 2
# index to replace '-' with alphbets
ind = 0
# tries
tr = 0

list_answers = []
for i in range(1, len(ran)-1):
    list_answers.append(ran[i])
for i in range(len(ran)):
    ran_alph = random.choice(list_alph)
    list_answers.append(ran_alph)
random.shuffle(list_answers)

# choice to guess a alphabet
print(list_answers)
# print uderscores b/w first and last character
print(underscores)

for i in range(len(ran)):
    alph = input('Guess a word :- ')
    tr = tr + 1
    for i in range(len_u):
        ind = ind + 1
        if alph == ran[ind]:
            underscores = rep(underscores, ran, alph)
            list_answers.remove(alph)
            break
    print(list_answers)
    print(underscores)
    if underscores[ind] == alph:
        print('ohh yah congratulation your guess is correct')
    else:
        print('ohh shit your guess is not correct')
    ind = 0
    if underscores == ran:
        print('congratulation you won the game in', tr, 'tries')
        break
if underscores == ran:
    print('congratulation you won the game in', tr, 'tries')
else:
    print('you lose the game! good luck for next time')