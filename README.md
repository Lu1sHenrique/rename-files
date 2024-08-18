# Renomeador de Arquivos por Correspondência

Este script em Python renomeia arquivos em um diretório com base na correspondência mais próxima entre os nomes fornecidos e os nomes dos arquivos existentes. A extensão original dos arquivos é mantida durante o processo de renomeação.

## Funcionalidades

- Renomeia arquivos em um diretório específico.
- Encontra o nome de arquivo mais semelhante usando a biblioteca `difflib`.
- Mantém a extensão original dos arquivos ao renomeá-los.
- Flexível, pois não requer a lista de nomes antigos, apenas a lista de novos nomes.

## Requisitos

- Python 3.x

## Instalação

1. Clone este repositório ou faça o download dos arquivos.
2. Navegue até o diretório do projeto.

## Uso

1. **Configure o diretório e os novos nomes de arquivos:**

   No script `rename_files_automatic.py` ou `rename_files_manually.py`, defina o caminho do diretório onde estão os arquivos que deseja renomear e a lista de novos nomes base.

   ```python
   # Diretório onde estão os arquivos
   directory_path = 'C:/caminho/para/seu/diretorio'

   # Lista de novos nomes base
   new_filenames = ['novo_nome1', 'novo_nome2', 'novo_nome3']


## Execute o script

```bash
python rename_files_automatic.py
```
ou

```bash
python rename_files_manually.py
```

## Resultado

O script irá renomear os arquivos no diretório especificado, preservando as extensões e exibindo no console os arquivos renomeados.

Exemplo de saída

```bash
Renamed: old_file1.png -> novo_nome1.png 
Renamed: old_file2.jpg -> novo_nome2.jpg
```

# Notas

- O script utiliza a função get_close_matches da biblioteca difflib para encontrar a correspondência mais próxima entre os nomes. Você pode ajustar o parâmetro cutoff se precisar de uma correspondência mais ou menos restrita.
- Certifique-se de que a lista de novos nomes (new_filenames) seja do mesmo tamanho ou menor que o número de arquivos no diretório.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou sugestões para este projeto. Abra um pull request ou relate problemas na seção de issues.