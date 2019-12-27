import csv

lista_utentes=[]

def encontrar_tempo_lst(lst,elem):
	for item in lst:
		if item[0] == elem:
			return True
	return False

file_to_read = 'tabela_utentes.csv'
file_to_write= 'sistema.csv'
file_to_stat= 'estatisticas.txt'

with open(file_to_read) as csv_file:
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
with open(file_to_write, mode='w') as tabela_sistema:
	fieldnames = ['CLOCK', 'TIPO EVENTO', 'UTENTE', 'PROX_CHEGADA', 'LISTA_F1', 'ESTADO_F1', 'PARTIDA_F1', 'LISTA_F2A', 'ESTADO_F2A1', 'PARTIDA_F2A1', 'ESTADO_F2A2', 'PARTIDA_F2A2', 'LISTA_F2B', 'ESTADO_F2B1', 'PARTIDA_F2B1', 'ESTADO_F2B2', 'PARTIDA_F2B2', 'LISTA_F2C', 'ESTADO_F2C', 'PARTIDA_F2C', 'LISTA_F3', 'ESTADO_F3', 'PARTIDA_F3','ESPERA_TOTAL']
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

										#ESTATISTICAS

	ESPERA_TOTAL=0

	T1_TAXA_OCUP_A1=0
	T1_TAXA_OCUP_A2=0
	T1_TAXA_OCUP_B1=0
	T1_TAXA_OCUP_B2=0
	T1_TAXA_OCUP_C=0

	T2_TAXA_OCUP_A1=0
	T2_TAXA_OCUP_A2=0
	T2_TAXA_OCUP_B1=0
	T2_TAXA_OCUP_B2=0
	T2_TAXA_OCUP_C=0

	T3_TAXA_OCUP_A1=0
	T3_TAXA_OCUP_A2=0
	T3_TAXA_OCUP_B1=0
	T3_TAXA_OCUP_B2=0
	T3_TAXA_OCUP_C=0

	T4_TAXA_OCUP_A1=0
	T4_TAXA_OCUP_A2=0
	T4_TAXA_OCUP_B1=0
	T4_TAXA_OCUP_B2=0
	T4_TAXA_OCUP_C=0

	TEMPO_ESPERA=0
	T1_TEMPO_ESPERA_MAX=0
	T1_TEMPO_ESPERA_MIN=999999
	T1_TEMPO_ESPERA_MED=0

	T2_TEMPO_ESPERA_MAX=0
	T2_TEMPO_ESPERA_MIN=999999
	T2_TEMPO_ESPERA_MED=0

	T3_TEMPO_ESPERA_MAX=0
	T3_TEMPO_ESPERA_MIN=999999
	T3_TEMPO_ESPERA_MED=0

	T4_TEMPO_ESPERA_MAX=0
	T4_TEMPO_ESPERA_MIN=999999
	T4_TEMPO_ESPERA_MED=0

	TT_TEMPO_ESPERA_MAX=0
	TT_TEMPO_ESPERA_MIN=999999
	TT_TEMPO_ESPERA_MED=0

	T1_CONT_ESPERA=0
	T2_CONT_ESPERA=0
	T3_CONT_ESPERA=0
	T4_CONT_ESPERA=0

	T1_TEMPO_ESPERA=0
	T2_TEMPO_ESPERA=0
	T3_TEMPO_ESPERA=0
	T4_TEMPO_ESPERA=0
	
	CONT_ESPERA=0


	LST_TEMPOS_ESPERA=[]

	
	print("ciclo")
	

	while (C < tempo_final) or (len(LISTA_EVENTO) != 0):          #até o clock acabar ou até que não haja mais cientes para atender
		TEMPO_ESPERA=0

		if encontrar_tempo_lst(LISTA_EVENTO,C):
			LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))

			TEMPO_ESPERA=0

			EVENTO = LISTA_EVENTO[0]
			UTENTE = EVENTO[2]

			if  ((INDEX_PROX_UTENTE < line_count-1) and (EVENTO[1] == "CH" or EVENTO[1] == "INICIO")) and  (int(PROX_CHEGADA) <= C or PROX_CHEGADA != lista_utentes[INDEX_PROX_UTENTE][1]) :
				PROX_UTENTE=lista_utentes[INDEX_PROX_UTENTE]
				PROX_CHEGADA=PROX_UTENTE[1]
				PROX=PROX_UTENTE[0]
				LISTA_EVENTO.append((int(PROX_CHEGADA),"CH",PROX))
				LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
				EVENTO = LISTA_EVENTO[0]
				UTENTE = EVENTO[2]
				INDEX_PROX_UTENTE += 1

			if (EVENTO[1] == "PF3") :
				ESTADO_F3="LIVRE"
				PARTIDA_F3 = "-"
				LISTA_F3 = sorted(LISTA_F3, key=lambda element: (element[2], element[0]))
				if(len(LISTA_F3) != 0):
					EVENTO = LISTA_F3.pop(0)
					ESTADO_F3="OCUPADO"
					TEMPO_ESPERA = (C-int(EVENTO[0]))
					ESPERA_TOTAL=ESPERA_TOTAL+TEMPO_ESPERA
					if(TEMPO_ESPERA != 0) :
						LST_TEMPOS_ESPERA.append(TEMPO_ESPERA)
						CONT_ESPERA += 1
					PARTIDA_F3 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6])
					LISTA_EVENTO.append((int(PARTIDA_F3),"PF3",EVENTO[2]))
					LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
