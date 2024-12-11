import random

def remove_random(the_list):
    x = random.choice(the_list)
    the_list.remove(x)
    return x

# De functie remove_random(the_list):
# Deze functie neemt een lijst (the_list) als parameter.
# Het kiest een willekeurig element uit de lijst met de functie random.choice(the_list).
# Vervolgens wordt dat willekeurige element verwijderd uit de lijst met the_list.remove(x).
# Ten slotte wordt het verwijderde element teruggegeven.


def main():
    colors = ['red', 'blue', 'green', 'orange']
    removed_color = remove_random(colors)
    print(f'The removed color was {removed_color}.')
    print(f'The remaining colors are {colors}')

# De main() functie:
# In de main() functie wordt een lijst genaamd colors gedefinieerd, die vier kleuren bevat: ['red', 'blue', 'green', 'orange'].
# De functie remove_random(colors) wordt aangeroepen, wat een willekeurige kleur uit de lijst verwijdert.
# Het resultaat (de verwijderde kleur) wordt opgeslagen in de variabele removed_color.
# Vervolgens wordt de verwijderde kleur en de resterende lijst van kleuren afgedrukt met print().

main()