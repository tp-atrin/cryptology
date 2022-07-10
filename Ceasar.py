#Cäser encryption

#Zuerst definieren wir ein Funktion, die Verschlüsseln übernihmt.
def cesar(text, key):
    empty = "" #Hier definieren wir ein Variable "empty" , die leer ist.empty wird am Ende Geheim-text enthalten.
    for i in text:  #wir bilden ein Loop.damit lesen wir jede Buchschtabe in text
        if i.isupper():  #Wenn die Buchschtabe "i" in text groß geschrieben ist, dann :
            empty += chr((ord(i) - ord('A') + key) % 26 + ord('A'))  #Wir reduzieren ascii code von Buchhschtabe "i" ascii code von "A" und addieren unseren Schlüssel dazu.
                                                                     #Dann teilen wir das Ergebnis durch 26 und bekommen den Rest davon.Und addieren ascii code von "A" zu Rest.
                                                                     #Und am Ende wandeln wir diese ergebte ascii code zu ein Buchschtabe um und addieren diese Buchschtabe zu "empty".


        elif i.islower(): #Wenn die Buchschtabe "i" in text groß geschrieben ist, dann :
            empty += chr((ord(i) - ord('a') + key) % 26 + ord('a'))#Wir reduzieren ascii code von Buchhschtabe "i" ascii code von "a" und addieren unseren Schlüssel dazu.
                                                                   #Dann teilen wir das Ergebnis durch 26 und bekommen den Rest davon.Und addieren ascii code von "a" zu Rest.
                                                                   #Und am Ende wandeln wir diese ergebte ascii code zu ein Buchschtabe um und addieren diese Buchschtabe zu "empty".


        elif i.isdigit(): #Wenn die Buchschtabe "i" in text eine Nummer ist, dann :
            empty += str((int(i) + key) % 10) #Das reicht, dass wir nur int(Zahl) von i zu key addieren und den Rest durch 26 rechnen
                                              # und das Ergebnis zu "string" umwandeln und am Ende diese Buchschtabe zu "empty" addieren.

        else:
            empty += i  #Wenn unser i Leerzeichen, Zeichen,Symbol usw. ist , dann das reicht,dass nur "i" zu "empty" addieren.
    return empty


#main part
text = input("Please enter a text: ") #wir bekommen den Klartext.
key = int(input("Please enter a key: ")) #wir bekommen den Schlüssel.
ciphertext = cesar(text, key) #wir definieren eine Variable, die verschlusselten Geheimtext enthält.
print(ciphertext) #wir drucken Geheim-text ein.