#pode estra sujeito a alteração
				if (lista_utentes[int(EVENTO[2].split(" ")[1])-1][4] == "SIM"):
					lista_utentes[int(EVENTO[2].split(" ")[1])-1][4] = "NAO"
					lista_utentes[int(EVENTO[2].split(" ")[1])-1][6] = 0
					if (lista_utentes[int(EVENTO[2].split(" ")[1])-1][5] == "A") :
						print(f'valor do assunto A {lista_utentes[int(EVENTO[2].split(" ")[1])-1][5]}')
						if (ESTADO_F2A1 == "LIVRE"):
							ESTADO_F2A1="OCUPADO"
							PARTIDA_F2A1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
							LISTA_EVENTO.append((int(PARTIDA_F2A1),"PF2A1","Q "+EVENTO[2].split(" ")[1]))
							LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
						elif (ESTADO_F2A2 == "LIVRE") :
							ESTADO_F2A2="OCUPADO"
							PARTIDA_F2A2 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
							LISTA_EVENTO.append((int(PARTIDA_F2A2),"PF2A2","Q "+EVENTO[2].split(" ")[1]))
							LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
						else:
							LISTA_F2A.append((int(C),"PF2A","Q "+EVENTO[2].split(" ")[1]))
							LISTA_F2A = sorted(LISTA_F2A, key=lambda element: (element[2], element[0]))
					elif (lista_utentes[int(EVENTO[2].split(" ")[1])-1][5] == "B") :
						print(f'valor do assunto B {lista_utentes[int(EVENTO[2].split(" ")[1])-1][5]}')
						if (ESTADO_F2B1 == "LIVRE"):
							ESTADO_F2B1="OCUPADO"
							PARTIDA_F2B1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
							LISTA_EVENTO.append((int(PARTIDA_F2B1),"PF2B1","Q "+EVENTO[2].split(" ")[1]))
							LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
						elif (ESTADO_F2B2 == "LIVRE") :
							ESTADO_F2B2="OCUPADO"
							PARTIDA_F2B2 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
							LISTA_EVENTO.append((int(PARTIDA_F2B2),"PF2B2","Q "+EVENTO[2].split(" ")[1]))
							LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
						else:
							LISTA_F2B.append((int(C),"PF2B","Q "+EVENTO[2].split(" ")[1]))
							LISTA_F2B = sorted(LISTA_F2B, key=lambda element: (element[2], element[0]))
					elif (lista_utentes[int(EVENTO[2].split(" ")[1])-1][5] == "C") :
						print(f'valor do assunto C {lista_utentes[int(EVENTO[2].split(" ")[1])-1][5]}')
						if (ESTADO_F2C == "LIVRE"):
							ESTADO_F2C="OCUPADO"
							PARTIDA_F2C = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
							LISTA_EVENTO.append((int(PARTIDA_F2C),"PF2C","Q "+EVENTO[2].split(" ")[1]))
							LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
						else:
							LISTA_F2C.append((int(C),"PF2C","Q "+EVENTO[2].split(" ")[1]))
							LISTA_F2C = sorted(LISTA_F2C, key=lambda element: (element[2], element[0]))
					else:        #ASSUNTO -, nao passa por esta fase, vai para a fase 3
						print("alguem saio do sistema")

			elif (EVENTO[1] == "PF2A1") :
				ESTADO_F2A1="LIVRE"
				PARTIDA_F2A1 = "-"
				LISTA_F2A = sorted(LISTA_F2A, key=lambda element: (element[2], element[0]))

				if(int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6]) != 0):   #se o tempo da fase 3 for diferente de zero, vai para a fase 3 isto é feito sempre que sai da fase 2
				
					if (ESTADO_F3 == "LIVRE"):
						ESTADO_F3="OCUPADO"
						PARTIDA_F3 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6])
						LISTA_EVENTO.append((int(PARTIDA_F3),"PF3",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F3.append((int(C),"PF3",EVENTO[2]))
						LISTA_F3 = sorted(LISTA_F3, key=lambda element: (element[2], element[0]))

				if(len(LISTA_F2A) != 0):
					EVENTO = LISTA_F2A.pop(0)
					ESTADO_F2A1="OCUPADO"
					TEMPO_ESPERA = (C-int(EVENTO[0]))
					ESPERA_TOTAL=ESPERA_TOTAL+TEMPO_ESPERA
					if(TEMPO_ESPERA != 0) :
						LST_TEMPOS_ESPERA.append(TEMPO_ESPERA)
						CONT_ESPERA += 1
					PARTIDA_F2A1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
					LISTA_EVENTO.append((int(PARTIDA_F2A1),"PF2A1",EVENTO[2]))
					LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))


			elif (EVENTO[1] == "PF2A2") :
				ESTADO_F2A2="LIVRE"
				PARTIDA_F2A2 = "-"
				LISTA_F2A = sorted(LISTA_F2A, key=lambda element: (element[2], element[0]))
				
				if(int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6]) != 0):

					if (ESTADO_F3 == "LIVRE"):
						ESTADO_F3="OCUPADO"
						PARTIDA_F3 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6])
						LISTA_EVENTO.append((int(PARTIDA_F3),"PF3",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F3.append((int(C),"PF3",EVENTO[2]))
						LISTA_F3 = sorted(LISTA_F3, key=lambda element: (element[2], element[0]))

				if(len(LISTA_F2A) != 0):
					EVENTO = LISTA_F2A.pop(0)
					ESTADO_F2A2="OCUPADO"
					TEMPO_ESPERA = (C-int(EVENTO[0]))
					ESPERA_TOTAL=ESPERA_TOTAL+TEMPO_ESPERA
					if(TEMPO_ESPERA != 0) :
						LST_TEMPOS_ESPERA.append(TEMPO_ESPERA)
						CONT_ESPERA += 1
					PARTIDA_F2A2 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
					LISTA_EVENTO.append((int(PARTIDA_F2A2),"PF2A2",EVENTO[2]))
					LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))

			elif (EVENTO[1] == "PF2B1") :
				ESTADO_F2B1="LIVRE"
				PARTIDA_F2B1 = "-"
				LISTA_F2B = sorted(LISTA_F2B, key=lambda element: (element[2], element[0]))
				
				if(int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6]) != 0):

					if (ESTADO_F3 == "LIVRE"):
						ESTADO_F3="OCUPADO"
						PARTIDA_F3 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6])
						LISTA_EVENTO.append((int(PARTIDA_F3),"PF3",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F3.append((int(C),"PF3",EVENTO[2]))
						LISTA_F3 = sorted(LISTA_F3, key=lambda element: (element[2], element[0]))

				if(len(LISTA_F2B) != 0):
					EVENTO = LISTA_F2B.pop(0)
					ESTADO_F2B1="OCUPADO"
					ESPERA_TOTAL=ESPERA_TOTAL+(C-int(EVENTO[0]))
					if(TEMPO_ESPERA != 0) :
						LST_TEMPOS_ESPERA.append(TEMPO_ESPERA)
						CONT_ESPERA += 1
					PARTIDA_F2B1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
					LISTA_EVENTO.append((int(PARTIDA_F2B1),"PF2B1",EVENTO[2]))
					LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))

			elif (EVENTO[1] == "PF2B2") :
				ESTADO_F2B2="LIVRE"
				PARTIDA_F2B2 = "-"
				LISTA_F2B = sorted(LISTA_F2B, key=lambda element: (element[2], element[0]))
				
				if(int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6]) != 0):

					if (ESTADO_F3 == "LIVRE"):
						ESTADO_F3="OCUPADO"
						PARTIDA_F3 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6])
						LISTA_EVENTO.append((int(PARTIDA_F3),"PF3",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F3.append((int(C),"PF3",EVENTO[2]))
						LISTA_F3 = sorted(LISTA_F3, key=lambda element: (element[2], element[0]))

				if(len(LISTA_F2B) != 0):
					EVENTO = LISTA_F2B.pop(0)
					ESTADO_F2B2="OCUPADO"
					TEMPO_ESPERA = (C-int(EVENTO[0]))
					ESPERA_TOTAL=ESPERA_TOTAL+TEMPO_ESPERA
					if(TEMPO_ESPERA != 0) :
						LST_TEMPOS_ESPERA.append(TEMPO_ESPERA)
						CONT_ESPERA += 1
					PARTIDA_F2B2 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
					LISTA_EVENTO.append((int(PARTIDA_F2B2),"PF2B2",EVENTO[2]))
					LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))


			elif (EVENTO[1] == "PF2C") :
				ESTADO_F2C="LIVRE"
				PARTIDA_F2C = "-"
				LISTA_F2C = sorted(LISTA_F2C, key=lambda element: (element[2], element[0]))
				
				if(int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6]) != 0):

					if (ESTADO_F3 == "LIVRE"):
						ESTADO_F3="OCUPADO"
						PARTIDA_F3 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6])
						LISTA_EVENTO.append((int(PARTIDA_F3),"PF3",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F3.append((int(C),"PF3",EVENTO[2]))
						LISTA_F3 = sorted(LISTA_F3, key=lambda element: (element[2], element[0]))

				if(len(LISTA_F2C) != 0):
					EVENTO = LISTA_F2C.pop(0)
					ESTADO_F2C="OCUPADO"
					TEMPO_ESPERA = (C-int(EVENTO[0]))
					ESPERA_TOTAL=ESPERA_TOTAL+TEMPO_ESPERA
					if(TEMPO_ESPERA != 0) :
						LST_TEMPOS_ESPERA.append(TEMPO_ESPERA)
						CONT_ESPERA += 1
					PARTIDA_F2C = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
					LISTA_EVENTO.append((int(PARTIDA_F2C),"PF2C",EVENTO[2]))
					LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))



			elif (EVENTO[1] == "PF1") :
				ESTADO_F1="LIVRE"
				PARTIDA_F1 = "-"
				LISTA_F1.sort(key=lambda tup: tup[0])
				
				if (lista_utentes[int(EVENTO[2].split(" ")[1])-1][5] == "A") :
					print(f'valor do assunto A {lista_utentes[int(EVENTO[2].split(" ")[1])-1][5]}')
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
						LISTA_F2A = sorted(LISTA_F2A, key=lambda element: (element[2], element[0]))
				elif (lista_utentes[int(EVENTO[2].split(" ")[1])-1][5] == "B") :
					print(f'valor do assunto B {lista_utentes[int(EVENTO[2].split(" ")[1])-1][5]}')
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
					print(f'valor do assunto C {lista_utentes[int(EVENTO[2].split(" ")[1])-1][5]}')
					if (ESTADO_F2C == "LIVRE"):
						ESTADO_F2C="OCUPADO"
						PARTIDA_F2C = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][3])
						LISTA_EVENTO.append((int(PARTIDA_F2C),"PF2C",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F2C.append((int(C),"PF2C",EVENTO[2]))
						LISTA_F2C = sorted(LISTA_F2C, key=lambda element: (element[2], element[0]))
				else:        #ASSUNTO -, nao passa por esta fase, vai para a fase 3
					print(f'valor do assunto - {lista_utentes[int(EVENTO[2].split(" ")[1])-1][5]}')
					if (ESTADO_F3 == "LIVRE"):
						ESTADO_F3="OCUPADO"
						PARTIDA_F3 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][6])
						LISTA_EVENTO.append((int(PARTIDA_F3),"PF3",EVENTO[2]))
						LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
					else:
						LISTA_F3.append((int(C),"PF3",EVENTO[2]))
						LISTA_F3 = sorted(LISTA_F3, key=lambda element: (element[2], element[0]))

				if(len(LISTA_F1) != 0):
					LISTA_F1 = sorted(LISTA_F1, key=lambda element: (element[2], element[0]))
					EVENTO = LISTA_F1.pop(0)
					ESTADO_F1="OCUPADO"
					TEMPO_ESPERA = (C-int(EVENTO[0]))
					ESPERA_TOTAL=ESPERA_TOTAL+TEMPO_ESPERA
					if(TEMPO_ESPERA != 0) :
						LST_TEMPOS_ESPERA.append(TEMPO_ESPERA)
						CONT_ESPERA += 1
					#print(f'EVENTO[2]-{EVENTO[2]}')
					#print(f'EVENTO[2].split(" ")-{EVENTO[2].split(" ")}')
					#print(f'EVENTO[2].split(" ")[1]-{EVENTO[2].split(" ")[1]}')
					#print(f'lista_utentes[int(EVENTO[2].split(" ")[1])-1]{lista_utentes[int(EVENTO[2].split(" ")[1])-1]}')
					PARTIDA_F1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][2])
					LISTA_EVENTO.append((int(PARTIDA_F1),"PF1",EVENTO[2]))
					LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))

					

			elif (EVENTO[1] == "CH") :
				if (ESTADO_F1 == "LIVRE"):
					ESTADO_F1="OCUPADO"
					PARTIDA_F1 = C+ int (lista_utentes[int(EVENTO[2].split(" ")[1])-1][2])
					LISTA_EVENTO.append((int(PARTIDA_F1),"PF1",EVENTO[2]))
					LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
				else :
					print(f'INDEX_PROX_UTENTE-{INDEX_PROX_UTENTE-1}')
					LISTA_F1.append((int(C),"PF1",UTENTE)) #lista_utentes[INDEX_PROX_UTENTE-1][0]
					LISTA_F1 = sorted(LISTA_F1, key=lambda element: (element[2], element[0]))
			else:
				print("VETOR DE EVENTO FOI INICIALIZADO")

				


			sistema_writer.writerow({'CLOCK' : C, 'TIPO EVENTO' : EVENTO[1] ,'UTENTE' : UTENTE, 'PROX_CHEGADA' : PROX_CHEGADA, 'LISTA_F1' : LISTA_F1, 'ESTADO_F1' : ESTADO_F1, 'PARTIDA_F1' : PARTIDA_F1, 'LISTA_F2A' : LISTA_F2A, 'ESTADO_F2A1' : ESTADO_F2A1, 'PARTIDA_F2A1' : PARTIDA_F2A1, 'ESTADO_F2A2' : ESTADO_F2A2, 'PARTIDA_F2A2' : PARTIDA_F2A2, 'LISTA_F2B' : LISTA_F2B, 'ESTADO_F2B1' : ESTADO_F2B1, 'PARTIDA_F2B1' : PARTIDA_F2B1, 'ESTADO_F2B2' : ESTADO_F2B2, 'PARTIDA_F2B2' : PARTIDA_F2B2, 'LISTA_F2C' : LISTA_F2C, 'ESTADO_F2C' : ESTADO_F2C, 'PARTIDA_F2C' : PARTIDA_F2C, 'LISTA_F3' : LISTA_F3, 'ESTADO_F3' : ESTADO_F3, 'PARTIDA_F3' : PARTIDA_F3, 'ESPERA_TOTAL' : ESPERA_TOTAL})
			LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
			print(f'\nCLOCK- {C}')
			print(f'1-INSERE- {LISTA_EVENTO}')

			


			LISTA_EVENTO.pop(0)
			print(f'2-REMOVE- {LISTA_EVENTO}')
			print(f'F1 - {ESTADO_F1} - {LISTA_F1}')
			print(f'F2A- A1 -{ESTADO_F2A1} - A2 -{ESTADO_F2A2} - {LISTA_F2A}')
			print(f'F2B- B1 -{ESTADO_F2B1} - B2 -{ESTADO_F2B2} - {LISTA_F2B}')
			print(f'F2C- {ESTADO_F2C} - {LISTA_F2C}')
			print(f'F3 - {ESTADO_F3} - {LISTA_F3}')

			
				
		

			

			LISTA_EVENTO = sorted(LISTA_EVENTO, key=lambda element: (element[0], element[2]))
			
		else:
			C += 1
			if (C <= 60*60*2 ):
				if (ESTADO_F2A1 == "OCUPADO"):
					T1_TAXA_OCUP_A1 += 1
				if (ESTADO_F2A2 == "OCUPADO"):
					T1_TAXA_OCUP_A2 += 1
				if (ESTADO_F2B1 == "OCUPADO"):
					T1_TAXA_OCUP_B1 += 1
				if (ESTADO_F2B2 == "OCUPADO"):
					T1_TAXA_OCUP_B2 += 1
				if (ESTADO_F2C == "OCUPADO"):
					T1_TAXA_OCUP_C += 1

				T1_CONT_ESPERA = T1_CONT_ESPERA + CONT_ESPERA
				for i in LST_TEMPOS_ESPERA:
					if(T1_TEMPO_ESPERA_MAX < i):
						T1_TEMPO_ESPERA_MAX=i

					if(i != 0 and T1_TEMPO_ESPERA_MIN > i):
						T1_TEMPO_ESPERA_MIN=i
					T1_TEMPO_ESPERA=T1_TEMPO_ESPERA + i
						


					

			elif (C <= 60*60*2*2):
				if (ESTADO_F2A1 == "OCUPADO"):
					T2_TAXA_OCUP_A1 += 1
				if (ESTADO_F2A2 == "OCUPADO"):
					T2_TAXA_OCUP_A2 += 1
				if (ESTADO_F2B1 == "OCUPADO"):
					T2_TAXA_OCUP_B1 += 1
				if (ESTADO_F2B2 == "OCUPADO"):
					T2_TAXA_OCUP_B2 += 1
				if (ESTADO_F2C == "OCUPADO"):
					T2_TAXA_OCUP_C += 1

				T2_CONT_ESPERA = T2_CONT_ESPERA + CONT_ESPERA
				for i in LST_TEMPOS_ESPERA:
					if(T2_TEMPO_ESPERA_MAX < i):
						T2_TEMPO_ESPERA_MAX=i

					if(i != 0 and T2_TEMPO_ESPERA_MIN > i):
						T2_TEMPO_ESPERA_MIN=i
					T2_TEMPO_ESPERA=T2_TEMPO_ESPERA + i

			elif (C <= 60*60*2*3):
				if (ESTADO_F2A1 == "OCUPADO"):
					T3_TAXA_OCUP_A1 += 1
				if (ESTADO_F2A2 == "OCUPADO"):
					T3_TAXA_OCUP_A2 += 1
				if (ESTADO_F2B1 == "OCUPADO"):
					T3_TAXA_OCUP_B1 += 1
				if (ESTADO_F2B2 == "OCUPADO"):
					T3_TAXA_OCUP_B2 += 1
				if (ESTADO_F2C == "OCUPADO"):
					T3_TAXA_OCUP_C += 1

				T3_CONT_ESPERA = T3_CONT_ESPERA + CONT_ESPERA
				for i in LST_TEMPOS_ESPERA:
					if(T3_TEMPO_ESPERA_MAX < i):
						T3_TEMPO_ESPERA_MAX=i

					if(i != 0 and T3_TEMPO_ESPERA_MIN > i):
						T3_TEMPO_ESPERA_MIN=i
					T3_TEMPO_ESPERA=T3_TEMPO_ESPERA + i

			else:
				if (ESTADO_F2A1 == "OCUPADO"):
					T4_TAXA_OCUP_A1 += 1
				if (ESTADO_F2A2 == "OCUPADO"):
					T4_TAXA_OCUP_A2 += 1
				if (ESTADO_F2B1 == "OCUPADO"):
					T4_TAXA_OCUP_B1 += 1
				if (ESTADO_F2B2 == "OCUPADO"):
					T4_TAXA_OCUP_B2 += 1
				if (ESTADO_F2C == "OCUPADO"):
					T4_TAXA_OCUP_C += 1

				T4_CONT_ESPERA = T4_CONT_ESPERA + CONT_ESPERA
				for i in LST_TEMPOS_ESPERA:
					if(T4_TEMPO_ESPERA_MAX < i):
						T4_TEMPO_ESPERA_MAX=i

					if(i != 0 and T4_TEMPO_ESPERA_MIN > i):
						T4_TEMPO_ESPERA_MIN=i
					T4_TEMPO_ESPERA=T4_TEMPO_ESPERA + i

			CONT_ESPERA=0
			LST_TEMPOS_ESPERA=[]
		#print(C)
	
