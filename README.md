# EncryptionChipers
This project contains some very simple encryption algorithims. It contains the Ceaser Cipher, Vigenere Cipher,XOR Cipher, and RSA. Run the Menu.py
file to try some of them out! 

## Ceaser Cipher
This is one of the most simple and classic ciphers but it's pretty cool. The way this is done is by shifting each character in
the string you're trying to encrypt so many spaces over right or left in the alphabet. For example if I have a right shift of
5 and shift the letter A it would become an F.

![image](https://github.com/user-attachments/assets/74888333-3e5a-4fae-8558-dee22b62d36e)

## Vigenere Cipher
The Vigenere Cipher is similar to the ceaser cipher. With this algorithim you can create your own custom encryption key. It's crucial
that encryption key is the same length of the string that you're trying to encrypt. If not you'll want to repeat the key at the end or
just cycle back to the beginning once you get to the end of the key. In my code I made a method to handle this but if you want you could
just cycle back to the beginning of the encryption key string. Once you have your key you will shift the string that you're trying to encrypt 
based off how what position the character is in the alphabet in the key. For example if I have the key "kllked" and the string "hello". 
I would shift "h" over 11 spaces because 'k' is the 11th letter in the alphabet. The corresponding letter would then be 'R' as shown on the table:
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
This is a more complex algorithim. It starts off the calculation by generating two large primes p and q. I used the python module [sympy](https://www.sympy.org/en/index.html)
to accomplish this. After that you want to compute n = p * q which is the modulus for both the public and private key. Next you want to compute λ(n) = lcm(p-1,q-1). After λ(n) is
computed you want to generate a coprime e between 0 < e < λ(n). Lastly, you want to find d which is the modular multiplicative inverse of e(mod(λ(n))). This is the critical value that is
used to reverse the encryption. 
* Public Key (n,e)
* Private Key (n,d)

EX from [Wikipedia](https://en.wikipedia.org/wiki/RSA_cryptosystem)
<img width="965" alt="Screenshot 2025-04-09 at 10 33 54 AM" src="https://github.com/user-attachments/assets/60ea5b76-e601-4864-9b2a-a8b34c76834d" />

### Encryption/Decryption Further Explanation
Let's say for example I have these values:
* String to encrypt: "Hello Nolan"
* Public Key: (3233,17)
* Private Key: (3233,413)

RSA encryption works by giving someone else the public key so they can send you encrypted messages while you keep the private key private so only you can decrypt the message. This is
called asymetric encryption because you use two different keys for encryption and decryption. Let's start by encrypting the letter "H". We start by getting the ASCII value for "H" which is 72. We then do the calculation:

c(m) = m<sup>e</sup> % n 

72<sup>17</sup> % 3233 = 3000

This is a really long number. You can just use this number or you could convert it to binary if you would like. This is just for one character. We will then repeat the process over and over for each character resulting in the full encryption on the string looking something like this: 


| Character| Integer | Binary |
|---------|--------|-----------|
|H|3000|10100100001|
|e|1313|10100100001|
|l|745|100010001001|
|l|745|100010001001|
|o|1992|11111001000|
|N|3165|100010001001|
|o|2185|100010001001|
|l|745|100010001001|
|a|1632|11001100000|
|n|2235|100010111011|

To decrypt we use the same formula but with the different numbers. If the number was stored as binary you will want to convert it back to it's decimal. If it's a decimal then you can do the conversion like so:

m(c) = m<sup>d</sup> % n 

3000<sup>413</sup> % 3233 = 72

The reason this works is becasue we found that multiplicative inverse which essentially allows to reverse the encryption that we just did. 

After you have the original ASCII value you can then convert that back to a character. We will then complete this process for every character until the string is decrypted.


