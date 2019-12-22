import csv

lista_utentes=[]

def encontrar_tempo_lst(lst,elem):
	for item in lst:
		if item[0] == elem:
			return True
	return False


with open('tabela_utentes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #print(f' {", ".join(row)}')
            line_count += 1
        else:
            #print(f'  U- {row[0]}   CH- {row[1]}   TF1- {row[2]}   TF2- {row[3]}   RF2- {row[4]}   A- {row[5]}   TF3- {row[6]}')
            utente_lst=[]
            utente_lst.append(row[0])
            utente_lst.append(row[1])
            utente_lst.append(row[2])
            utente_lst.append(row[3])
            utente_lst.append(row[4])
            utente_lst.append(row[5])
            utente_lst.append(row[6])
            lista_utentes.append(utente_lst)
            line_count += 1
print(f' -> {line_count} Utentes passarão pelo Sistema')
#print(lista_utentes)
with open('sistema.csv', mode='w') as tabela_sistema:
	fieldnames = ['CLOCK', 'TIPO EVENTO', 'UTENTE', 'PROX_CHEGADA', 'LISTA_F1', 'ESTADO_F1', 'PARTIDA_F1', 'LISTA_F2A', 'ESTADO_F2A1', 'PARTIDA_F2A1', 'ESTADO_F2A2', 'PARTIDA_F2A2', 'LISTA_F2B', 'ESTADO_F2B1', 'PARTIDA_F2B1', 'ESTADO_F2B2', 'PARTIDA_F2B2', 'LISTA_F2C', 'ESTADO_F2C', 'PARTIDA_F2C']
	sistema_writer = csv.DictWriter(tabela_sistema , fieldnames=fieldnames)

	sistema_writer.writeheader()
#Intanciar variáveis

	CLOCK=0                                          #CLOCK
	tempo_final=8*60*60                              #28800 seg
	TIPO_EVENTO="INICIO"                             #Tipo de Evento = INICIO
	LISTA_EVENTO=[(0,TIPO_EVENTO,"-")]                     #Lista de Eventos, que é um dicionario
	LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
	#print(LISTA_EVENTO)
	UTENTE = "-"
	PROX_CHEGADA = 0
	C=CLOCK
	PROX_UTENTE="-"
	INDEX_PROX_UTENTE=0

				
	TEMPO_F1="-"						#FASE 1

	ESTADO_F1="LIVRE"
	PARTIDA_F1="-"
	LISTA_F1=[]
				
	TEMPO_F2="-"						#FASE 2
										#ASSUNTO A COM 2 BALCOES
	ESTADO_F2A1="LIVRE"
	ESTADO_F2A2="LIVRE"
	PARTIDA_F2A1="-"
	PARTIDA_F2A2="-"
	LISTA_F2A=[]
										#ASSUNTO B COM 2 BALCOES
	ESTADO_F2B1="LIVRE"
	ESTADO_F2B2="LIVRE"
	PARTIDA_F2B1="-"
	PARTIDA_F2B2="-"
	LISTA_F2B=[]
										#ASSUNTO C COM 1 BALCOES
	ESTADO_F2C="LIVRE"
	PARTIDA_F2C="-"
	LISTA_F2C=[]
				
	TEMPO_F3="-"						#FASE 3

	ESTADO_F3="LIVRE"
	PARTIDA_F3="-"
	LISTA_F3=[]

	
	print("ciclo")
	

	while (C < tempo_final) or (len(LISTA_EVENTO) != 0):          #até o clock acabar ou até que não haja mais cientes para atender
		if encontrar_tempo_lst(LISTA_EVENTO,C):
			LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
			
			EVENTO = LISTA_EVENTO[0]
			UTENTE = EVENTO[2]

			if  ((INDEX_PROX_UTENTE < line_count-1) and (EVENTO[1] == "CH" or EVENTO[1] == "INICIO")) and  (PROX_CHEGADA != lista_utentes[INDEX_PROX_UTENTE][1] or PROX_CHEGADA == C) :
				PROX_UTENTE=lista_utentes[INDEX_PROX_UTENTE]
				PROX_CHEGADA=PROX_UTENTE[1]
				PROX=PROX_UTENTE[0]
				LISTA_EVENTO.append((int(PROX_CHEGADA),"CH",PROX))
				INDEX_PROX_UTENTE += 1


			if (EVENTO[1] == "PF2A1") :
				ESTADO_F2A1="LIVRE"
				PARTIDA_F2A1 = "-"
				LISTA_F2A.sort(key=lambda tup: tup[0])
				if(len(LISTA_F2A) != 0):
					EVENTO = LISTA_F2A.pop(0)
					ESTADO_F2A1="OCUPADO"
					PARTIDA_F2A1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][2])
					LISTA_EVENTO.append((int(PARTIDA_F2A1),"PF2A1",EVENTO[2]))

			if (EVENTO[1] == "PF2A2") :
				ESTADO_F2A2="LIVRE"
				PARTIDA_F2A2 = "-"
				LISTA_F2A.sort(key=lambda tup: tup[0])
				if(len(LISTA_F2A) != 0):
					EVENTO = LISTA_F2A.pop(0)
					ESTADO_F2A2="OCUPADO"
					PARTIDA_F2A2 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][2])
					LISTA_EVENTO.append((int(PARTIDA_F2A2),"PF2A2",EVENTO[2]))

			if (EVENTO[1] == "PF2B1") :
				ESTADO_F2B1="LIVRE"
				PARTIDA_F2B1 = "-"
				LISTA_F2B.sort(key=lambda tup: tup[0])
				if(len(LISTA_F2B) != 0):
					EVENTO = LISTA_F2B.pop(0)
					ESTADO_F2B1="OCUPADO"
					PARTIDA_F2B1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][2])
					LISTA_EVENTO.append((int(PARTIDA_F2B1),"PF2B1",EVENTO[2]))

			if (EVENTO[1] == "PF2B2") :
				ESTADO_F2B2="LIVRE"
				PARTIDA_F2B2 = "-"
				LISTA_F2B.sort(key=lambda tup: tup[0])
				if(len(LISTA_F2B) != 0):
					EVENTO = LISTA_F2B.pop(0)
					ESTADO_F2B2="OCUPADO"
					PARTIDA_F2B2 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][2])
					LISTA_EVENTO.append((int(PARTIDA_F2B2),"PF2B2",EVENTO[2]))

			if (EVENTO[1] == "PF2C") :
				ESTADO_F2C="LIVRE"
				PARTIDA_F2C = "-"
				LISTA_F2C.sort(key=lambda tup: tup[0])
				if(len(LISTA_F2C) != 0):
					EVENTO = LISTA_F2C.pop(0)
					ESTADO_F2C="OCUPADO"
					PARTIDA_F2C = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][2])
					LISTA_EVENTO.append((int(PARTIDA_F2C),"PF2C",EVENTO[2]))



			if (EVENTO[1] == "PF1") :
				ESTADO_F1="LIVRE"
				PARTIDA_F1 = "-"
				LISTA_F1.sort(key=lambda tup: tup[0])
				if(len(LISTA_F1) != 0):
					EVENTO = LISTA_F1.pop(0)
					ESTADO_F1="OCUPADO"
					PARTIDA_F1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][2])
					LISTA_EVENTO.append((int(PARTIDA_F1),"PF1",EVENTO[2]))
				if (lista_utentes[int(EVENTO[2].split(" ")[1])-1][5] == "A") :
					if (ESTADO_F2A1 == "LIVRE"):
						ESTADO_F2A1="OCUPADO"
						PARTIDA_F2A1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
						LISTA_EVENTO.append((int(PARTIDA_F2A1),"PF2A1",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					elif (ESTADO_F2A2 == "LIVRE") :
						ESTADO_F2A2="OCUPADO"
						PARTIDA_F2A2 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
						LISTA_EVENTO.append((int(PARTIDA_F2A2),"PF2A2",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F2A.append((int(C),"PF2A",EVENTO[2]))
						LISTA_F2A = sorted(LISTA_F2B, key=lambda element: (element[2], element[0]))
				elif (lista_utentes[int(EVENTO[2].split(" ")[1])-1][5] == "B") :
					if (ESTADO_F2B1 == "LIVRE"):
						ESTADO_F2B1="OCUPADO"
						PARTIDA_F2B1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
						LISTA_EVENTO.append((int(PARTIDA_F2B1),"PF2B1",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					elif (ESTADO_F2B2 == "LIVRE") :
						ESTADO_F2B2="OCUPADO"
						PARTIDA_F2B2 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
						LISTA_EVENTO.append((int(PARTIDA_F2B2),"PF2B2",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F2B.append((int(C),"PF2B",EVENTO[2]))
						LISTA_F2B = sorted(LISTA_F2B, key=lambda element: (element[2], element[0]))
				elif (lista_utentes[int(EVENTO[2].split(" ")[1])-1][5] == "C") :
					if (ESTADO_F2C == "LIVRE"):
						ESTADO_F2C="OCUPADO"
						PARTIDA_F2C = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
						LISTA_EVENTO.append((int(PARTIDA_F2C),"PF2C",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F2C.append((int(C),"PF2C",EVENTO[2]))
						LISTA_F2C = sorted(LISTA_F2C, key=lambda element: (element[2], element[0]))
				else:        #ASSUNTO -, nao passa por esta fase, vai para a fase 3
					if (ESTADO_F3 == "LIVRE"):
						ESTADO_F3="OCUPADO"
						PARTIDA_F3 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
						LISTA_EVENTO.append((int(PARTIDA_F3),"PF3",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F3.append((int(C),"PF3",EVENTO[2]))
						LISTA_F3 = sorted(LISTA_F3, key=lambda element: (element[2], element[0]))

					

			if (EVENTO[1] == "CH") :
				if (ESTADO_F1 == "LIVRE"):
					ESTADO_F1="OCUPADO"
					PARTIDA_F1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][2])
					LISTA_EVENTO.append((int(PARTIDA_F1),"PF1",EVENTO[2]))
					LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
				else :
					LISTA_F1.append((int(C),"PF1",EVENTO[2]))
					LISTA_F1 = sorted(LISTA_F1, key=lambda element: (element[2], element[0]))

				


			sistema_writer.writerow({'CLOCK' : C, 'TIPO EVENTO' : EVENTO[1] ,'UTENTE' : UTENTE, 'PROX_CHEGADA' : PROX_CHEGADA, 'LISTA_F1' : LISTA_F1, 'ESTADO_F1' : ESTADO_F1, 'PARTIDA_F1' : PARTIDA_F1, 'LISTA_F2A' : LISTA_F2A, 'ESTADO_F2A1' : ESTADO_F2A1, 'PARTIDA_F2A1' : PARTIDA_F2A1, 'ESTADO_F2A2' : ESTADO_F2A2, 'PARTIDA_F2A2' : PARTIDA_F2A2, 'LISTA_F2B' : LISTA_F2B, 'ESTADO_F2B1' : ESTADO_F2B1, 'PARTIDA_F2B1' : PARTIDA_F2B1, 'ESTADO_F2B2' : ESTADO_F2B2, 'PARTIDA_F2B2' : PARTIDA_F2B2, 'LISTA_F2C' : LISTA_F2C, 'ESTADO_F2C' : ESTADO_F2C, 'PARTIDA_F2C' : PARTIDA_F2C})
			LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
			print(f'\nCLOCK- {C}')
			print(f'1-INSERE- {LISTA_EVENTO}')

			LISTA_EVENTO.pop(0)
			print(f'2-REMOVE- {LISTA_EVENTO}')
			print(f'F1 - {LISTA_F1}')
			print(f'F2A- {LISTA_F2A}')
			print(f'F2B- {LISTA_F2B}')
			print(f'F2C- {LISTA_F2C}')

			
				
		

			

			LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
			
		else:
			C += 1
		#print(C)