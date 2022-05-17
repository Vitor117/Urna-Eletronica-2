print("[1] Iniciar Votação")
print("[2] Imprimir Zerísima")
opção = int(input("Digite sua Opção: "))

if opção == 2:
    print()
    print('==PREFEITOS==\n')
    print('PITUCA (PSD) = qtd. VOTOS 0')
    print('LOLO (PT) = qtd. VOTOS 0')
    print('LALAU (Psol) = qtd VOTOS 0\n')
    
    print('==VEREADORES==\n')
    print('BENE (PT) = qtd. VOTOS 0')
    print('JOSÉ (PSD) = qtd. VOTOS 0')
    print('LINEU (Psol) = qtd. VOTOS 0')
    print('CARLOS (PECI) = qtd. VOTOS 0')
    print('GILVAN (PSD) = qtd. VOTOS 0')
    print('DAVI (CDL) = qtd. VOTOS 0')
    print('DADINHO (PT) = qtd. VOTOS 0')
    print('BRUNO (PT) = qtd. VOTOS 0')
    print('JOSEFA (CDL) = qtd. VOTOS 0')
    print('MARIA (SSD) = qtd. VOTOS 0\n')
    
    print('Iniciar votação digite (4)') 
    opção = int(input('Digite o número: ')) 

opção15 = 0 
opção17 = 0 
opção19 = 0 
opção5 = 0 
opção10 = 0 

opção = 1
while opção:
    print()    
    print("======== PREFEITO ========")
    print()
    print('========Candidatos========')
    print('Pituca (15)', 'Lolo (17)', 'Lalau (19)\n')
    print("Para votar em um (CADIDATO) digite o sua opção\n")
    print("Para votar em BRANCO digite (5)")
    opção = int(input("Digite sua opção: "))
    print()
    if opção == 15:
        print("Pituca", "(PSD)\n")
        print("Confirmar voto digite (3)")
        opção = int(input("Digite sua Opção: "))
        opção15 = opção15 + 1
          
    elif opção == 17:
        print("Lolo", "(PT)")
        print("Confirmar Voto Digite (3)")
        opção = int(input("Digite sua Opção: "))
        opção17 = opção17 + 1
        print()
    elif opção == 19:
        print("Lalau", "(Psol)")
        print("Confirmar Voto Digite (3)")
        opção = int(input("Digite sua Opção: "))
        opção19 = opção19 + 1            
        print() 
    elif opção == 5:
        print("VOTO BRANCO\n")
        print("Confirmar Voto Digite (3)")
        opção = int(input("Digite sua Opção: "))
        opção5 = opção5 + 1
        print()  
    else:
        print()
        print('(NÚMERO INVALIDO) Seu VOTO SERÁ COMPUTADO COMO NULO')
        print()
        print('Deseja corrigir aperte (8)')  
        opção = int(input('Digte sua opção: '))
        opção10 = opção10 + 1
        print()
    if opção == 3:
        print()    
        print('VOTO CONFIRMADO!')
        print()    
    if opção == 8:
        print("==CORRIGINDO O VOTO==")
        continue
    break

opção20 = 0 
opção25 =0
opção28 = 0 
opção30 = 0 
opção31 = 0 
opção32 = 0 
opção33 = 0 
opção34 = 0 
opção35 = 0 
opção36 = 0 
opção5 = 0 
opção10 = 0

