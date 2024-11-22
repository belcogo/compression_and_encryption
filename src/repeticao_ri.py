import collections

class RRepetition:
    def __init__(self, r):
        self.r = r
    
    def encode(self, data):
        # Multiplica cada caractere por 'r' para codificação
        return data * self.r

    def transmit(self, data):
        # Codifica e concatena todos os caracteres da mensagem
        result = [self.encode(char) for char in list(data)]
        return ''.join(result)
    
    def decode(self, data):
        # Decodifica a mensagem transmitida
        result = ''
        dataChars = list(data)
        
        # Itera sobre os blocos de tamanho 'r'
        for k in range(0, len(dataChars) // self.r):  # Garante iteração somente dentro do limite
            step = k * self.r
            subArr = ''.join(dataChars[step:step + self.r])
            
            if subArr:  # Evita erros se subArr for vazio
                result += collections.Counter(subArr).most_common(1)[0][0]
            else:
                print(f"Warning: subArr vazio na iteração {k}.")
        
        return result