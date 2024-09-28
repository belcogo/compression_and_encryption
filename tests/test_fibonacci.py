import unittest
from src.fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.fibonacci = Fibonacci()


    def test_fibonacci_encrypt_symbol(self):
        input_simbols = "("
        expected_output = "100100011"
        encrypted_symbol = self.fibonacci.encrypt_symbol(input_simbols)
        
        self.assertEqual(encrypted_symbol, expected_output, f"Dado a string de entrada {input_simbols}, Quando executado a função encrypt_symbols, Então o retorno será {expected_output}.")

    def test_generate_fibonacci_array(self):
        input = 40
        expected_return = [1, 2, 3, 5, 8, 13, 21, 34]

        output = self.fibonacci.generate_fibonacci_array(input)

        self.assertEqual(output, expected_return)
    
    def test_fibonacci_encrypt_symbols(self):
        input_simbols = "(Oi)"
        expected_output = "100100011001000101100100100011010100011"
        encrypted_symbol = self.fibonacci.encrypt_symbols(input_simbols)
        
        self.assertEqual(encrypted_symbol, expected_output, f"Dado a string de entrada {input_simbols}, Quando executado a função encrypt_symbols, Então o retorno será {expected_output}.")


if __name__ == '__main__':
    unittest.main()
