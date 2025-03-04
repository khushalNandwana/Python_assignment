import random
print("this is the program of guessing the number from 1 to 100")
lower_bound=1
upper_bound=100
total_chances=10
chance_counter=0
guess_num=random.randint(lower_bound,upper_bound)
while chance_counter < total_chances:
    chance_counter+=1
    my_num=int(input("Enter the number guess number"))
    if my_num==guess_num:
        print("the number is correct")
        break
    elif chance_counter>=total_chances and my_num!=guess_num:
        print("the number is not correct and no more chances is left")
    elif my_num > guess_num:
        print("number is too high")
    elif my_num < guess_num:
        print("number is too low")