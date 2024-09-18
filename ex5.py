#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ")
code_medals = input("Chaine représentant les médailles ? ")
code_medals = list(code_medals)
impression = False

for i in code_medals:
    if i != 'G':
        if i != 'S':
            if i != 'B':
                print("Veuillez entrer une chaîne valide.")
                impression = True
                break

if impression == False:
    nombre_Or = code_medals.count('G')
    nombre_Argent = code_medals.count('S')
    nombre_Bronze = code_medals.count('B')
    print(f"{country}:\n- {nombre_Or} OR\n- {nombre_Argent} Argent\n- {nombre_Bronze} Bronze")