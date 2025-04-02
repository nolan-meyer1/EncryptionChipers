"""
Module that contains popular encryption ciphers

Ceaser Cipher: https://en.wikipedia.org/wiki/Caesar_cipher
Substiution Cipher: https://en.wikipedia.org/wiki/Substitution_cipher
Viginere Cipher: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
Enigma Cipher: https://en.wikipedia.org/wiki/Enigma_machine

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

def vignereCipher():
    pass

def enigmaCipher():
    pass