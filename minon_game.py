def minion_game(string):
    vowels = 'AEIOU'
    stuart_score = 0
    kevin_score = 0
    length = len(string)
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i
    if stuart_score > kevin_score:
        print('Stuart', stuart_score)
    elif stuart_score == kevin_score:
        print('Draw')
    else:
        print('Kevin', kevin_score)
if __name__ == '__main__':
    s = input()
    minion_game(s)