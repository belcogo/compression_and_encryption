from src.parser import Parser
import collections

class RRepetition:
    def __init__(self, r):
        self.parser = Parser()
        self.r = r
    
    def getWord(self, data):
        ascii_bit_groups = [data[i:i+8] for i in range(0, len(data), 8)]
        ascii_values = [int(bits, 2) for bits in ascii_bit_groups]
        decoded_message = "".join(self.parser.parse_ascii_to_symbols(ascii_values))
        return decoded_message
    
    def encode(self, data):
        # Multiplica cada caractere por 'r' para codificação
        return data * self.r

    def transmit(self, data):
        ascii_code = self.parser.parse_symbols_to_ascii(data)

        encoded = []

        # Intera sobre eles
        for i in range(0, len(ascii_code)):
            # Tranforma o ASCII code para binário.
            binary = self.parser.parse_decimal_to_binary(ascii_code[i], 8)
            encoded.append(self.encode(binary))

        result = "".join(map(str, encoded))
        return result
    
    def decode(self, data):
        # Decodifica a mensagem transmitida
        result = ''
        dataChars = list(self.getWord(data))
        
        # Itera sobre os blocos de tamanho 'r'
        for k in range(0, len(dataChars) // self.r):  # Garante iteração somente dentro do limite
            step = k * self.r
            subArr = ''.join(dataChars[step:step + self.r])
            
            if subArr:  # Evita erros se subArr for vazio
                result += collections.Counter(subArr).most_common(1)[0][0]
            else:
                print(f"Warning: subArr vazio na iteração {k}.")
        
        return result
    
