# Programa que encontra dados escificos dentro de um arquivo
#		e salva no arquivo dados2y.txt
# Escrito por Alex G. Silva.
# Data de finalizacao: 02/04/2021.
# Modificado em 04/04/2021.
# No python 2 retire list(), mas deixe seu argumento.

y = list(map(str.split, open('eixo_x.dat'))) ; f = open ('dados2y.txt', 'w')
p = open ('dadoskkk.txt', 'w')
frase = "optimization completed"; frase2 = "Distance matrix (angstroms):"; k=0
nome_arquivo=["fd000.log", 'fd005.log', 'fd010.log', 'fd015.log', 'fd020.log', 'fd025.log', 
            'fd030.log', 'fd035.log', 'fd040.log', 'fd045.log', 'fd050.log', 'fd055.log', 'fd060.log', 
                'fd065.log', 'fd070.log', 'fd075.log', 'fd080.log', 'fd085.log', 'fd090.log', 'fd095.log', 
                    'fd100.log', 'fd105.log', 'fd110.log', 'fd115.log', 'fd120.log', 'fd125.log', 'fd130.log', 
                        'fd135.log', 'fd140.log', 'fd145.log', 'fd150.log', 'fd155.log', 'fd160.log', 'fd165.log', 
                            'fd170.log', 'fd175.log', 'fd180.log', 'fd185.log', 'fd190.log', 'fd195.log', 'fd200.log']
# Loop que varre o nome dos arquivos
for nome in nome_arquivo:
# Abertura dos arquivos:
    arqui = open(nome, "r")
    x=0
    # Varra o arquivo (arqui) linha por linha:
    for line in arqui:
        x=x+1
        # procurando a 'frase' em cada linha de arqui: 
        if frase in line.lower():
            #Coordenada eh o numero da linha no arquivo (arqui), em que a 'frase' foi encontrada
            #coordenada = x 
            #.readlines(): Return all lines in the file, as a list where each line is 
            #        an item in the list object
            lines = arqui.readlines() 
            print(frase + ' encontrada'+ ' no arquivo ' + nome)
            w=0
            
            #Varra lines de tras para frente:
            for i in reversed(lines):
                p.write(i)
                if frase2 in i:
                    #print(w)
                    arquivo = list(map(str.split, open(nome)))
                    f.write(y[k][0])
                    f.write('	')
                    f.write(arquivo[len(arquivo) - w+6][6])#a
                    f.write('	')
                    f.write(arquivo[len(arquivo) - w+5][5])#b
                    f.write('	')
                    f.write(arquivo[len(arquivo) - w+4][4])#c
                    f.write('	')
                    f.write(arquivo[len(arquivo) - w+15][4])#d
                    f.write('	')
                    f.write(arquivo[len(arquivo) - w+62][6])#e
                    f.write('	')
                    f.write(arquivo[len(arquivo) - w+79][3])#f
                    f.write('	')
                    f.write(arquivo[len(arquivo) - w+80][5])#g
                    f.write('	')
                    f.write(arquivo[len(arquivo) - w+82][6])#h
                    f.write('	')
                    f.write(arquivo[len(arquivo) - w+96][3])#i
                    f.write('	')
                    f.write(arquivo[len(arquivo) - w+104][2])#j
                    f.write('	\n')                    
                    break            
                w=w+1         
    k=k+1
arqui.close()
print("programa finalizado")
