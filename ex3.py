# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.

speed = float(input("Vitesse initiale (m/s): ")) 
angle = float(input("Angle de lancer (en degrés): "))
import math
g = 9.8
distance = ((speed ** 2) * math.sin(math.radians(2 * angle))) / g 
new_distance = round(distance, 2)
print(f"Distance parcourue: {new_distance}m")