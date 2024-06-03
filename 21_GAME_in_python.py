order_list = [0]
multiple_of_4 = [4, 8, 12, 16, 20]
last_num = order_list[-1]
print('Player 2 is computer\nDo you want to start the game:(yes/no)')
yes_no = input()
if yes_no == 'yes':
    print('Enter \'f\' to take the first chance:\nEnter \'s\' to take the seconde chance:')
    first_second = input()
    if first_second == 'f':
        while last_num != 20:
            # user turn
            print('how many number do you want to enter')
            num = int(input())
            if num <= 3 and num > 0:
                last_num = order_list[-1]
                for i in range(num):
                    last_num = last_num + 1
                    print('your number :- ', last_num)
                    order_list.append(last_num)
                print('order of list after your turn is:\n', order_list)
                if last_num == 20:
                    print('congratulation! you win the game.')            
                    break
            else:
                print('your enter number is greater than \'3\' or less than eqaul to \'0\'')
            # computer turn
            last_num = order_list[-1]
            for i in range(3):
                last_num = last_num + 1
                print('computer number :- ', last_num)
                order_list.append(last_num)
                if last_num in multiple_of_4:
                    break
            if last_num == 20:
                print('Good luck! for next time, you lose the game.')
                break                
            print('order of list after computer turn is:\n', order_list)
    else:
        while last_num != 20:
            # computer turn
            last_num = order_list[-1]
            for i in range(3):
                last_num = last_num + 1
                order_list.append(last_num)
                if last_num in multiple_of_4:
                    break
            if last_num == 20:
                print('Good luck! for next time, you lose the game.')
                break                
            print('order of list after computer turn is:\n', order_list)
            # user turn
            print('how many number do you want to enter')
            num = int(input())
            if num <= 3 and num > 0:
                last_num = order_list[-1]
                for i in range(num):
                    last_num = last_num + 1
                    print('your number :- ', last_num)
                    order_list.append(last_num)
                print('order of list after your turn is:\n', order_list)
                if last_num == 20:
                    print('congratulation! you win the game.')            
                    break
            else:
                print('your enter number is greater than \'3\' or less than eqaul to \'0\'')
else:
    print('Quit')