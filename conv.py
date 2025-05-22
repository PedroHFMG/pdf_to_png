import os, pymupdf, argparse

def conv(pdfpath, pages, output_dir = None, dpi=300, filename=None):
    if not os.path.exists(pdfpath):
        print("Erro: o diretório do arquivo PDF não existe.")
        return False
    
    try:
        pdf_doc = pymupdf.open(pdfpath)
        total_pages = pdf_doc.page_count
        print(total_pages)

        #if pages is None:
        for page in pdf_doc:
            page_img =  page.get_pixmap(matrix=pymupdf.Matrix(2, 2))
            page_img.save(f"{filename}{page.number + 1}.png")
        print("Conversão finalizada com sucesso.")
        return True
        
    except Exception as e:
        print(f"Erro durante a conversão: {str(e)}")
        return False

def parse_pages(input_str, pages):
    input_str = input_str.strip().upper()
    if input_str == "T":
        return pages

def main():
    parser = argparse.ArgumentParser(description="Converte PDF em imagens.")
    parser.add_argument('pdfpath', help='Arquivo PDF de entrada (precisa estar na mesma pasta).')

    args = parser.parse_args()
    pdf_doc = pymupdf.open(args.pdfpath)
    pages = pdf_doc.page_count

    if pages > 1:
        print(f"Seu arquivo possui {pages} páginas.")
        choice = input("Quais páginas deseja converter? (T) todas ou (X-Y) intervalo: ")
        pages_to_convert = parse_pages(choice, pages)
        while pages_to_convert is None:
            print("Entrada inválida! Tente novamente.")
            choice = input("Quais páginas deseja converter? (T) todas ou (X-Y) intervalo: ")
            pages_to_convert = parse_pages(choice, pages)

    filename = os.path.splitext(os.path.basename(args.pdfpath))[0]
    custom_name = input(f"Digite um nome para seu arquivo final, ou pressione ENTER para manter o nome do arquivo-mãe ({filename}): ")

    if not custom_name: 
        custom_name = filename

    conv(args.pdfpath, pages, filename=custom_name)

if __name__ == "__main__":
    main()