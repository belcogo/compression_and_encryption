from typing import List

class Parser:
    def parse_symbols_to_ascii(self, symbols: List[str]) -> List[int]:
        return [ord(symbol) for symbol in symbols]
    
    def parse_ascii_to_symbols(self, ascii_values):
        return [chr(value) for value in ascii_values]