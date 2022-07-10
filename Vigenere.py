#Funktions
def encrypt(plaintext, key):#Wir definieren eine Fucktion, die den Klartext verschlüsselt.
    key_length = len(key)  #Die Länge von dem Schlüssel ist wichtig,dann schpeichern wir das in eine Variable.
    key_as_int = [ord(i) for i in key] #Dann bilden wir eine List, die ascii code von jeder Buchschtabe von Schlüssel enthält.
    plaintext_int = [ord(i) for i in plaintext] #Dann bilden wir eine List, die ascii code von jeder Buchschtabe von Klartext enthält.
    ciphertext = '' #Wir definieren eine Variable,welche unseren Geheimtext enthalten wird.
    for i in range(len(plaintext_int)): #Wir erstellen eine Loop, die über die Länge unseres Klartextes läuft.
        value = (plaintext_int[i] + key_as_int[i % key_length]) % 26 #Wir addieren die ascii code von jeder Buchschtabe von klartext zu
                                                                     #ascii code von jeder Buchschtabe von Schlüssel.
                                                                     #Dann teilen wir das Ergebnis durch 26 und bekommen den Rest davon.
                                                                     #Dann speichern wir das in "value".
        ciphertext += chr(value + 65) #Dann addieren wir 65 zu "value" und dann wandeln wir das Ergebnis zu Buchstabe um.
    return ciphertext


#Main part
plaintext = input("Enter your plain text: ").replace(" ", "").upper() #Wir bekommen klartext und ersetzen statt leerzeichen nichts.
                                                                                 # und dann machen alle Buchschtaben groß.
key = input("Please enter the key: ").upper() #Wir bekommen den Schlüssel und dann machen alle Buchschtaben groß.
ciphertext = encrypt(plaintext,key) #Dann definieren eine Variable, die verschlüsselten Geheimtext enthält.
print("Your ciphertext is: " + ciphertext) #wir drucken Geheim-text ein.