while opção:
    print()         
    print('====VEREADORES====')           
    print()
    print('Bene (20200)', 'José (25251)', 'Lineu (28282)', 'Carlos (30303)', 'Gilvan (31314)')
    print('Davi (32325)', 'Dadinho (33336)', 'Bruno (34347)', 'Josefa (35358)', 'Maria (36369)\n')
    print("Para votar em um (CADIDATO) digite o sua opção\n")
    print('Para votar em BRANCO digite (5)')
    opção = int(input('Digite sua opção: '))
    print()
    if opção == 20200:
        print('Bene', '(PT)\n')
        print("Confirma voto digite (3)")
        opção = int(input('digite sua opção: '))
        opção20 = opção20 + 1
        print()
    elif opção == 25251:
        print('José', '(PSD)\n')
        print("Confirma voto digite (3)")
        opção = int(input('digite sua opção: '))
        opção25 = opção25 + 1
        print()
    elif opção == 28282:
        print('Lineu', '(Psol)\n')
        print("Confirma voto digite (3)")
        opção = int(input('digite sua opção: '))
        opção28 = opção28 + 1
        print()
    elif opção == 30303:
        print('Carlos', '(PECI)\n')
        print("Confirma voto digite (3)")
        opção = int(input('digite sua opção: '))
        opção30 = opção30 + 1
        print()
    elif opção == 31314:
        print('Gilvan', '(PSD)\n')
        print("Confirma voto digite (3)")
        opção = int(input('digite sua opção: '))
        opção31 = opção31 + 1
        print()
    elif opção == 32325:
        print('Davi', '(CDL)\n')
        print("Confirma voto digite (3)")
        opção = int(input('digite sua opção: '))
        opção32 = opção32 + 1
        print()
    elif opção == 33336:
        print('Dadinho', '(PT)\n')
        print("Confirma voto digite (3)")
        opção = int(input('digite sua opção: '))
        opção33 = opção33 + 1
        print()
    elif opção == 34347:
        print('Bruno', '(PT)\n')
        print("Confirma voto digite (3)")
        opção = int(input('digite sua opção: '))
        opção34 = opção34 + 1
        print()
    elif opção == 35358:
        print('Josefa', '(CDL)\n')
        print("Confirma voto digite (3)")
        opção = int(input('digite sua opção: '))
        opção35 = opção35 + 1
        print()
    elif opção == 36369:
        print('Maria', '(SSD)\n')
        print("Confirma voto digite (3)")
        opção = int(input('digite sua opção: '))
        opção36 = opção36 + 1
        print()
    elif opção == 5:
        print('VOTO BRANCO\n')    
        print("Confirmar digite (3)")
        opção = int(input("Digite sua opção: "))
        opção5 = opção5 + 1 
        print()   
  
    else:
        print()
        print('(NÚMERO INVALIDO) Seu VOTO SERÁ COMPUTADO COMO NULO!')
        print()
        print('Deseja corrigir aperte (8)')  
        print("Confirmar Digite (3)")
        opção = int(input('Digte sua opção: '))
        opção10 = opção10 + 1
        print()
    if opção == 3:    
        print('VOTO CONFIRMADO!')
        print()
        # Essa parte é a que deveria voltar para o inicio do programa por isso eu criei essa condição 6 com o continue mais não finciona.
        # Eu preciso que apareca o candidato eleito para prefeito e os 3 mais votados para vereadores como posso fazer essa ação?
        print("Deseja Continuar Votando Digite (6)")
        print("Finalizar Digite (7)")
        opção = int(input("Digite sua Opção: "))
    if opção == 6:
        continue    
    if opção == 8:
        print("==CORRIGINDO O VOTO==")
        continue
    break
if opção == 7:
    print()  
    print("==TOTAL DE VOTOS DE CADA CANDIDATO==\n")
    print("====PREFEITOS====\n")
    print(f"Pituca (PSD) {opção15}")
    print(f"Lolo (PT) {opção17}")
    print(f"Lalau (Psol) {opção19}")
    print(f"VOTO BRANCO {opção5}")
    print(f"VOTO NULO {opção10}\n")
    print("====VEREADORES====\n")
    print(f"Bene (PT) {opção20}")
    print(f"José (PSD) {opção28}")
    print(f"Lineu (Psol) {opção28}")
    print(f"Carlos (PECI) {opção30}")
    print(f"Gilvan (PSD) {opção31}")
    print(f"Davi (CDL) {opção32}")
    print(f"Dadinho (PT) {opção33}")
    print(f"Bruno (PT) {opção34}")    
    print(f"Josefa (CDL) {opção35}")     
    print(f"Maria (SSD) {opção36}")
    print(f"VOTO BRANCO {opção5}")
    print(f"VOTO NULO {opção10}\n")

   
      

                                                   