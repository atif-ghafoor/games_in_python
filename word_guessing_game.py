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
def rep(ran, ind, alph):
    list_r = list(ran)
    list_r[ind] = alph
    r = ''.join(list_r)
    return r
import random
list_words = ['Arham','Zayan','Azlan','Ali','Saad','Adnan','Sahil','Fahad','Ayaz','Usman','Zaid','Taha','Maaz','Ahnaf','Salaar','Aliyar','Ayesha','Anabia','Arham','Ayan','Ayaan','Inaya','Sana','Fatima','Zayan','Aryan','Anas','Ayat','Aaira','Rehan','Zoya','Aiza','Zara','Huzaifa','Zain','Naira','Ayat','Aiza','Abeeha','Ali','Ayra','Aqsa','Saad','Adnan','Usman','Taha','Maaz']
ran  = random.choice(list_words)
# print uderscores b/w first and last character
underscores = dashes(ran)
print(underscores)
len_u = len(ran) - 2
# index to replace '-' with alphbets
ind = 0
# tries
tr = 0
while underscores != ran:
    alph = input('Guess a word')
    tr = tr + 1
    for i in range(len_u):
        ind = ind + 1
        if alph == ran[ind]:
            underscores = rep(underscores, ind, alph)
            break
    print(underscores)
    if underscores[ind] == alph:
        print('ohh yah congratulation your guess is correct')
    else:
        print('ohh shit your guess is not correct')
    ind = 0
tr = tr - len_u
print('congratulation you won the game in', tr, 'tries')