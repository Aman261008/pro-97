from operator import countOf


number=5
guess=(1,2,3,4,5,6,7,8,9)
chances=5

while chances < 5:
    if guess == number:
        print("congratulation you won!!!")
        break
    if not chances < 5:
        print("you lose the numer is number",number)


