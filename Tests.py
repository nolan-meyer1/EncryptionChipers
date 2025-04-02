import FinalProject
import unittest

class CeasarCipherEncryptionTest(unittest.TestCase):

    def test_aToX(self):
        self.assertEqual(FinalProject.ceasarCipher('a',-3),'x',"This did not convert a to an X")
    
    def test_SamplePhraseLeftShiftThree(self):
        self.assertEqual(FinalProject.ceasarCipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",-3),"QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD","Didn't properly convert sample string")
    
    def test_SamplePhraseWithNumbers(self):
        self.assertEqual(FinalProject.ceasarCipher("THE QUICK BROWN FOX JUMPS OVER 13 LAZY DOG",-3),"QEB NRFZH YOLTK CLU GRJMP LSBO 13 IXWV ALD","Didn't properly convert sample string")
    
    def test_rightShiftTest(self):
        self.assertEqual(FinalProject.ceasarCipher("Caesar Cipher 123! The quick brown fox jumps over the lazy dog.",30),"Geiwev Gmtliv 123! Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk.","Didn't correctly encrypt")
    


class CeasarCipherDecryptionTest(unittest.TestCase):

    def test_xToA(self):
        self.assertEqual(FinalProject.decryptCeasarCipher('x',-3),'a',"This did not convert x to A")
    
    def test_rightShiftDecryption(self):
        self.assertEqual(FinalProject.decryptCeasarCipher("Geiwev Gmtliv 123! Xli uymgo fvsar jsb nyqtw sziv xli pedc hsk.",30),"Caesar Cipher 123! The quick brown fox jumps over the lazy dog.","Didn't correctly decrypt")
        
    


if __name__ == '__main__':
    unittest.main()

