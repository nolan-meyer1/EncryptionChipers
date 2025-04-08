import EncryptionCiphers

def ceaserCipherMenu():
    keepGoing = True

    while keepGoing:
        print()
        print("Ceaser Cipher:")
        print("0. Quit")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        userInput = input("Please select an option: ")

        if userInput == "0":
            keepGoing = False

        elif userInput == "1":
            stringToBeEncrytped = input("Please enter string you want to be encrypted: ")
            shift = input("Please enter the shift: ")

            if isNumber(shift):
                encryptedString = EncryptionCiphers.ceasarCipher(stringToBeEncrytped,int(shift))
                print()
                print("Please copy this string and remember the shift you used to decrypt")
                print(f"Encrypted String: {encryptedString}")
            else:
                print("Shift must be an integer! Please try again!")
        
        elif userInput == "2":

            stringToBeDecrypted = input("Please enter string you want to be decrypted: ")
            shift = input("Please enter the shift: ")

            if isNumber(shift):
                decryptedString = EncryptionCiphers.decryptCeasarCipher(stringToBeDecrypted,int(shift))
                print()
                print(f"Decrypted String: {decryptedString}")
            else:
                print("Shift must be an integer! Please try again!")

        
        else:
            print("Please enter a valid response!")


def vigenereCipherMenu():

    keepGoing = True

    while keepGoing:
        print()
        print("Vigenere Cipher:")
        print("0. Quit")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        userInput = input("Please select an option: ")

        if userInput == "0":
            keepGoing = False

        elif userInput == "1":
            stringToBeEncrytped = input("Please enter string you want to be encrypted: ")
            encryptionKey = input("Please enter the encryption key you would like to use: ")
            encryptedString = EncryptionCiphers.vigenereCipher(stringToBeEncrytped,encryptionKey)

            print()
            print("Please copy this string and remember the shift you used to decrypt")
            print(f"Encrypted String: {encryptedString}")

        elif userInput == "2":
            stringToBeDecrypted = input("Please enter string you want to be decrypted: ")
            encryptionKey = input("Please enter the ecryption key: ")

            decryptedString = EncryptionCiphers.decryptVigenereCipher(stringToBeDecrypted,encryptionKey)
            print()
            print(f"Decrypted String: {decryptedString}")

        else:
            print("Please enter a valid response!")



def isNumber(number):
    """
    Used to verify if a string of numbers is a digit or not.
    """

    output = True

    try:
        int(number)
    except ValueError:
        output = False
    
    return output

def xorCipherMenu():

    keepGoing = True

    while keepGoing:
        print()
        print("XOR Cipher:")
        print("0. Quit")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        userInput = input("Please select an option: ")

        if userInput == "0":
            keepGoing = False

        elif userInput == "1":
            stringToBeEncrytped = input("Please enter string you want to be encrypted: ")
            encryptionKey = EncryptionCiphers.xorCipher(stringToBeEncrytped)

            print(f"Please save this key to decrypt encryption file: {encryptionKey}")

        elif userInput == "2":
            encryptionKey = input("Please enter the ecryption key: ")

            decryptedString = EncryptionCiphers.decryptXorCipher(encryptionKey)
            print()
            print(f"Decrypted String: {decryptedString}")

        else:
            print("Please enter a valid response!")



def main():

    keepGoing = True

    while keepGoing:

        print("0. Quit")
        print("1. Ceaser Cipher")
        print("2. Vigenere Cipher")
        print("3. XOR Cipher")
        userInput = input("Please enter an option: ")

        if userInput == "0":
            keepGoing = False
        elif userInput == "1":
            ceaserCipherMenu()
        elif userInput == "2":
            vigenereCipherMenu()
        elif userInput == "3":
            xorCipherMenu()
        else:
            print("Please enter a valid response!")

if __name__ == "__main__":        
    main()