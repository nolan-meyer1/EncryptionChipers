import EncryptionCiphers
import unittest

class CeasarCipherEncryptionTest(unittest.TestCase):

    def test_aToX(self):
        self.assertEqual(EncryptionCiphers.ceasarCipher('a',-3),'x',"This did not convert a to an X")
    
    def test_SamplePhraseLeftShiftThree(self):
        self.assertEqual(EncryptionCiphers.ceasarCipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",-3),"QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD","Didn't properly convert sample string")
    
    def test_SamplePhraseWithNumbers(self):
        self.assertEqual(EncryptionCiphers.ceasarCipher("THE QUICK BROWN FOX JUMPS OVER 13 LAZY DOG",-3),"QEB NRFZH YOLTK CLU GRJMP LSBO 13 IXWV ALD","Didn't properly convert sample string")
    
    def test_rightShiftTest(self):
        self.assertEqual(EncryptionCiphers.ceasarCipher("Caesar Cipher 123! The quick brown fox jumps over the lazy dog.",30),"Geiwev Gmtliv 123! Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk.","Didn't correctly encrypt")
    


class CeasarCipherDecryptionTest(unittest.TestCase):

    def test_xToA(self):
        self.assertEqual(EncryptionCiphers.decryptCeasarCipher('x',-3),'a',"This did not convert x to A")
    
    def test_rightShiftDecryption(self):
        self.assertEqual(EncryptionCiphers.decryptCeasarCipher("Geiwev Gmtliv 123! Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk.",30),"Caesar Cipher 123! The quick brown fox jumps over the lazy dog.","Didn't correctly decrypt")



class VigenereCipherEncryptionTest(unittest.TestCase):

    def test_aToO(self):
        self.assertEqual(EncryptionCiphers.vigenereCipher("a","oculorhinolaryngology"),'o',"a was not properly converted to o")
    
    def test_sampleStringTest(self):
        self.assertEqual(EncryptionCiphers.vigenereCipher("attacking tonight","oculorhinolaryngology"),"ovnlqbpvt hznzeuz","Sample string was not properly converted")
    
    
    def test_unequalKeySize(self):
        self.assertEqual(EncryptionCiphers.vigenereCipher("HELLO WORLD","KEY"),"RIJVS UYVJN","Does not work when key is not greater than or equal to the size of the string")


class VigenereCipherDecryptionTest(unittest.TestCase):

    def test_aToO(self):
        self.assertEqual(EncryptionCiphers.decryptVigenereCipher("o","oculorhinolaryngology"),'a',"o was not properly converted to a")
    
    def test_sampleStringTest(self):
        self.assertEqual(EncryptionCiphers.decryptVigenereCipher("ovnlqbpvt hznzeuz","oculorhinolaryngology"),"attacking tonight","Sample string was not properly converted")

    def test_unequalKeySize(self):
        self.assertEqual(EncryptionCiphers.decryptVigenereCipher("RIJVS UYVJN","KEY"),"HELLO WORLD","Does not work when key is not greater than or equal to the size of the string")
    

class LengthenKeyTest(unittest.TestCase):

    def test_lengthenKeyTest(self):
        self.assertEqual(EncryptionCiphers.lengthenKey("KEY",10),"KEYKEYKEYK","Key did not get properly lengthened")



class GreatestCommonDivsiorTest(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(EncryptionCiphers.gcd(61,53),1,"Did not generate the correct gcd.")


class LeastCommonMultipleTest(unittest.TestCase):

    def test_lcm(self):
        self.assertEqual(EncryptionCiphers.lcm(60,52),780,"Did not generate the correct lcm")


class GetRsaEncryptionKeysTest(unittest.TestCase):
    
    def test_getEncryptionKeys(self):
        self.assertEqual(EncryptionCiphers.getRsaEncryptionKeys(),((3233,17),(3233,413)),"Did not generate the correct keys")


class EncryptUsingRSATest(unittest.TestCase):

    def test_encryptUsingRsaTest(self):
        self.assertEqual(EncryptionCiphers.encryptUsingRSA("a",(3233,17)),"11001100000","Did not properly encrypt")


class DecryptUsingRSATest(unittest.TestCase):

    def test_decryptUsingRsaTest(self):
        self.assertEqual(EncryptionCiphers.decryptUsingRSA("11001100000",(3233,413)),"a","Did not decrypt correctly")



if __name__ == '__main__':
    unittest.main()

