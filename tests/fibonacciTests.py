import unittest
from src.fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):
    
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.fibonacci = Fibonacci()

    def test_fibonacci_encrypt(self):
        """Teste se o valor encriptado está correto."""
        input_simbols = ""
        expected_output = ""
        encrypted_symbol = self.fibonacci.encrypt(input_simbols)
        
        self.assertEqual(encrypted_symbol, expected_output)
        

if __name__ == '__main__':
    unittest.main()
