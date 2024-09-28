from typing import List

class Parser:
    def parse_symbols_to_ascii(self, symbols):
        return [self.parse_symbol_to_ascii(symbol) for symbol in symbols]
    
    def parse_ascii_to_symbols(self, ascii_values):
        return [self.parse_ascii_to_symbol(value) for value in ascii_values]
    
    def parse_symbol_to_ascii(self, symbol):
        return ord(symbol)
    
    def parse_ascii_to_symbol(self, ascii_value):
        return chr(ascii_value)