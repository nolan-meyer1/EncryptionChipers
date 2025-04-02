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

def isNumber(number):

    output = True

    try:
        int(number)
    except ValueError:
        output = False
    
    return output



def main():

    keepGoing = True

    while keepGoing:

        print("0. Quit")
        print("1. Ceaser Cipher")
        userInput = input("Please enter an option: ")

        if userInput == "0":
            keepGoing = False
        elif userInput == "1":
            ceaserCipherMenu()
        else:
            print("Please enter a valid response!")
        
main()