from gpiozero import RGBLED, LED, Button
from signal import pause
from time import sleep

# 1. Configuration des LEDs Vertes (J'ai changé le 2 par 23)
# Branche ta première LED sur le GPIO 23 à la place du 2
leds_vertes = [LED(27), LED(17), LED(2), LED(3)]

# 2. Configuration de la LED RGB (Anode Commune)
rgb = RGBLED(red=16, green=20, blue=21, active_high=False)

# 3. Configuration du Bouton relié au 3.3V
# pull_up=False active la résistance de Pull-down interne
bouton = Button(26, pull_up=False)

def sequence_bouton():
    print("Bouton pressé (Signal 3.3V reçu) !")
    rgb.color = (1, 1, 1)
    for l in leds_vertes: l.on()
    sleep(1)
    rgb.off()
    for l in leds_vertes: l.off()

bouton.when_pressed = sequence_bouton

print("Système prêt avec bouton au 3.3V.")
pause()
