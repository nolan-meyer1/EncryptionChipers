import FinalProject
import unittest

class CeaserCipherEncryptionTest(unittest.TestCase):

    def test_aToX(self):

        self.assertEqual(FinalProject.ceaserCipher('a',-3),'x',"This did not convert a to an X")
    
    def test_SamplePhraseLeftShiftThree(self):
        self.assertEqual(FinalProject.ceaserCipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",-3),"QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD","Didn't properly convert sample string")
    
    def test_SamplePhraseWithNumbers(self):
        self.assertEqual(FinalProject.ceaserCipher("THE QUICK BROWN FOX JUMPS OVER 13 LAZY DOG",-3),"QEB NRFZH YOLTK CLU GRJMP LSBO 13 IXWV ALD","Didn't properly convert sample string")
    
    


if __name__ == '__main__':
    unittest.main()