print(f'Foi criado um ficheiro -> \"{file_to_write}\"\n com a INFORMACAO DE CADA PASSO DADO no sistema \n')
print(f'E foi criado um ficheiro -> \"{file_to_stat}\"\n com as ESTATISTICAS OBTIDAS do sistema \n')
print(f'Apartir dos dados gerados , que são lidos \ndo ficheiro -> \"{file_to_read}\"')
#with open(file_to_stat, mode='a') as tabela_estatisticas:
	#fieldnames = ['T1_TAXA_OCUP_A1','T1_TAXA_OCUP_A2','T1_TAXA_OCUP_B1','T1_TAXA_OCUP_B2','T1_TAXA_OCUP_C','T2_TAXA_OCUP_A1','T2_TAXA_OCUP_A2','T2_TAXA_OCUP_B1','T2_TAXA_OCUP_B2','T2_TAXA_OCUP_C','T3_TAXA_OCUP_A1','T3_TAXA_OCUP_A2','T3_TAXA_OCUP_B1','T3_TAXA_OCUP_B2','T3_TAXA_OCUP_C','T4_TAXA_OCUP_A1','T4_TAXA_OCUP_A2','T4_TAXA_OCUP_B1','T4_TAXA_OCUP_B2','T4_TAXA_OCUP_C','TOTAL_TAXA_OCUP_A1','TOTAL_TAXA_OCUP_A2','TOTAL_TAXA_OCUP_B1','TOTAL_TAXA_OCUP_B2','TOTAL_TAXA_OCUP_C']]
	#estatisticas_writer = csv.DictWriter(tabela_estatisticas , fieldnames=fieldnames)
	#estatisticas_writer.writeheader()
