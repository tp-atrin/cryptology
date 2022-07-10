#Zuerst bilden wir ein  "Dictionary",die ensprechende "morse code" für jede Buchschtabe enthält.
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# Funktion zum Verschlüsseln des Strings
def encrypt(message):
    cipher = '' #wie haben ein leere String,die Morse code enthalten wird.
    for letter in message: #damit lesen wir jede Buchschtabe in massage
        if letter != ' ':

            cipher += MORSE_CODE_DICT[letter] + ' ' #damit addieren wir ensprechende "morse code" je nach den Buchschtabe.
        else:

            cipher += ' '  #Wir brauchen "space". Dann wenn "space" gesehen wird, muss genau so wie das ist hinzufügt werden.

    return cipher




#main part
message = input("Enter your plain text: ") #Wir bekommen einen Klar-text
result = encrypt((message.upper())) #Wir verschlüsseln den Klartext
print("Your ciphertext is: " + result) #wir drucken Geheim-text ein.

