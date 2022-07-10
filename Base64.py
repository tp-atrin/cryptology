def base64encode(s):
    i = 0
    base64 = ending = ''
    base64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    # Add padding if string is not dividable by 3
    pad = 3 - (len(s) % 3)
    if pad != 3:
        s += "A" * pad
        ending += '=' * pad

    # Iterate though the whole input string
    while i < len(s):
        b = 0
        # Take 3 characters at a time, convert them to 4 base64 chars
        for j in range(0, 3, 1):
            # get ASCII code of the next character in line
            n = ord(s[i])
            i += 1

            # Concatenate the three characters together
            b += n << 8 * (2 - j)

        # Convert the 3 chars to four Base64 chars
        base64 += base64chars[(b >> 18) & 63]
        base64 += base64chars[(b >> 12) & 63]
        base64 += base64chars[(b >> 6) & 63]
        base64 += base64chars[b & 63]
    # Add the actual padding to the end
    if pad != 3:
        base64 = base64[:-pad]
        base64 += ending

    # Print the Base64 encoded result
    return base64




#main part
enc = base64encode(input("Enter your plain text: "))

print("encrypted:", enc)