file_estatisticas=open(file_to_stat, mode='w')

#TEMPOS DE ESPERA

TT_CONT_ESPERA = T1_CONT_ESPERA + T2_CONT_ESPERA + T3_CONT_ESPERA + T4_CONT_ESPERA
TT_TEMPO_ESPERA=  T1_TEMPO_ESPERA + T2_TEMPO_ESPERA + T3_TEMPO_ESPERA + T4_TEMPO_ESPERA

TT_TEMPO_ESPERA_MIN = min(T1_TEMPO_ESPERA_MIN,T2_TEMPO_ESPERA_MIN,T3_TEMPO_ESPERA_MIN,T4_TEMPO_ESPERA_MIN)
if(TT_TEMPO_ESPERA_MIN == 999999):
	TT_TEMPO_ESPERA_MIN=0

if(T1_TEMPO_ESPERA_MIN == 999999):
	T1_TEMPO_ESPERA_MIN=0
if(T2_TEMPO_ESPERA_MIN == 999999):
	T2_TEMPO_ESPERA_MIN=0
if(T3_TEMPO_ESPERA_MIN == 999999):
	T3_TEMPO_ESPERA_MIN=0
if(T4_TEMPO_ESPERA_MIN == 999999):
	T4_TEMPO_ESPERA_MIN=0

