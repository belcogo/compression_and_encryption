import numpy as np
import math
from src.parser import Parser

class EliasGamma:
    def __init__(self):
        self.parser = Parser()

    def encoder(self, message_encoder : list):
        message_ascii = self.parser.parse_symbols_to_ascii(message_encoder)
        print(message_ascii)
        i = 0
        final_code_word = ""

        for number in message_ascii:
            # Acha a potência de 2 mais próxima do número
            lower_power = 2 ** math.floor(math.log2(message_ascii[i]))  # Potência de 2 menor ou igual a n
        
            # Calcula o resto que falta até o número
            rest = message_ascii[i] - lower_power
            
            # Formata a sequência de bits
            prefix = power_of_two(lower_power) * '0'
            sufix = bin(rest)[2:]

            # Sequência de bits do símbolo e da palavra toda
            codeword = prefix + sufix
            final_code_word += codeword
            i += 1

        return final_code_word
    

    def decoder(self, message_decoder : list):

        decoded_numbers = []
        i = 0
    
        while i < len(message_decoder):
            print(message_decoder)
            # Step 1: Contar o número de zeros até o primeiro '1' (Prefixo Unário)
            zero_count = 0
            while i < len(message_decoder) and message_decoder[i] == '0':
                zero_count += 1
                i += 1
        
            # O próximo bit deve ser '1' (parte final do prefixo)
            i += 1  # Avança para o próximo bit após o '1'
        
            # Step 2: Ler os próximos (zero_count) bits como o sufixo binário
            binary_number = '1'  # Começa com o bit '1' que foi omitido na codificação
            for _ in range(zero_count):
                print(i)
                binary_number += message_decoder[i-1]
                i += 1
        
            # Step 3: Converter o número binário em decimal e adicionar à lista de números decodificados
            decoded_numbers.append(int(binary_number, 2))
            final = self.parser.parse_ascii_to_symbols(decoded_numbers)

            # message_ascii = self.parser.parse_symbols_to_ascii(message_encoder)

        return final


def power_of_two(n):
    power = 0
    while n > 1:
        n /= 2
        power += 1
    return power