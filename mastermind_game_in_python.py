import random
# tries of first player
tries_1 = ''
# tries of player 2
tries_2 = ''
# it wil run two times for player 1 and player 2
for i in range(1, 3):
    num = random.randrange(1000, 10000)
    print('player', i, end='')
    print( ', set the number: ')
    num_str = str(num)
    num_len = len(num_str)
    num_l = list(num_str)
    trie = 0
    if i == 1:
        i_op = 2
    else:
        i_op = 1
    # for creating x strings of num_len
    win1 = ''
    for a in range(num_len):
        win1 += 'X'
    win_l = list(win1)
    print(win1)
    while win1 != num_str:
        ind = 0
        cor_dig = 0
        if i == 1:
            guess = int(input(print('guess number of lenth: ', num_len, '\nplayer 2, guess the number: ')))
        else:
            guess = int(input(print('guess number of lenth: ', num_len, '\nplayer 1, guess the number: ')))
        guess_str = str(guess)
        guess_len = len(guess_str)
        guess_lis = list(guess_str)
        if guess_len == num_len:
            trie = trie + 1
            for b in range(num_len):
                if guess_str[ind] == num_str[ind]:
                    cor_dig = cor_dig + 1
                    win_l[ind] = guess_str[ind]
                ind = ind + 1
            win1 = ''.join(win_l)
            if win1 == num_str:
                print('congratulation you win the game in: ', trie, 'tries')
                print(win1)
                if i == 1:
                    trie_str = str(trie)
                    tries_1 += trie_str
                else:
                    trie_str = str(trie)
                    tries_2 += trie_str
            else:
                win1 = ' '.join(win_l)
                print('you have guessed', cor_dig, 'correct! digits guessed more', num_len-cor_dig, 'digts to win')
                print(win1)
        else:
            print('your input len is wrong')
tries_1 = int(tries_1)
tries_2 = int(tries_2)
if tries_1 > tries_2:
    print('congratulation! player 2 become the mastermind')
elif tries_1 == tries_2:
    print('congratulation! you both are mastermind')
else:
    print('congratulation! player 1 become the mastermind')