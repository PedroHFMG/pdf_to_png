# PDF to Image Converter
Um projeto pessoal para converter páginas de arquivos PDF em imagens PNG, com suporte a diferentes linguagens e interfaces.

## Objetivo
Criar uma ferramenta simples  para extrair imagens de arquivos PDF. Será desenvolvido em múltiplas linguagens, com foco inicial em linha de comando (CLI - Command Line Interface) e, futuramente, com interface gráfica.

## Suporte planejado:

| Plataforma | Status        | Tipo             |
|------------|---------------|------------------|
| Python     | ✅ Concluído | CLI            |
| Node.js    | 🔜 Planejado | CLI               |
| C#         | 🔜 Planejado | Interface gráfica |
| Java       | 🔜 Planejado | Interface gráfica |

## Instruções
### 1. Dependências
- Python instalado

- Biblioteca PyMuPDF: `pip install pymupdf`
### 2. Preparação
Coloque o arquivo conv.py em uma pasta qualquer, junto com seu PDF, e dentro da pasta execute `python conv.py [nome-do-seu-arquivo.pdf]`
### 3. Processo de Conversão
Em caso de PDFs com mais de uma página, será perguntado se o usuário deseja converter todas as páginas, ou somente um intervalo.

Digite **T** para todas, uma página específica, ou **X-Y** para um intervalo (2-5, por exemplo).

Depois será perguntado se deseja manter o nome do arquivo original, ou usar um nome personalizado.
### 4. Resultado
As imagens serão geradas na mesma pasta do arquivo .py