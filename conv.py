import os, pymupdf, argparse

def conv(pdfpath, pages_to_convert, dpi=300, filename=None):
    if not os.path.exists(pdfpath):
        print("Erro: o diretório do arquivo PDF não existe.")
        return False
    
    try:
        dpi_zoom =  dpi / 72
        pdf_doc = pymupdf.open(pdfpath)

        if isinstance(pages_to_convert, range):
            for i in pages_to_convert:
                page = pdf_doc[i]
                page_img = page.get_pixmap(matrix=pymupdf.Matrix(dpi_zoom, dpi_zoom))
                page_img.save(f"{filename}{i + 1}.png")

        elif isinstance(pages_to_convert, int):
            for page in pdf_doc:
                page_img =  page.get_pixmap(matrix=pymupdf.Matrix(dpi_zoom, dpi_zoom))
                page_img.save(f"{filename}{page.number + 1}.png")

        print("Conversão finalizada com sucesso.")
        pdf_doc.close()
        return True
        
    except Exception as e:
        print(f"Erro durante a conversão: {str(e)}")
        return False

def parse_pages(input_str, pages):
    input_str = input_str.strip().upper()
    
    if input_str == "T":
        return pages
    
    if input_str.isdigit():
        page = int(input_str)
        if page > pages or page < 1:
            print("ERRO: Página escolhida fora do intervalo do documento.")
            return None
        return range(page - 1, page)
    
    if "-" in input_str:
        interval = input_str.split("-")
        
        if len (interval) == 2 and interval[0].isdigit() and interval[1].isdigit():
            start = int(interval[0]) - 1
            end = int(interval[1]) - 1

            if start < 0 or end < 0:
                print("Há valores negativos no seu intervalo. Digite novamente um intervalo válido.")
                return None
            
            if start > end:
                print("Sua página inicial é maior que a final. Intervalo inválido.")
                return None
            
            if end >= pages:
                print("O intervalo digitado ultrapassa o intervalo de páginas do documento.")
                return None
            
            return range(start, end + 1)
        else:
            print("ERRO: Intervalo inválido.")
            return None

def main():
    parser = argparse.ArgumentParser(description="Converte PDF em imagens.")
    parser.add_argument('pdfpath', help='Arquivo PDF de entrada (precisa estar na mesma pasta).')
    args = parser.parse_args()

    pdf_doc = pymupdf.open(args.pdfpath)
    pages = pdf_doc.page_count

    if pages > 1:
        print(f"Seu arquivo possui {pages} páginas.")
        choice = input("Quais páginas deseja converter? \n - Digite T para todas" \
                "\n - Uma única página da sua escolha" \
                "\n - Ou (X-Y) para um intervalo específico" \
                "\n - ")
        pages_to_convert = parse_pages(choice, pages) #Aqui chama a função parse_pages acima
        
        while pages_to_convert is None:
            choice = input("Quais páginas deseja converter? \n - Digite T para todas" \
                "\n - Uma única página da sua escolha"
                "\n - Ou (X-Y) para um intervalo específico" \
                "\n - ")
            pages_to_convert = parse_pages(choice, pages)

    file_name = os.path.splitext(os.path.basename(args.pdfpath))[0]

    map = {
        "1": 72,
        "2": 144,
        "3": 300
    }

    quality = input("Escolha a qualidade da imagem:\n1 - Baixa\n2 - Padrão\n3 - Alta\n")
    dpi = map.get(quality, 144)

    custom_name = input(f"Digite um nome para seu arquivo final, ou pressione ENTER para manter o nome do arquivo-mãe ({file_name}):\n")

    if not custom_name: 
        custom_name = file_name

    conv(args.pdfpath, pages_to_convert, dpi=dpi, filename=custom_name)

if __name__ == "__main__":
    main()