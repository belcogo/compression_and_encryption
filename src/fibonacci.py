from src.parser import Parser

class Fibonacci:
    def __init__(self) -> None:
        self.parser = Parser()

    def generate_fibonacci_array(self, number):
        fibonacci_array = []

        fibonacci_array.append(1)
        fibonacci_array.append(2)

        while fibonacci_array[len(fibonacci_array) - 1] <= number:
            array_index = len(fibonacci_array) - 1
            value_to_add = fibonacci_array[array_index] + fibonacci_array[array_index-1]

            if (value_to_add <= number):
                fibonacci_array.append(value_to_add)
            else:
                break

        return fibonacci_array


    def fibonacci_value(self, number):
        fibonacci_array = self.generate_fibonacci_array(number)
        inversed_binary_value = []
        value = 0

        while (len(fibonacci_array) != 0):
            current_numb = fibonacci_array.pop()
            sum = value + current_numb

            if (sum <= number):
                value = sum
                inversed_binary_value.append(1)
            else:
                inversed_binary_value.append(0)

        return list(reversed(inversed_binary_value))

    def encrypt_symbol(self, symbol):
        ascii_value = self.parser.parse_symbol_to_ascii(symbol)
        returned_binary = self.fibonacci_value(ascii_value)
        stop_bit = '1'

        return ''.join(str(value) for value in returned_binary) + stop_bit
    
    def encrypt_symbols(self, symbols : list):
        encrypted_symbols = (self.encrypt_symbol(value) for value in symbols)
        return ''.join(value for value in encrypted_symbols)
    
    def split_symbols(self, encrypted_symbols : str):
        i = 0
        symbols_array = []
        curent_string = ''

        while (i < len(encrypted_symbols)):
            curent_string += encrypted_symbols[i]

            if (i == len(encrypted_symbols) - 1 or (encrypted_symbols[i] == '1' and encrypted_symbols[i + 1] == '1')):
                symbols_array.append(curent_string)
                curent_string = ''
                i += 1
            
            i += 1
        
        return symbols_array

    def decrypt_symbol(self, encrypted_symbol : str):
        

        return ""

    def decrypt_symbols(self, encrypted_symbols : str):
        encrypted_symbols_array = self.split_symbols(encrypted_symbols)
        return ""