TT_TEMPO_ESPERA_MAX = max(T1_TEMPO_ESPERA_MAX,T2_TEMPO_ESPERA_MAX,T3_TEMPO_ESPERA_MAX,T4_TEMPO_ESPERA_MAX)
if(TT_TEMPO_ESPERA_MAX == 0):
	TT_TEMPO_ESPERA_MAX=0

if(T1_TEMPO_ESPERA_MAX == 0):
	T1_TEMPO_ESPERA_MAX=0
if(T2_TEMPO_ESPERA_MAX == 0):
	T2_TEMPO_ESPERA_MAX=0
if(T3_TEMPO_ESPERA_MAX == 0):
	T3_TEMPO_ESPERA_MAX=0
if(T4_TEMPO_ESPERA_MAX == 0):
	T4_TEMPO_ESPERA_MAX=0

if(T1_CONT_ESPERA != 0):
	T1_TEMPO_ESPERA_MED = T1_TEMPO_ESPERA/T1_CONT_ESPERA
else:
	T1_TEMPO_ESPERA_MED = 0
if(T2_CONT_ESPERA != 0):
	T2_TEMPO_ESPERA_MED = T2_TEMPO_ESPERA/T2_CONT_ESPERA
else:
	T2_TEMPO_ESPERA_MED = 0
