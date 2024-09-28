import unittest
from src.parser import Parser

class TestParser(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.parser = Parser()
    
    def test_parser_parse_ascii_to_symbols(self):
        ascii_array = [116, 101, 115, 116, 101, 32, 97, 115, 99, 99, 105]
        expected_output = ['t', 'e', 's', 't', 'e', ' ', 'a', 's', 'c', 'c', 'i']

        parsed_symbols = self.parser.parse_ascii_to_symbols(ascii_array)

        self.assertEqual(parsed_symbols, parsed_symbols, f"Dado os valores ascii {ascii_array}, Quando executado a função parse_ascii_to_symbols, Então o retorno será {expected_output}.")

    def test_parser_parse_symbols_to_ascii(self):
        expected_output = [116, 101, 115, 116, 101, 32, 97, 115, 99, 99, 105]
        symbols_array = ['t', 'e', 's', 't', 'e', ' ', 'a', 's', 'c', 'c', 'i']

        parsed_ascii = self.parser.parse_symbols_to_ascii(symbols_array)

        self.assertEqual(parsed_ascii, expected_output, f"Dado os símbolos {symbols_array}, Quando executado a função parse_symbols_to_ascii, Então o retorno será {expected_output}.")

if __name__ == '__main__':
    unittest.main()
