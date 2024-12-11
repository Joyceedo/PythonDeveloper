import random

def main():
    # Kies steen, papier, schaar
    choice_user = int(input('geef een nummer van 1 tot en met 3 (steen (1), papier (2), schaar (3))'))
    choice = ['steen', 'papier', 'schaar']

    # Maak een keuze
    keuze_gebruiker_element = choice[choice_user-1]
    print('User:', keuze_gebruiker_element)

    # De keuze van de computer
    computer_choice_element = random.choice(choice)
    print('computer', computer_choice_element)

    # De winnaar bepalen 
    if keuze_gebruiker_element == computer_choice_element:
        print('Het is een gelijkspel!')

    elif (keuze_gebruiker_element == 'steen' and computer_choice_element == 'schaar') or \
        (keuze_gebruiker_element == 'papier' and computer_choice_element == 'steen') or \
        (keuze_gebruiker_element == 'schaar' and computer_choice_element == 'paier'):
        print('Je hebt gewonnen!')

    else:
        print('De computer heeft gewonnen!')

main()