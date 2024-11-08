from datetime import date
from functions import main
# datetime zit standaard in Python, maar moet opgeroepen worden. Import is het gene wat je nodig bent
# functions import main is een verwijzing naar de functie van een eigen python file. Waar main de eigen functie is, die in dit bestand wordt weergeven. 

main()

today = date.today()

print(today)

