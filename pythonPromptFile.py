# Tome cuidado com a endentacao se nao nao ira funcionar
# para Python 3
opcao = 0
qualquerCoisa=""

def banner(titulo):
 print("\n=========="+titulo+"===========")
 print("===============================\n")

def escreveArquivo(arquivo,texto):
 with open(arquivo, 'a') as nesse:
  nesse.write(texto+"\n")
  nesse.close()

def leLinhasArquivo(arquivo, verboso):
 i=0
 with open(arquivo, 'r') as desse: 
  textoLinhas = desse.readlines()
  if(verboso != ""):
   print("..................\n")
  for linha in textoLinhas:
   if(verboso != ""):
    print(linha) 
   i += 1
  if(verboso != ""): 
   print("..................")
  return i 

def checaMenu(opc):
 try:
  if(int(opc) > 6):
   print("Essa opcao nao existe, tente outra!")
 except ValueError:
  print("Essa opcao nao existe, tente outra!");
  
def salvaNovaEquipe():
 escreveArquivo("equipes.txt",input("Nova equipe: ")) 

def salvaNovoJogo():   
 escreveArquivo("jogos.txt",input("Digite novo jogo, ex: 12/12/2022 Sao Paulo x Palmeiras : "))

def listaJogos():
 leLinhasArquivo("jogos.txt", "sim")
 
def ListaTotalJogos():
 total =  leLinhasArquivo("jogos.txt", "")
 print("\nTOTAL JOGOS ====> "+ str(total) +"\n")
     
def menu():
 banner("JOGOS 2022")
 menuEscolhido = 0
 print("1)Sair\n2)Nova equipe\n3)Novo jogo\n4)Numero total jogs\n5)Gravar jogo\n6)Listar os jogos\n\n ")
 menuEscolhido = input("Digite a opcao desejada:");
 checaMenu(menuEscolhido)
 return menuEscolhido

while (opcao != '1'):
 opcao = menu()
 if(opcao == '2'):
  salvaNovaEquipe()
 if(opcao == '3'): 
  salvaNovoJogo()
 if(opcao == '4'): 
  ListaTotalJogos()
 if(opcao == '5'): 
  salvaNovoJogo()
 if(opcao == '6'): 
  listaJogos()
 
 
 
 
