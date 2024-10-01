import numpy as np
from src.parser import Parser

class Golomb:
  def __init__(self):
    self.parser = Parser()
  
  def choose_k(self, ascii_list):
    ascii_mean = np.mean(ascii_list)
    
    k = 2 ** int(np.log2(ascii_mean))
    return k

  def golomb_encoder(self, message : list):
    message_ascii = self.parser.parse_symbols_to_ascii(message)
    k = self.choose_k(message_ascii)
    
    encoded_message = ""
    stop_bit = "1"

    for i in message_ascii:
      if i < k:
        prefix = ""
      else:
        zero_prefix = int(i / k)
        prefix = zero_prefix * "0"
      
      suffix_size = int(np.log2(k))
      division_result_mod = i % k
      suffix = format(division_result_mod, "0" + str(suffix_size) + "b")

      partial_encoded_message = prefix + stop_bit + suffix
      encoded_message += partial_encoded_message

    return encoded_message, k
  
  def golomb_decoder(self, encoded_message:str, k:int):
    decoded_message = ""
    suffix_size = int(np.log2(k))
    stop_bit = "1"
    
    while len(encoded_message) > 0:
      stop_bit_index = encoded_message.index(stop_bit)

      prefix = encoded_message[:stop_bit_index]

      encoded_message = encoded_message[stop_bit_index + 1:]
      
      zero_prefix = prefix.count("0")

      suffix = encoded_message[:suffix_size]
      
      encoded_message = encoded_message[suffix_size:]
      
      ascii_value = zero_prefix * k + int(suffix, 2)

      decoded_message += self.parser.parse_ascii_to_symbol(ascii_value)

    return decoded_message