if(T3_CONT_ESPERA != 0):
	T3_TEMPO_ESPERA_MED = T3_TEMPO_ESPERA/T3_CONT_ESPERA
else:
	T3_TEMPO_ESPERA_MED = 0
if(T4_CONT_ESPERA != 0):
	T4_TEMPO_ESPERA_MED = T4_TEMPO_ESPERA/T4_CONT_ESPERA
else:
	T4_TEMPO_ESPERA_MED = 0
if(TT_CONT_ESPERA != 0):
	TT_TEMPO_ESPERA_MED = TT_TEMPO_ESPERA/TT_CONT_ESPERA
else:
	TT_TEMPO_ESPERA_MED = 0


#TAXAS DE OCUPACAO

T1_A1 = (T1_TAXA_OCUP_A1*100)/(60*60*2)
T1_A2 = (T1_TAXA_OCUP_A2*100)/(60*60*2)
T1_B1 = (T1_TAXA_OCUP_B1*100)/(60*60*2)
T1_B2 = (T1_TAXA_OCUP_B2*100)/(60*60*2)
T1_C =  (T1_TAXA_OCUP_C*100)/(60*60*2)

T2_A1 = (T2_TAXA_OCUP_A1*100)/(60*60*2)
T2_A2 = (T2_TAXA_OCUP_A2*100)/(60*60*2)
T2_B1 = (T2_TAXA_OCUP_B1*100)/(60*60*2)
T2_B2 = (T2_TAXA_OCUP_B2*100)/(60*60*2)
T2_C =  (T2_TAXA_OCUP_C*100)/(60*60*2)

