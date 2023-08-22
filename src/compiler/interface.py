import subprocess

import tkinter as tk
from tkinter import scrolledtext
import builtins

from antlr4 import FileStream

from compiler import compiler

# Função para executar o código inserido pelo usuário
def execute_code():
    code = code_text.get("1.0", "end-1c")  # Obtém o código do campo de texto
    try:
        # Sobrescreve a função print para capturar a saída
        output_text.delete("1.0", "end")
        original_print = builtins.print
        def custom_print(*args, **kwargs):
            output_text.insert("end", " ".join(map(str, args)) + "\n")
            original_print(*args, **kwargs)
        builtins.print = custom_print
        
        with open('code.jsp', 'w') as file:
            file.write(code)

        file = FileStream('code.jsp')

        # Compila o código
        compiler(file)

        # Compila o código gerado para java
        subprocess.run(["java", "-jar", "jasmin.jar", "code.jsp"])

        print("Código compilado com sucesso! Execute no terminal o comando 'java code' para executar o código gerado.")

    except Exception as e:
        output_text.insert("end", f"Erro: {e}\n")

# Cria a janela principal
root = tk.Tk()
root.title("Execução de Código")

# Campo de texto para o código
code_label = tk.Label(root, text="Insira o código:")
code_label.pack()
code_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
code_text.pack()

# Botão de execução
execute_button = tk.Button(root, text="Compilar Código", command=execute_code)
execute_button.pack()

# Saída do código
output_label = tk.Label(root, text="Saída:")
output_label.pack()
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
output_text.pack()

# Inicia a interface
root.mainloop()