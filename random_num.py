from random import randint
guess_num = randint(1,100)
user_input = -1
trial_period = 1
while guess_num != user_input :
    print("The Trial No %d" %trial_period,end='')
    user_input= int(input())
    if user_input <guess_num:
        print("The input number is less")
    elif user_input > guess_num:
        print("The input number is Much")
    else:
        print("Kudos! The right guess")
trial_period +=1
