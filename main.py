import tkinter as tk
from tkinter import ttk
import numpy as np
from src.fibonacci import Fibonacci
from src.golomb import Golomb
from src.huffmann import Huffmann

golomb_k = None
huffmann_alg = Huffmann()

def process_text():
    global golomb_k
    input_text = input_entry.get()
    operation = operation_var.get()
    algorithm = algorithm_var.get()

    fibonacci_alg = Fibonacci()
    golomb_alg = Golomb()

    # Aqui você pode implementar a lógica para codificação e decodificação
    if operation == 'Codificação':
        if algorithm == 'Fibonacci':
            output_text = fibonacci_alg.encrypt_symbols(input_text)
        elif algorithm == 'Huffman':
            output_text = huffmann_alg.encode(input_text)
        elif algorithm == 'Golomb':
            output_text, k = golomb_alg.golomb_encoder(input_text)
            golomb_k = k
    elif operation == 'Decodificação':
        if algorithm == 'Fibonacci':
            output_text = fibonacci_alg.decrypt_symbols(input_text)
        elif algorithm == 'Huffman':
            output_text = huffmann_alg.decode(input_text)
        elif algorithm == 'Golomb':
            output_text = golomb_alg.golomb_decoder(input_text, golomb_k)
    
    output_text_area.delete(1.0, tk.END)  # Limpa o campo de saída
    output_text_area.insert(tk.END, output_text)  # Insere o texto no campo de saída

# Criação da janela principal
root = tk.Tk()
root.title("Codificador/Decodificador")

# Input de texto
input_label = tk.Label(root, text="Texto:")
input_label.pack(pady=5)
input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=5)

# Select para operação
operation_var = tk.StringVar(value='Codificação')
operation_label = tk.Label(root, text="Escolha a operação:")
operation_label.pack(pady=5)
operation_select = ttk.Combobox(root, textvariable=operation_var, values=["Codificação", "Decodificação"])
operation_select.pack(pady=5)

# Select para algoritmo
algorithm_var = tk.StringVar(value='Fibonacci')
algorithm_label = tk.Label(root, text="Escolha o algoritmo:")
algorithm_label.pack(pady=5)
algorithm_select = ttk.Combobox(root, textvariable=algorithm_var, values=["Fibonacci", "Huffman", "Golomb"])
algorithm_select.pack(pady=5)

# Output de texto
output_label = tk.Label(root, text="Saída:")
output_label.pack(pady=5)
output_text_area = tk.Text(root, width=50, height=10)
output_text_area.pack(pady=5)

# Botão para processar
process_button = tk.Button(root, text="Processar", command=process_text)
process_button.pack(pady=20)

# Executar a aplicação
root.mainloop()
