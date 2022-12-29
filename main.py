import os

arq = open('dados.txt', 'r')
try:
    for i in arq:
        if 'MODULOS:' in i:
            listaModulosGC = i
        if 'PASTARAIZ:' in i:
            pasta = i
        if 'TELAPESQUISAR:' in i:
            tela = i
except:
    raise ValueError('Alguma Variavel nao foi encontrada')
arq.close()

listaModulosGC = listaModulosGC[8:].strip()
pasta = pasta[10:].strip()
tela= tela[14:].strip()


"""listaModulosGC = ['nctb', 'nctr', 'nfin', 'ngem', 'nfis', 'narq', 'ninv', 'npat',
                  'nfpa', 'nlea', 'norg', 'npro', 'nstt', 'ntce']

pasta = input('Caminho Pesquisar: ')
if len(pasta) == 0:
    pasta = ('D:\\workspace\\TestesTributario')
tela = input('Tela Pesquisar: ')"""

listaDiretorios = []
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        if '.tcKDTest' in arquivo:
            dir = (os.path.join(os.path.realpath(diretorio), arquivo))
            with open(dir, 'r', encoding='utf-8') as arq:
                if tela in arq.read():
                    listaDiretorios.append(diretorio)
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
            if '.pjs' not in arquivo and '.mds' in arquivo:
                if i[-2][0:4].lower() in listaModulosGC:
                    listaTestes.append(i[-2])
listaTestes = set(listaTestes)

print(f'Testes em Firebird:')
for teste in listaTestes:
    if teste[0:4].lower() == 'nfis':
        print(f'http://cit/view/TributarionFis/job/nFis%20-%20Firebird/job/Tributario-Firebird-{teste}')
    if teste[0:4].lower() == 'nfpa':
        print(f'http://cit/view/TributarionFpa/job/nFpa%20-%20Firebird/job/Tributario-Firebird-{teste}')