T3_A1 = (T3_TAXA_OCUP_A1*100)/(60*60*2)
T3_A2 = (T3_TAXA_OCUP_A2*100)/(60*60*2)
T3_B1 = (T3_TAXA_OCUP_B1*100)/(60*60*2)
T3_B2 = (T3_TAXA_OCUP_B2*100)/(60*60*2)
T3_C =  (T3_TAXA_OCUP_C*100)/(60*60*2)

T4_A1 = (T4_TAXA_OCUP_A1*100)/(60*60*2)
T4_A2 = (T4_TAXA_OCUP_A2*100)/(60*60*2)
T4_B1 = (T4_TAXA_OCUP_B1*100)/(60*60*2)
T4_B2 = (T4_TAXA_OCUP_B2*100)/(60*60*2)
T4_C =  (T4_TAXA_OCUP_C*100)/(60*60*2)

TT_A1 = ((T1_TAXA_OCUP_A1+T2_TAXA_OCUP_A1+T3_TAXA_OCUP_A1+T4_TAXA_OCUP_A1)*100)/(tempo_final)
TT_A2 = ((T1_TAXA_OCUP_A2+T2_TAXA_OCUP_A2+T3_TAXA_OCUP_A2+T4_TAXA_OCUP_A2)*100)/(tempo_final)
TT_B1 = ((T1_TAXA_OCUP_B1+T2_TAXA_OCUP_B1+T3_TAXA_OCUP_B1+T4_TAXA_OCUP_B1)*100)/(tempo_final)
TT_B2 = ((T1_TAXA_OCUP_B2+T2_TAXA_OCUP_B2+T3_TAXA_OCUP_B2+T4_TAXA_OCUP_B2)*100)/(tempo_final)
TT_C =  ((T1_TAXA_OCUP_C +T2_TAXA_OCUP_C +T3_TAXA_OCUP_C +T4_TAXA_OCUP_C )*100)/(tempo_final)


file_estatisticas.write(f'TEmed = Tempo de Espera Médio\nTEmax = Tempo de Espera Máximo\nTEmin = Tempo de Espera Minimo\nTEtot = Tempo de Espera Total\nUtot = Utentes que tiveram de Esperar\n')
file_estatisticas.write(f'TdO = Taxa de Ocupacao\nT1 = 9h até às 11h\nT2 = 11h até às 13h\nT3 = 13h até às 15h\nT4 = 15h até às 17h\nTT =Tempo Total\n')
file_estatisticas.write(f'A1 = Balcao 1 com o Assunto A\nA2 = Balcao 2 com o Assunto A\nB1 = Balcao 1 com o Assunto B\nB2 = Balcao 2 com o Assunto B\nC = Único Balcao com o Assunto C\n\n')

