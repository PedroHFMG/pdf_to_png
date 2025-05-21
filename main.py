import os
import sys
import time
import fitz

print(time.ctime())
print(os.getcwd())
print(os.path.dirname(os.path.realpath(__file__)))
print(os.path.splitext(os.path.basename(__file__))[0])

def conv(path, output_dir = None, dpi=300):
    if not os.path.exists(path):
        print("Erro: o diretório do arquivo PDF não existe.")
        return False
    
    output_dir = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.splitext(os.path.basename(path))[0]

    try:
        pdf_doc = fitz.open(path)
        for page in pdf_doc:
            page_img =  page.get_pixmap()
            page_img.save("page-%i.png" % page.number)
        
    except Exception as e:
        print(f"Erro durante a conversão: {str(e)}")
        return False
    
if __name__ == "__main__":
    conv("test.pdf")