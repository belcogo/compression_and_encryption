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
    s1, s2, s3, s4 = map(int, binary_word)

    # Cálcula os bits de verificação
    t5 =  int(s1) ^ int(s2) ^ int(s3)
    t6 =  int(s2) ^ int(s3) ^ int(s4)
    t7 = int(s1) ^ int(s3) ^ int(s4)

    return f"{s1}{s2}{s3}{s4}{t5}{t6}{t7}"

  def validate_has_error(self, hamming_code):
    # Obtém as informações de cada bit.
    s1, s2, s3, s4, t5, t6, t7 = map(int, hamming_code)

    # Verifica valor esperado com base em cálculo.
    t5_calculated = int(s1) ^ int(s2) ^ int(s3)
    t6_calculated = int(s2) ^ int(s3) ^ int(s4)
    t7_calculated = int(s1) ^ int(s3) ^ int(s4)

    # Atribuí valor de calculated e received.
    calculated = f"{s1}{s2}{s3}{s4}{t5_calculated}{t6_calculated}{t7_calculated}"
    received = f"{s1}{s2}{s3}{s4}{t5}{t6}{t7}"

    return {
      "calculated": calculated,
      "received": received,
      "has_error": calculated != received
    }

  def correct_error(self, hamming_code, calculated, received):
    # Extrai os bits de dados e paridade.
    data_bits = list(hamming_code[:4])
    calculated_parity = list(calculated[4:])
    received_parity = list(received[4:])  # Transformar em lista mutável.

    # Identifica os bits de paridade que não correspondem.
    mismatch_positions = [i for i in range(3) if calculated_parity[i] != received_parity[i]]

    # Se houver mais de um erro, não é possível corrigir.
    if len(mismatch_positions) > 1:
        return "", False

    # Se não houver erro, retorna os bits de dados diretamente.
    if len(mismatch_positions) == 0:
        return "".join(data_bits), True

    # Correções específicas para os bits de paridade e dados.
    # Erro no primeiro bit de paridade.
    if (received_parity[0] != calculated_parity[0]) and (received_parity[1] == calculated_parity[1]) and (received_parity[2] == calculated_parity[2]):
        received_parity[0] = calculated_parity[0]

    # Erro no segundo bit de paridade.
    if (received_parity[0] == calculated_parity[0]) and (received_parity[1] != calculated_parity[1]) and (received_parity[2] == calculated_parity[2]):
        received_parity[1] = calculated_parity[1]

    # Erro no terceiro bit de paridade.
    if (received_parity[0] == calculated_parity[0]) and (received_parity[1] == calculated_parity[1]) and (received_parity[2] != calculated_parity[2]):
        received_parity[2] = calculated_parity[2]

    # Correções nos bits de dados.
    if (received_parity[0] != calculated_parity[0]) and (received_parity[1] == calculated_parity[1]) and (received_parity[2] != calculated_parity[2]):
        data_bits[0] = '1' if data_bits[0] == '0' else '0'

    if (received_parity[0] != calculated_parity[0]) and (received_parity[1] != calculated_parity[1]) and (received_parity[2] == calculated_parity[2]):
        data_bits[1] = '1' if data_bits[1] == '0' else '0'

    if (received_parity[0] != calculated_parity[0]) and (received_parity[1] != calculated_parity[1]) and (received_parity[2] != calculated_parity[2]):
        data_bits[2] = '1' if data_bits[2] == '0' else '0'

    if (received_parity[0] == calculated_parity[0]) and (received_parity[1] != calculated_parity[1]) and (received_parity[2] != calculated_parity[2]):
        data_bits[3] = '1' if data_bits[3] == '0' else '0'

    return "".join(data_bits), True

  def decode(self, hamming_code):
    # Divide o código Hamming em blocos de 7 bits.
    hamming_code = [hamming_code[i:i+7] for i in range(0, len(hamming_code), 7)]

    # Decodifica cada bloco de 7 bits.
    decoded_bits = []
    for block in hamming_code:
      # Obtém os bits de dados.
      data_bits = block[:4]

      # Verifica se há erro.
      error = self.validate_has_error(block)

      # Se não houver erro, mantém os bits originais.
      if not error["has_error"]:
        decoded_bits.append(data_bits)
      else:
        # Se houver erro, tenta corrigi-lo.
        corrected, corrected_successfully = self.correct_error(block, error["calculated"], error["received"])
        if corrected_successfully:
          decoded_bits.append(corrected[:4])  # Adiciona apenas os bits de dados corrigidos.
        else:
          # Não foi possível corrigir o erro.
          return "Não foi possível corrigir o erro."

    # Junta todos os bits decodificados.
    decoded_bits_string = "".join(decoded_bits)

    # Divide os bits em grupos de 8 (para representar caracteres ASCII).
    ascii_bit_groups = [decoded_bits_string[i:i+8] for i in range(0, len(decoded_bits_string), 8)]

    # Converte os grupos de 8 bits para valores ASCII.
    ascii_values = [int(bits, 2) for bits in ascii_bit_groups]

    # Usa o método parse_ascii_to_symbols para obter a mensagem final.
    decoded_message = "".join(self.parser.parse_ascii_to_symbols(ascii_values))

    # Retorna a mensagem decodificada.
    return decoded_message

