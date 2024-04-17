print('\033[1;33m=-\033[m'*15)
print('\033[1;33m  MEDIDOR DE VELOCIDADE')
print('\033[1;33m=-\033[m'*15)
tamanho = float(input('\033[1mTamanho do arquivo (Mb): '))
velocidade = float(input('Velocidade de internet (Mbps): '))
tempo = (tamanho*8)/velocidade
print(f'Tempo aproximado de download: ')
print(f'\033[1;32m{(tempo//60):.0f}\033[m \033[1mminutos e \033[1;32m{(tempo%60):.0f}\033[m \033[1msegundos.')