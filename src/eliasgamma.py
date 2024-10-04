import math
from src.parser import Parser

class EliasGamma:
    def __init__(self):
        self.parser = Parser()

    def encoder(self, message_encoder : list):
        message_ascii = self.parser.parse_symbols_to_ascii(message_encoder)
        i = 0
        final_code_word = ""

        for _ in message_ascii:

            # Acha a potência de 2 mais próxima do número
            lower_power = 2 ** math.floor(math.log2(message_ascii[i]))  # Potência de 2 menor ou igual a n
        
            # Calcula o resto que falta até o número
            rest = message_ascii[i] - lower_power
            
            # Formata a sequência de bits
            prefix = power_of_two(lower_power) * '0'
            sufix = bin(rest)[2:] + '1' # Adicionar o stop bit

            # Sequência de bits do símbolo e da palavra toda
            codeword = prefix + sufix
            final_code_word += codeword
            i += 1

        return final_code_word
    

    def decoder(self, message_decoder : list):
        decoded_numbers = []
        i = 0
    
        while i < len(message_decoder):

            # Conta o número de zeros até o primeiro 1
            zero_count = 0
            while i < len(message_decoder) and message_decoder[i] == '0':
                zero_count += 1
                i += 1
        
            # Avança para o próximo bit depois do 1
            i += 1 
        
            # Ler o restante da codeword
            binary_number = '1'  # Começa com o bit '1' que foi omitido na codificação
            for _ in range(zero_count):
                if i < len(message_decoder):
                    binary_number += message_decoder[i-1]
                    i += 1

            decoded_number = int(binary_number, 2)

            # Ver se o caractere está dentro do range da tabela ASCII
            if 32 <= decoded_number <= 126:
                decoded_numbers.append(int(binary_number, 2))
                final = self.parser.parse_ascii_to_symbols(decoded_numbers)
                        
        return  "".join(value for value in final)


def power_of_two(n):
    power = 0
    while n > 1:
        n /= 2
        power += 1
    return power