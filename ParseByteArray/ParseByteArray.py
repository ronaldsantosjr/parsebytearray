import csv
import json

# Nome do arquivo de entrada e saída
input_file = "clientes.csv"
output_file = "clientes_parseados.csv"

# Ler e processar o arquivo CSV
with open(input_file, mode="r", newline="", encoding="utf-8") as infile,     open(output_file, mode="w", newline="", encoding="utf-8") as outfile:
    
    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    
    for row in reader:
        # Carrega JSON da primeira coluna
        cliente_json = json.loads(row[0])
        
        # Converte valores de hexadecimal para string
        cliente_parseado = {k: bytes.fromhex(v).decode("utf-8") for k, v in cliente_json.items()}
        
        # Cria uma nova linha com o JSON original na coluna A e valores parseados nas colunas seguintes
        nova_linha = [v for v in cliente_parseado.values()]
        
        # Escreve a linha no arquivo de saída
        writer.writerow(nova_linha)

print(f"Arquivo processado e salvo como {output_file}")
