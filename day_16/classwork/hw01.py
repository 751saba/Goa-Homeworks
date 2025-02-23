# სწორ პაროლზე სამუშაო ცვლადი
correct_password = "my_secure_password"

# ცვლადი შესატყვისი პაროლის შეყვანის რაოდენობისთვის
counter = 0

# while ციკლი სანამ მომხმარებლის პაროლი არ დაემთხვევა სწორს
while True:
    user_password = input("გთხოვთ, შეიტანეთ პაროლი: ")
    counter += 1  # ყოველი შეყვანის შემდეგ ხორციელდება კალკულაცია
    
    if user_password == correct_password:
        print("access granted")
        print(f"პაროლი შესული იყო {counter} ჯერ.")
        break  # პაროლის სწორი შეყვანის შემდეგ ციკლი შეჩერდება
