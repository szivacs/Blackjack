import array
from random import randint

playerPoint = 0
lap = int(input("Hány kört szeretnél játszani? "))

for i in range(lap):
    playerCards = 0
    # hátralévő kártyák
    Cards = array.array('b', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    # Első két kártya
    for i in range(2):
        newCard = Cards[randint(0, (len(Cards)-1))]
        playerCards += newCard
        Cards.remove(newCard)

    print(f"Jelenlegi állásod: {playerCards}\n")
    Question = input("Megszeretnél állni? I/N")

    # játék folytatás
    while Question == "N" or Question == "n":
        newCard = Cards[randint(0, (len(Cards)-1))]
        playerCards += newCard

        print(f"Kapott kártya: {newCard}, összesen: {playerCards}\n")

        # Blackjack
        if playerCards == 21:
            playerPoint += 3
            print(f"Gratulálok! +3 pont. Jelenlegi pontszámod: {playerPoint}\n")
            break

        # túlment
        elif playerCards > 21:
            playerPoint -= 1
            print(f"Besokaltál. -1 pont. Jelenlegi pontszámod: {playerPoint}\n")
            break

        Cards.remove(newCard)
        Question = input("Megszeretnél állni? I/N")


    if Question != "n":
        if playerCards <= 20 and playerCards >= 17:
            playerPoint += 1
        else:
            playerPoint -= 1
        print("Megálltál.", "+1 pont." if playerCards <= 20 and playerCards >= 17 else "-1 pont.", f"Jelenlegi pontszámod: {playerPoint}\n")


    print("Vége a körnek." if i < (lap-1) else "")
    
print(f"Vége a játéknak.\nVégső pontszámod: {playerPoint}")
