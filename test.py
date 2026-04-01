from gpiozero import RGBLED, LED, Button
from signal import pause
from time import sleep

# 1. Configuration des LEDs Vertes
# Liste de tes GPIO : 2, 3, 4, 17
leds_vertes = [LED(27), LED(17), LED(3), LED(2)]

# 2. Configuration de la LED RGB (Anode Commune)
# Ordre : R=16, G=20, B=21 | active_high=False pour l'Anode Commune
rgb = RGBLED(red=16, green=20, blue=21, active_high=False)

# 3. Configuration du Bouton
# GPIO 26, relié au GND (Pull-up interne par défaut)
bouton = Button(13, pull_up=False)

def test_initial():
    print("--- Lancement du test matériel ---")

    # Test des LEDs vertes une par une
    print("Test LEDs vertes...")
    for i, l in enumerate(leds_vertes):
        print(f"  LED verte {i+1} allumée")
        l.on()
        sleep(0.3)
        l.off()

    # Test de la LED RGB
    print("Test LED RGB...")
    print("  Rouge")
    rgb.color = (1, 0, 0)
    sleep(0.5)
    print("  Vert")
    rgb.color = (0, 1, 0)
    sleep(0.5)
    print("  Bleu")
    rgb.color = (0, 0, 1)
    sleep(0.5)
    rgb.off()
    print("--- Test terminé ! Appuie sur le bouton pour la séquence ---")

def sequence_bouton():
    print("Bouton pressé ! Flash général !")
    # Allume tout en blanc / vert
    rgb.color = (1, 1, 1)
    for l in leds_vertes:
        l.on()

    sleep(1)

    # Éteint tout
    rgb.off()
    for l in leds_vertes:
        l.off()

# Lancement automatique du test au démarrage
test_initial()

# Attribution de la fonction au bouton
bouton.when_pressed = sequence_bouton

pause()
