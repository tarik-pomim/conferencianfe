# EXPERIMENTANDO COM LEITURA DE ARQUIVOS EM UMA PASTA

#PROCURA ARQUIVOS NA PASTA E DELETA:
import glob
import os
DOTNFE = glob.glob('c:/danfe/CONFERENCIA/*-nfe.xml')
for file in DOTNFE:
    os.remove(file)
    print(f'Aquivo {file} removidos com sucesso!')

#COLOCANDO OS ARQUIVOS EM UMA LISTA:
ARQNFE = glob.glob('c:/danfe/CONFERENCIA/*.xml')
#print(f'Os arquivos crus são: {ARQNFE}')

#EXTRAINDO APENAS A CHAVE DE ACESSO DE 44 DIGITOS:
#for item in ARQNFE:
#    CHAVE44 = item[9:53] #PEGA SÓ A CHAVE DE ACESSO 44 DIGITOS
#    print(CHAVE44)

#EXTRAINDO APENAS O NUMERO DA NFE:
NUM055STR = []
NUM065STR = []
for item in ARQNFE:
    if item[41:43] == '55':
        NUM055STR.append(item[46:55]) #PEGA SÓ O NUMERO DA NOTA FISCAL E COLOCA NA LISTA DE NFE NUM055STR
        NUM055STR.sort()
    if item[41:43] == '65':
        NUM065STR.append(item[46:55]) #PEGA SÓ O NUMERO DA NOTA FISCAL E COLOCA NA LISTA DE CUPOM NUM065STR
        NUM065STR.sort()

#CONVERTE A LISTA DE STR PARA INT:
NUM055INT = [int(i) for i in NUM055STR]
NUM065INT = [int(i) for i in NUM065STR]

#SEPARAR OS DUPLICADOS EM UMA SEGUNDA LISTA, QUE SERÁ A LISTA DE EVENTOS DE NFE:
EVENTOS055 = set([x for x in NUM055INT if NUM055INT.count(x) > 1]) #NFE
EVENTOS065 = set([x for x in NUM065INT if NUM065INT.count(x) > 1]) #CUPOM
if EVENTOS055 == set():
    EVENTOS055 = 'Nenhum evento encontrado'
if EVENTOS065 == set():
    EVENTOS065 = 'Nenhum evento encontrado'

#CRIAR UMA LISTA SEM OS DUPLICADOS:
SET055INT = list(set(NUM055INT)) #NFE
SET065INT = list(set(NUM065INT)) #CUPOM

#CRIAR UMA LISTA COM A ORDEM CORRETA DA NUMERAÇÃO:
#---------- NFE ----------
LISTAGERAL055 = []
if SET055INT == []:
    print('Modelo 55 não encontrado!')
else:
    for y in range(0, (SET055INT[-1] - SET055INT[0])):
        LISTAGERAL055.append((SET055INT[0] + y))
    LISTAGERAL055.append(LISTAGERAL055[-1] + 1)
#---------- CUPOM ---------
LISTAGERAL065 = []
if SET065INT == []:
    print('Modelo 65 não encontrado!')
else:
    for y in range(0, (SET065INT[-1] - SET065INT[0])):
        LISTAGERAL065.append((SET065INT[0] + y))
    LISTAGERAL065.append(LISTAGERAL065[-1] + 1)

#COMPARAR LISTAGERAL, QUE CONTEM TODAS AS NUMERAÇÕES, COM SETNFEINT, QUE CONTEM A LISTA DE NFEs EXISTENTES.
#---------- NFE ----------
FALTANTES055 = []
for y in range(len(LISTAGERAL055)):
    if LISTAGERAL055[y] not in SET055INT:
        FALTANTES055.append(LISTAGERAL055[y])
#---------- CUPOM ---------
FALTANTES065 = []
for y in range(len(LISTAGERAL065)):
    if LISTAGERAL065[y] not in SET065INT:
        FALTANTES065.append(LISTAGERAL065[y])

#INFORMAÇÕES QUE TEMOS ATÉ AGORA:
# ---------- NFE ----------
if len(SET055INT) != 0:
    print('=' *80)
    print('{:^80}'.format('- VERIFICAÇÃO DE NF-es -'))
    print('-' *80)
    print(f'Numero da NF-e inicial: {SET055INT[0]}')
    print(f'Numero da NF-e final: {SET055INT[-1]}')
    print(f'NF-es que apresentam eventos de cancelamento e/ou inutilização: {EVENTOS055}')
    print(f'Quantas NF-e a lista deveria ter: {len(LISTAGERAL055)}')
    print(f'Quantidade de NF-e presentes lista: {len(SET055INT)}')
    print(f'Quantidade de NF-e que faltam na lista: {len(FALTANTES055)}')
    print(f'*** NOTAS FISCAIS (NF-e 55) QUE ESTÃO FALTANDO *** --->>>>> {FALTANTES055}')
    print('=' *80)
else:
    print('--- MODELO 55 NÃO ENCONTRADO ---')
# ---------- CUPOM ----------
if len(SET065INT) != 0:
    print('{:^80}'.format('- VERIFICAÇÃO DE CUMPOM (NFC-e) -'))
    print('-' *80)
    print(f'Numero do Cupom inicial: {SET065INT[0]}')
    print(f'Numero do Cupom final: {SET065INT[-1]}')
    print(f'Cupons que apresentam eventos de cancelamento e/ou inutilização: {EVENTOS065}')
    print(f'Quantos Cupons a lista deveria ter: {len(LISTAGERAL065)}')
    print(f'Quantidade de Cupons presentes lista: {len(SET065INT)}')
    print(f'Quantidade de Cupons que faltam na lista: {len(FALTANTES065)}')
    print(f'*** CUPONS FISCAIS (NFC-e 65) QUE ESTÃO FALTANDO *** --->>>>> {FALTANTES065}')
    print('=' *80)
    print('{:^80}'.format('- FINAL DAS VALIDAÇÕES -'))
else:
    print('--- MODELO 65 NÃO ENCONTRADO ---')








