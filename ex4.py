# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level = float(input("Pourcentage de batterie ? "))
distance = 0
if 50 < battery_level <= 100:
    battery_level = battery_level - 50
    distance = battery_level * 2 + 25*0.5 + 15 + 2.5*5 + 6*5
    print(f"{float(distance)} km")
elif 25 < battery_level <= 50:
    battery_level = battery_level - 25
    distance = battery_level * 0.5 + 15 + 2.5*5 + 6*5
    print(f"{float(distance)} km")
elif 10 < battery_level <= 25:
    battery_level = battery_level - 10
    distance = battery_level + 2.5*5 + 6*5
    print(f"{float(distance)} km")
elif 5 < battery_level <= 10:
    battery_level = battery_level - 5
    distance = battery_level * 0.5 + 6*5
    print(f"{float(distance)} km")
elif 0 < battery_level <= 5:
    battery_level = battery_level
    distance = battery_level * 6
    print(f"{float(distance)} km")
elif battery_level == 0:
    print("La batterie est vide") 