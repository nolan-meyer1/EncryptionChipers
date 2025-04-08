# EncryptionChipers
This project contains some very simple encryption algorithims. It contains the Ceaser Cipher, Vigenere Cipher, and XOR Cipher. Run the Menu.py
file to try some of them out! 

## Ceaser Cipher
This is one of the most simple and classic ciphers but it's pretty cool. The way this is done is by shifting each character in
the string you're trying to encrypt so many spaces over right or left in the alphabet. For example if I have a right shift of
5 and shift the letter A it would become an F.

![image](https://github.com/user-attachments/assets/74888333-3e5a-4fae-8558-dee22b62d36e)

## Vigenere Cipher
The Vigenere Cipher is similar to the ceaser cipher. With this algorithim you can create your own custom encryption key. It's crucial
that encryption key is hte same length of the string that you're trying to encrypt. If not you'll want to repeat the key at the end or
just cycle back to the beginning once you get to the end of the key. Once you ahve your key you will shift the string that you're trying
to encrypt based off how many spaces the key is. For example if I have the key "kllked" and the string "hello". I would shift "h" over
over 11 spaces because 'k' is the 11th letter in the alphabet. The corresponding letter would then be 'R' as shown on the table:
![image](https://github.com/user-attachments/assets/00a1bb7c-a708-46f0-b700-03a53d5da099)

## XOR Cipher
The XOR Cipher is one of my favorite I did for this assignment. The way the XOR cipher works is by generating a random key that is the 
length of the string that you're trying to encrypt. Once you have that string you look at the character and do an XOR bit operation with
both of the characters in the string and encryption key that are at the same position. This also makes it where it is symetric encryption
meaning that the same encryption key is used for encryption and decryption. That is the power of using the XOR operation becasue it's
basically toggling bits meaning that you don't lose data when you do this operation allowing us to use one key for both encryption and 
decryption. When doing this a lot of time we will save the binary to a file that we will then decrypt because a lot of times it will decrypt
the character into something that isn't nessecarily a readable character.

```
String: Hello
Encryption Key: jmn$s

    h: 0100 1000
xor j: 0110 1010
----------------
 NAK = 0010 0010  
```

## Rivest–Shamir–Adleman(RSA) Cryptosystem
This is a more complex algorithim. It starts off the calculation by generating two large primes p and q. 

