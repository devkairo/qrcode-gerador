# Desenvolvido por Kairo Trzeciak
# https://github.com/devkairo/qrcode-gerador
import qrcode
import os
from PIL import Image
from colorama import init
from termcolor import colored

os.system('clear')

# CORES QRCODE
 
cores_qrcode = {
	'1': 'Red',
	'2': 'Blue',
	'3': 'Green',
	'4': 'Yellow',
	'5': 'Magenta'
}

# CORES EXIBIDAS NO TERMINAL

cores = {
	'1': 'on_red',
	'2': 'on_blue',
	'3': 'on_green',
	'4': 'on_yellow',
	'5': 'on_magenta'
}


print("\n[0] Sem cor/No Color")

for titulo,valor in cores.items():
	print("["+titulo+"] " + (colored('           ', 'white', valor)))


print("\n")
cor = input("Código da Cor (Color Code): ")

if (cor == "1"):
	cor = cores_qrcode.get("1")
elif (cor == "2"):
	cor = cores_qrcode.get("2")
elif (cor == "3"):
	cor = cores_qrcode.get("3")
elif (cor == "4"):
	cor = cores_qrcode.get("4")
elif (cor == "5"):
	cor = cores_qrcode.get("5")
else:
	cor = False

print("\n")
logo = input("Logo (S/N or Y/N): ")

if (logo == "S" or logo == "s" or logo == "Y" or logo == "y"):
	logo = True
	logo_caminho = input("Caminho da logotipo (Logo path): ")
else:
	logo = False
 


QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)


print("\n")
url_qrcode = input("URL (Use https://): ")

QRcode.add_data(url_qrcode)
QRcode.make()



QRimg = QRcode.make_image(
    fill_color=cor, back_color="white").convert('RGB')

 
if logo == True:
	
	Logo_link = logo_caminho
	logo = Image.open(Logo_link)
	basewidth = 100

	wpercent = (basewidth/float(logo.size[0]))
	hsize = int((float(logo.size[1])*float(wpercent)))
	logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
	pos = ((QRimg.size[0] - logo.size[0]) // 2,
	       (QRimg.size[1] - logo.size[1]) // 2)
	QRimg.paste(logo, pos)
 

QRimg.save('qrcode_gerado.png')


print('\n[!] QRCode generated successfully (qrcode_gerado.png)!') 
print('[!] QRCode gerado com sucesso! (qrcode_gerado.png)')	