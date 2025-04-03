"""
Module that contains popular encryption ciphers

Ceaser Cipher: https://en.wikipedia.org/wiki/Caesar_cipher
Substiution Cipher: https://en.wikipedia.org/wiki/Substitution_cipher
Viginere Cipher: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

"""

def ceasarCipher(string, shift):
    """
    This function takes in a string that will be encrypted and the shift that you want to do.
    If you give it a negative number it's a left shift. If you give it a positive number it 
    is a right shift.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = []

    for character in string:

        if character.isalpha():
            shiftedIndex = (alphabet.index(character.lower()) + shift) % 26

            if character.isupper():

                output.append(alphabet[shiftedIndex].upper())
            else:
                output.append(alphabet[shiftedIndex])
    
        else:
            output.append(character)


    return "".join(output)


def decryptCeasarCipher(string, shift):
    """
    This method handles the decryption of the ceaser cipher. You will have to give it the shift as well as the string you want to decrypt
    This works by using the original ceasar cipher method but using the opposite of it's shift. 
    """
    return ceasarCipher(string,-shift)


def substituionCipher():
    pass

def vigenereCipher(string,key):
    """
    This is the vignere cipher. This works by giving a string and key.
    If they key is not the same length as the string it will then repeat 
    the key until it is the same length. After that it will look at each
    character in the string and compare it with each character in the key. 
    It will shift the string based off what position the same element in the
    key is in the alphabet. 
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = []
    keyIndex = 0
    keyLength = getLength(key)
    stringLength = getLength(string)

    if keyLength != stringLength:
        key = lengthenKey(key,stringLength)

    for character in string:

        if character.isalpha():
            shiftedIndex = (alphabet.index(character.lower()) + alphabet.index(key[keyIndex].lower())) % 26

            if character.isupper():

                output.append(alphabet[shiftedIndex].upper())
            else:
                output.append(alphabet[shiftedIndex])
            
            keyIndex += 1
    
        else:
            output.append(character)
    
    return "".join(output)

def decryptVigenereCipher(string,key):
    """
    This method does the opposite of the vigenere encryption cipher
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    output = []
    keyIndex = 0
    keyLength = getLength(key)
    stringLength = getLength(string)

    if keyLength != stringLength:
        key = lengthenKey(key,stringLength)

    for character in string:

        if character.isalpha():
            shiftedIndex = (alphabet.index(character.lower()) - alphabet.index(key[keyIndex].lower())) % 26

            if character.isupper():

                output.append(alphabet[shiftedIndex].upper())
            else:
                output.append(alphabet[shiftedIndex])
            
            keyIndex += 1
    
        else:
            output.append(character)
    
    return "".join(output)


def getLength(string):
    """
    This method is used to get the length of a string
    not account for spaces.
    """
    length = 0

    for character in string:

        if character != " ":
            length += 1
        
    return length

def lengthenKey(key,length):
    """
    This is used for the vigenere chipher. if the key isn't long
    enough it makes the key the length of the string by repeating 
    the key.
    """

    output = [key]
    keyLength = getLength(key)
    difference = length - keyLength
    keyPosition = 0

    for i in range(difference):
        output.append(key[keyPosition])
        keyPosition += 1

        if keyPosition >= keyLength:
            keyPosition = 0
    
    return "".join(output)




def enigmaCipher():
    pass