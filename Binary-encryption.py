
#Zuerst importieren wir eine Bibliothek(library),dir "random" heißt.
#Damit bilden wir einen zufälligen(random) Schlüssel.
import random


#Wir definieren eine Menge von Buchschtaben
# damit wir einen zufälligen(random) Schlüssel bilden.
char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

#Wir brauchen ein "dictionary".So können wir einen einfachen Text in Bits umwandeln.
alphabet = {'E': 0,
            'T': 10,
            'A': 110,
            'O': 1110,
            'I': 11110,
            'N': 111110,
            'S': 1111110,
            'H': 11111110,
            'R': 111111110,
            'D': 1111111110,
            'L': 11111111110,
            'C': 111111111110,
            'U': 1111111111110,
            'M': 11111111111110,
            'W': 111111111111110,
            'F': 1111111111111110,
            'G': 11111111111111110,
            'Y': 111111111111111110,
            'P': 1111111111111111110,
            'B': 11111111111111111110,
            'V': 111111111111111111110,
            'K': 1111111111111111111110,
            'J': 11111111111111111111110,
            'X': 111111111111111111111110,
            'Q': 1111111111111111111111110,
            'Z': 11111111111111111111111110 }


#Mit dieser Funktion wandeln wir einen einfachen Text in Bits um.
def plan_to_bits(p):
    bits = ''
    for i in p:
        if i in alphabet:
            bits += str(alphabet[i])
    return bits


#Mit dieser Funktion codieren wir die Bits, die aus Klartext stammen.
def encrypt(p, k):
    c = ''
    for i in range(len(p)):
        a = int(p[i])
        b = int(k[i])
        tmp = a^b
        c += str(tmp)
    return c

#main
msg = input("Enter your plain text: ")#wir bekommen den Klartext.
my_key = ""
for x in range(len(msg)):          #Wir bilden einen zufälligen(random) Schlüssel
    my_key += random.choice(char)
akey = plan_to_bits(my_key)        #Wir wandeln den Schlüssel in Bits um.
p = msg.upper().replace(' ', '')   #wir lösen alle Plätze und machen alle Buchschtaben groß.
pbits = plan_to_bits(p)            #Wir wandeln den Klar-text in Bits um.
c = encrypt(pbits, akey)           #Wir verschlüsseln den Klar-text mit unserem Schlüssel.
print ("Your ciphertext is: " + c)  #Wir drucken den Geheimtext.
print("Your one-time key is: " + my_key) #Wir drucken den Schlüssel.

