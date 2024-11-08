# write the divide() function
# Devide functie moet bovenaan. Van boven naar beneden. 
def divide(getal1, getal2):
    uitkomst = getal1//getal2
    restwaarde = getal1%getal2
    print(getal1,'divided by', getal2, 'equals', uitkomst, 'with a remainder of', restwaarde)


def main():
    divide(5, 2)
    divide(6, 3)
    divide(12, 5)
    divide(1, 2)



main()