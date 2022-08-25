from PIL import Image

arquivo_imagem = Image.open(r".\imagemcolorida.png")

arquivo_imagem = arquivo_imagem.convert('L')

arquivo_imagem.save(r'.\imagempreto-e-branco.png')
