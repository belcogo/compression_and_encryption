import unittest
from src.hamming import Hamming


class TestHamming(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.hamming = Hamming()


    def test_hamming_encoded(self):
        input_simbols = "a" # ASCII 1100001 - 0110 0001

        # 0110 -> s1: 0, s2: 1, s3: 1, s4:0, t5: 0, t6: 0, t7: 1
        # 0110 -> s1: 0, s2: 0, s3: 0, s4:1, t5: 0, t6: 1, t7: 1
        # 0110001 0001011
        expected_ouput = "01100010001011"

        encrypted_symbol = self.hamming.encode(input_simbols)
        
        self.assertEqual(encrypted_symbol, expected_ouput, f"Dado a string de entrada {input_simbols}, Quando executado a função encode, Então o retorno será {expected_ouput}.")

    def test_validate_has_error_when_having_error(self):
        hamming_code_with_error = "0110000" # ASCII 1100001 - 0110 0001

        expected_ouput = {
            "calculated": "0110001",
            "received": "0110000",
            "has_error": True
        }

        result = self.hamming.validate_has_error(hamming_code_with_error)
        
        self.assertEqual(result, expected_ouput, f"Dado a string de entrada {hamming_code_with_error}, Quando executado a função validate_has_error, Então o retorno será {expected_ouput}.")




if __name__ == '__main__':
    unittest.main()
