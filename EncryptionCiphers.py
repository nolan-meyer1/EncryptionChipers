import string
import random
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



def generateKey(length):
    """
    This method generates a random key. It looks at the alphabet 
    and builds a string of random choices from the alphabet. 
    """
    return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation,k=length))



def xorCipher(string):
    """
    Cipher that does generates a random key based off the
    length of the string. Then it does xor on the each
    character of the encrypted key to each character on the
    cipher.
    """
    encryptionKey = generateKey(len(string))
    output = []

    for i in range(len(string)):

        output.append(bin(ord(string[i]) ^ ord(encryptionKey[i]))[2:].zfill(8))
    

    with open("Encrypted.txt","w") as file:
        file.write(" ".join(output))
    
    return encryptionKey



def decryptXorCipher(encryptionKey):
    """
    This handles the decryption of the encryption file that will be generated.
    """

    output = []
    
    with open("Encrypted.txt","r") as file:
        encryptedString = file.readline().split(" ")

        for i in range(len(encryptedString)):

            output.append(chr(int(encryptedString[i],2) ^ ord(encryptionKey[i])))
    
    return "".join(output)

def getRsaEncryptionKeys():
    """
    Method that returns a tuple of this strucutre
    ((Public key),(Private Key))
    """
    p = 61
    q = 53

    n = p * q
    lambdaSymbol = lcm(p-1,q-1)

    e = 17

    d = pow(e,-1,lambdaSymbol)

    return ((n,e),(n,d))

def encryptUsingRSA(stringToEncrypt,publicKey):
    """
    Uses the public key to decrypt using the
    modular inverse
    """

    output = []

    for character in stringToEncrypt:

        convertedCharacter = ord(character)
        output.append(bin(pow(convertedCharacter,publicKey[1],publicKey[0]))[2:])
    
    with open("Encrypted.txt","w") as file:
        file.write("\n".join(output))


def decryptUsingRSA(privateKey):
    """
    Uses the private key to decrypt using the
    modular inverse
    """

    output = []

    with open("Encrypted.txt","r") as file:

        for line in file:
            output.append(chr(pow(int(line,2),privateKey[1],privateKey[0])))
        
    return "".join(output)



def lcm(a,b):
    """
    Finds the least common multiple
    """
    return (a * b) // gcd(a,b)

def gcd(a,b):
    """
    Finds the greatest common divsor
    """

    while b:

        a,b = b, a % b

    return a