import os
import requests
from requests.auth import HTTPBasicAuth

arquivo = open('dados.txt', 'r')
try:
    variaveis = arquivo.read().split(';')
except:
    raise ValueError('Alguma Variavel nao foi encontrada')
arquivo.close()

listaModulosGC = variaveis[0].strip()
pasta = variaveis[1].strip()
tela = variaveis[2].strip()

cont = 0
listaDiretorios = []
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if '.tcKDTest' in arquivo:
            dir = (os.path.join(os.path.realpath(diretorio), arquivo))
            with open(dir, 'r', encoding='utf-8') as arq:
                if tela in arq.read():
                    listaDiretorios.append(diretorio)
                    cont += 1
            arq.close()
listaDiretorios = set(listaDiretorios)

listaTestes = []
for i in listaDiretorios:
    caminho = ''
    i = i.split('\\')
    for j in i[0:-1]:
        caminho = caminho + '\\' + j
    for dir, subpastas, arquivos in os.walk(caminho[1:]):
        for arquivo in arquivos:
            #if '.pjs' not in arquivo and '.mds' in arquivo:
            if i[-2][0:4].lower() in listaModulosGC:
                listaTestes.append(i[-2])
listaTestes = set(listaTestes)

print(f'A tela {tela} foi encontrada em {cont} Keywords')
print('Nos seguintes caminhos:')
for diretorio in listaDiretorios:
    print(diretorio)
print(f'Foram encontrados os seguintes testes:')
for teste in listaTestes:
    if teste[0:4].lower() == 'nfis':
        if requests.get(f'http://cit/view/TributarionFis/job/nFis%20-%20Firebird/job/Tributario-Firebird-{teste}',
                        auth = HTTPBasicAuth('testcomplete', '12345')):
            print(f'http://cit/view/TributarionFis/job/nFis%20-%20Firebird/job/Tributario-Firebird-{teste}')
    if teste[0:4].lower() == 'nfpa':
        if requests.get(f'http://cit/view/TributarionFpa/job/nFpa%20-%20Firebird/job/Tributario-Firebird-{teste}',
                        auth = HTTPBasicAuth('testcomplete', '12345')):
            print(f'http://cit/view/TributarionFpa/job/nFpa%20-%20Firebird/job/Tributario-Firebird-{teste}')


