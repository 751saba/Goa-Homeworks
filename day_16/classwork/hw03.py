# my_num ცვლადში 1-დან 10-მდე შემთხვევითი რიცხვი განსაზღვრეთ
import random

my_num = random.randint(1, 10)
attempts = 0

# მომხმარებლისგან რიცხვის მიღება და შედარება my_num-თან
while True:
    user_guess = int(input("5: "))
    attempts += 1
    
    if user_guess == my_num:
        print(f"5 {attempts} attempts!")
        break
    else:
        print("Try again!")
