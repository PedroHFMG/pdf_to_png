import os, sys, time, fitz, argparse

def conv(pdfpath, output_dir = None, dpi=300):
    if not os.path.exists(pdfpath):
        print("Erro: o diretório do arquivo PDF não existe.")
        return False
    
    output_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.splitext(os.path.basename(pdfpath))[0]

    try:
        pdf_doc = fitz.open(pdfpath)
        for page in pdf_doc:
            page_img =  page.get_pixmap(matrix=fitz.Matrix(2, 2))
            page_img.save("page-%i.png" % page.number)
        print("Conversão finalizada com sucesso.")
        return True
        
    except Exception as e:
        print(f"Erro durante a conversão: {str(e)}")
        return False
    
def main():
    parser = argparse.ArgumentParser(description="Converte PDF em imagens.")
    parser.add_argument('pdfpath', help='Arquivo PDF de entrada (precisa estar na mesma pasta).')

    args = parser.parse_args()

    conv(args.pdfpath)

if __name__ == "__main__":
    main()