import random
print("Zagrajmy w papier kamien nozyce!")

options = ["Papier", "Kamien", "Nozyce"]
user_choice = input("Wybierz Papier, Kamien albo Nozyce :")
computer_choice = random.choice(options)
print ("Wybrales/as :", user_choice)
print ("Ja wybralem :", computer_choice)

if user_choice == computer_choice: 
    print("Zremisowalismy!")

elif user_choice == "Kamien" and computer_choice == "Nozyce":
    print("Wygrales/as!")
elif user_choice == "Papier" and computer_choice == "Kamien":
    print("Wygrales/as!")
elif user_choice == "Nozyce" and computer_choice == "Papier":
    print("Wygrales/as!")
else:
    print("Przegrales/as!")