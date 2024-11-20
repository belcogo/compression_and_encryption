from src.parser import Parser

class Hamming:
  def __init__(self):
    self.parser = Parser()
    self.codeword = ""
    self.hamming_code = ""
    self.error = False
    self.error_position = 0

  def encode(self, codewords):
    # Obtém codewords para tabela ASCII
    encoded = []

    # Transforma a palavra em ASCII code.
    ascii_code = self.parser.parse_symbols_to_ascii(codewords)

    # Intera sobre eles
    for i in range(0, len(ascii_code)):
      # Tranforma o ASCII code para binário.
      binary = self.parser.parse_decimal_to_binary(ascii_code[i], 8)

      # Obtém a letra no código de hamming.
      encoded_letter = self.get_hamming_code(binary[0:4]) + self.get_hamming_code(binary[4:8])

      # Adiciona para o conjunto de retorno.
      encoded.append(encoded_letter)

    return "".join(map(str, encoded))

  def get_hamming_code(self, binary_word):
    # Obtém as informações de cada bit
    s1 = binary_word[0]
    s2 = binary_word[1]
    s3 = binary_word[2]
    s4 = binary_word[3]

    # Cálcula os bits de verificação
    t5 =  int(s1) ^ int(s2) ^ int(s3)
    t6 =  int(s2) ^ int(s3) ^ int(s4)
    t7 = int(s1) ^ int(s3) ^ int(s4)

    return f"{s1}{s2}{s3}{s4}{t5}{t6}{t7}"

  def validate_has_error(self, hamming_code):

    # Obtém as informações de cada bit.
    s1 = hamming_code[0]
    s2 = hamming_code[1]
    s3 = hamming_code[2]
    s4 = hamming_code[3]
    t5 = hamming_code[4]
    t6 = hamming_code[5]
    t7 = hamming_code[6]
    
    # Verifica valor esperado com base em cálculo.
    t5_calculated = int(s1) ^ int(s2) ^ int(s3)
    t6_calculated = int(s2) ^ int(s3) ^ int(s4)
    t7_calculated = int(s1) ^ int(s3) ^ int(s4)

    # Atribuí valor de expected e received.
    expected = f"{s1}{s2}{s3}{s4}{t5_calculated}{t6_calculated}{t7_calculated}"
    received = f"{s1}{s2}{s3}{s4}{t5}{t6}{t7}"

    return {
      "expected": expected,
      "received": received,
      "has_error": expected != received
    }

  def decode(self, hamming_code):
    if not self.validate_with_error(hamming_code):
      return "Código inválido"
    
    bits = [int(bit) for bit in hamming_code]
    
    p1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6] # XOR dos bits 0, 2, 4 e 6
    p2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6] # XOR dos bits 1, 2, 5 e 6
    p3 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6] # XOR dos bits 3, 4, 5 e 6
    error_position = p1 + p2 * 2 + p3 * 4
    if error_position > 0:
      self.error = True
      self.error_position = error_position
      bits[error_position - 1] ^= 1 # Inverte o bit com erro
    return "".join([str(bit) for bit in bits[2:]]) # Remove os bits de paridade e retorna a mensagem original