file_estatisticas.write(f'TEmed A1 T1 = {("%.3f" % T1_TEMPO_ESPERA_MED)}seg    \tTEmax A2 T1 = {( T1_TEMPO_ESPERA_MAX)}seg    \tTEmin B1 T1 = {( T1_TEMPO_ESPERA_MIN)}seg    \tTEtot B2 T1 = {( T1_TEMPO_ESPERA)}seg   \t Utot C T1 = {(T1_CONT_ESPERA)} utentes\n')
file_estatisticas.write(f'TEmed A1 T2 = {("%.3f" % T2_TEMPO_ESPERA_MED)}seg    \tTEmax A2 T2 = {( T2_TEMPO_ESPERA_MAX)}seg    \tTEmin B1 T2 = {( T2_TEMPO_ESPERA_MIN)}seg    \tTEtot B2 T2 = {( T2_TEMPO_ESPERA)}seg   \t Utot C T2 = {(T2_CONT_ESPERA)} utentes\n')
file_estatisticas.write(f'TEmed A1 T3 = {("%.3f" % T3_TEMPO_ESPERA_MED)}seg    \tTEmax A2 T3 = {( T3_TEMPO_ESPERA_MAX)}seg    \tTEmin B1 T3 = {( T3_TEMPO_ESPERA_MIN)}seg    \tTEtot B2 T3 = {( T3_TEMPO_ESPERA)}seg   \t Utot C T3 = {(T3_CONT_ESPERA)} utentes\n')
file_estatisticas.write(f'TEmed A1 T4 = {("%.3f" % T4_TEMPO_ESPERA_MED)}seg    \tTEmax A2 T4 = {( T4_TEMPO_ESPERA_MAX)}seg    \tTEmin B1 T4 = {( T4_TEMPO_ESPERA_MIN)}seg    \tTEtot B2 T4 = {( T4_TEMPO_ESPERA)}seg   \t Utot C T4 = {(T4_CONT_ESPERA)} utentes\n')
file_estatisticas.write(f'TEmed A1 TT = {("%.3f" % TT_TEMPO_ESPERA_MED)}seg    \tTEmax A2 TT = {( TT_TEMPO_ESPERA_MAX)}seg    \tTEmin B1 TT = {( TT_TEMPO_ESPERA_MIN)}seg    \tTEtot B2 TT = {( TT_TEMPO_ESPERA)}seg   \t Utot C TT = {(TT_CONT_ESPERA)} utentes\n')

file_estatisticas.write(f'\n')

file_estatisticas.write(f'TdO A1 T1 = {("%.3f" % T1_A1)}%   \tTdO A2 T1 = {("%.3f" % T1_A2)}%   \tTdO B1 T1 = {("%.3f" % T1_B1)}%   \tTdO B2 T1 = {("%.3f" % T1_B2)}%   \tTdO C T1 = {("%.3f" % T1_C)}%\n')
file_estatisticas.write(f'TdO A1 T2 = {("%.3f" % T2_A1)}%   \tTdO A2 T2 = {("%.3f" % T2_A2)}%   \tTdO B1 T2 = {("%.3f" % T2_B1)}%   \tTdO B2 T2 = {("%.3f" % T2_B2)}%   \tTdO C T2 = {("%.3f" % T2_C)}%\n')
file_estatisticas.write(f'TdO A1 T3 = {("%.3f" % T3_A1)}%   \tTdO A2 T3 = {("%.3f" % T3_A2)}%   \tTdO B1 T3 = {("%.3f" % T3_B1)}%   \tTdO B2 T3 = {("%.3f" % T3_B2)}%   \tTdO C T3 = {("%.3f" % T3_C)}%\n')
file_estatisticas.write(f'TdO A1 T4 = {("%.3f" % T4_A1)}%   \tTdO A2 T4 = {("%.3f" % T4_A2)}%   \tTdO B1 T4 = {("%.3f" % T4_B1)}%   \tTdO B2 T4 = {("%.3f" % T4_B2)}%   \tTdO C T4 = {("%.3f" % T4_C)}%\n')
file_estatisticas.write(f'TdO A1 TT = {("%.3f" % TT_A1)}%   \tTdO A2 TT = {("%.3f" % TT_A2)}%   \tTdO B1 TT = {("%.3f" % TT_B1)}%   \tTdO B2 TT = {("%.3f" % TT_B2)}%   \tTdO C TT = {("%.3f" % TT_C)}%\n')

#estatisticas_writer.writerow({})

file_estatisticas.close()
