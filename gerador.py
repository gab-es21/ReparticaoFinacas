
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import csv

pessoas = random.randint(120,150) #gerar numero de pessoas entre 120 e 150

tempo_chegada= []

print (pessoas)

#CALCULO DO TEMPO DE CHEGADA NUMA LISTA
for j in range(pessoas):
	r1=random.randint(1,100)
	if r1<=10:                                # 9h - 11h          10%
		r2=random.randint(1,60*60*2)
		tempo_chegada.append(r2)
	elif r1<=(10+25):                         # 11h - 13h         25%
		r2=random.randint(60*60*2+1,2*60*60*2)
		tempo_chegada.append(r2)
	elif r1<=(10+25+45):                      # 13h - 15h         45%
		r2=random.randint(2*60*60*2+1,3*60*60*2)
		tempo_chegada.append(r2)
	else:                                     # 15h - 17h         20%
		r2=random.randint(3*60*60*2+1,4*60*60*2)
		tempo_chegada.append(r2)

#ORDENACAO DA LISTA POR ORDEM CRESCENTE
tempo_chegada.sort()



with open('tabela_utentes.csv', mode='w') as tabela_utentes:
	fieldnames = ['cliente(tipo-num)', 'tempo_chegada', '1_fase_tempo_triagem', '2_fase_tempo_balcao_assunto', '2_fase_regresso', 'assunto','3_fase_tempo_tesouraria']
	utentes_writer = csv.DictWriter(tabela_utentes , fieldnames=fieldnames)

	utentes_writer.writeheader()

	for i in range(pessoas):
		#Calculo do tipo de cliente
		r1=random.randint(1,100)
		if r1<=20 :
			tipo="P {}"  						# prioritario     20%   considerado prioritario logo na fase 1
		else:
			tipo="R {}"  						# Regulare           80%
		cliente=(tipo.format(i+1))
		#Atribuicao do tempo de chegada
		chegada=tempo_chegada[i]
		#calculo do Assunto
		r1=random.randint(1,100)
		if r1 <= 10:                      #sem Assunto    10%   , logo para a fase 3 
			assunto="-"
		else:
			r2=random.randint(1,100)
			if r2<=35 :
				assunto="A" 						# Assunto A       35%
			elif r2 <= (35+50):
				assunto="B"  						# Assunto B       50%
			else:
				assunto="C"  						# Assunto C       15%
		#calculo do tempo na fase 1
		r1=random.randint(1,100)
		if r1<=55 :           					# ]0,1]           55%
			f1=random.randint(1,1*60)
		elif r1 <= (55+35) : 					# ]1,2]           35% 
			f1=random.randint(1*60+1,2*60)
		else:                 					# ]2,3]           10% 
			f1=random.randint(2*60+1,3*60)
		#calculo do tempo na fase 2
		if assunto == "A":
			r1=random.randint(1,100)
			if r1<=25 :          				# ]00,05]         25%
				r2=random.randint(1,5*60)
				f2=r2
			elif r1 <= (25+35) :  				# ]05,15]         35% 
				r2=random.randint(5*60+1,15*60)
				f2=r2
			elif r1 <= (25+35+30) :  			# ]15,25]         30% 
				r2=random.randint(15*60+1,25*60)
				f2=r2
			else:                               # ]25,30]         10% 
				r2=random.randint(25*60+1,30*60)
				f2=r2
			r3=random.randint(1,100)
			if r3<=20 :                     ## 20%  passam pela fase 3
				r4=random.randint(1,100)
				if r4<=40:               # ]0,1]           40%
					f3=random.randint(1,1*60)
				elif r4 <=(40+55):       # ]1,2]           95% 
					f3=random.randint(1*60+1,2*60)
				else:                    # ]2,3]            5% 
					f3=random.randint(2*60+1,3*60)               
				r5=random.randint(1,100)
				if r4<=70:              #   70% abandona na fase 3
					f2r="NAO"
				else:
					f2r="SIM"			# 30% regressa a fase 2
			else:
				f3=0
				f2r="NAO"

		elif assunto == "B":
			r1=random.randint(1,100)
			if r1<=25 :          				# ]00,05]         25%
				r2=random.randint(1,5*60)
				f2=r2
			elif r1 <= (25+45) :  				# ]05,10]         45% 
				r2=random.randint(5*60+1,10*60)
				f2=r2
			elif r1 <= (25+45+25) :  			# ]10,15]         25% 
				r2=random.randint(10*60+1,15*60)
				f2=r2
			else:                               # ]15,25]         05% 
				r2=random.randint(15*60+1,25*60)
				f2=r2
			r3=random.randint(1,100)
			if r3<=30 :                     ## 30%  passam pela fase 3
				r4=random.randint(1,100)
				if r4<=40:               # ]0,1]           40%
					f3=random.randint(1,1*60)
				elif r4 <=(40+55):       # ]1,2]           95% 
					f3=random.randint(1*60+1,2*60)
				else:
					f3=random.randint(2*60+1,3*60)               # ]2,3]            5% 
				r5=random.randint(1,100)
				if r4<=80:              #   80% abandona na fase 3
					f2r="NAO"
				else:
					f2r="SIM"			# 20% regressa a fase 2
			else:
				f3=0
				f2r="NAO"

		elif assunto == "C":            #Assunto C
			r1=random.randint(1,100)
			if r1<=10 :          				# ]00,05]         10%
				r2=random.randint(1,5*60)
				f2=r2
			elif r1 <= (10+35) :  				# ]05,10]         35% 
				r2=random.randint(5*60+1,10*60)
				f2=r2*60
			elif r1 <= (10+35+45) :  			# ]10,15]         45% 
				r2=random.randint(10*60+1,15*60)
				f2=r2*60
			else:                               # ]15,20]         10% 
				r2=random.randint(15*60+1,20*60)
				f2=r2*60
			r3=random.randint(1,100)
			if r3<=75 :                     ## 75%  passam pela fase 3
				r4=random.randint(1,100)
				if r4<=40:               # ]0,1]           40%
					f3=random.randint(1,1*60)
				elif r4 <=(40+55):       # ]1,2]           55% 
					f3=random.randint(1*60+1,2*60)
				else:
					f3=random.randint(2*60+1,3*60)                 # ]2,3]            5% 
				r5=random.randint(1,100)
				if r4<=60:              #   60% abandona na fase 3
					f2r="NAO"
				else:
					f2r="SIM"			# 40% regressa a fase 2
			else:
				f3=0
				f2r="NAO"
		else:
			f2=0

			r4=random.randint(1,100)
			if r4<=40:               # ]0,1]           40%
				f3=random.randint(1,1*60)
			elif r4 <=(40+55):       # ]1,2]           55% 
				f3=random.randint(1*60+1,2*60)
			else:
				f3=random.randint(2*60+1,3*60)                # ]2,3]            5% 
			f2r="NAO"
		
		
		
		utentes_writer.writerow({'cliente(tipo-num)' : cliente, 'tempo_chegada' : chegada, '1_fase_tempo_triagem' : f1, '2_fase_tempo_balcao_assunto' : f2, 'assunto' : assunto, '2_fase_regresso' : f2r, '3_fase_tempo_tesouraria' : f3})
