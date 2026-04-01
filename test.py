from gpiozero import Button
from time import sleep

# On force le pull_down car ton bouton est au 3.3V
bouton = Button(26, pull_up=False)

print("Test de lecture du bouton (Ctrl+C pour quitter)")
print("Le bouton doit afficher 0 au repos et 1 quand on appuie.")

try:
    while True:
        print(f"État du bouton : {bouton.value}", end="\r")
        sleep(0.1)
except KeyboardInterrupt:
    print("\nTest arrêté.")
