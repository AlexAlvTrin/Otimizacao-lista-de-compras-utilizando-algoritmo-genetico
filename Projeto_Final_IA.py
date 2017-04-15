from random import randint
import random
#matriz produtos
minimo=[]
z=[]
funcao_z=[]
lista_somaz=[]
soma=0
soma_z=0
lista_pedidos=[]
lista_beneficio=[]
#restricao por produto
r=[10,15,20,25,30,35,40,45]
#restricao por supermercado
s=[2,4,5,6,7,8,9,9]

#matriz custo
custo=matriz8x8=[
                 [3.99,4.99,4.75,2.99,3.99,3.99,1.97,4.98],

                 [5.99,12.90,5.98,11.99,9.49,6.99,15.77,13.98],

                 [12.90,9.39,9.90,15.99,14.59,12.99,9.99,10.84],

                 [0.99,4.99,1.18,1.79,0.99,1.99,1.18,3.98],

                 [3.99,6.89,7.98,9.99,7.89,6.99,5.97,6.88],

                 [5.99,15.99,0,3.49,10.09,6.99,5.97,8.98],

                 [12.90,7.59,6.98,7.99,4.79,9.99,9.75,10.38],

                 [4.99,7.98,4.98,7.99,7.89,5.99,5.98,3.58]
                 ]

#matrizes pedidos, e beneficios
beneficio=matriz8x8=[[0 for col in range(8)] for row in range(8)]
pedidos=matriz8x8=[[0 for col in range(8)] for row in range(8)]



for x in range (0,8):
     minimo.append(min(custo[x]))
     
# preenchendo a lista beneficio    
for x in range (0,8):
    for y in range (0,8):
        beneficio[x][y]=minimo[x]-custo[x][y]
        lista_beneficio.append(beneficio[x][y])
        

#algoritmo genetico
TM=0.01
TC=0.85
tam=64
lista_z=[]
indiv=[]
I=[[]]*20200
F=[[]]*200
Z=[[]]*200
Beneficio=[[]]*200
B1=[]
z=0
w=tam
soma_beneficio=[0]*200
tamanho=[]


#funcao ordnear ordem decrescente
def decres1(count, vet_qualquer=[],vet2=[],vet3=[],vet4=[]):
 count=0
 for t in range (0,8):
  xvet_qualquer=vet_qualquer[count:count+8]  
  xvet2=vet2[count:count+8]
  xvet3=vet3[count:count+8]
  for s in range (0,10):    
   for x in range (0,7):           
      if xvet_qualquer[x+1]>xvet_qualquer[x]:
       aux=xvet_qualquer[x]
       xvet_qualquer[x]=xvet_qualquer[x+1]
       xvet_qualquer[x+1]=aux
       aux1=xvet2[x]     
       xvet2[x]=xvet2[x+1]
       xvet2[x+1]=aux1
       aux2=xvet3[x]
       xvet3[x]=xvet3[x+1]
       xvet3[x+1]=aux2
  vet_qualquer[count:count+8]=xvet_qualquer
  vet2[count:count+8]=xvet2
  vet4.append(xvet3)
  count=count+8     
      
def decres2(vet_qualquer=[],vet2=[]):      
  for s in range (0,200):    
   for x in range (0,198):           
      if vet_qualquer[x+1]>vet_qualquer[x]:
       aux=vet_qualquer[x]
       vet_qualquer[x]=vet_qualquer[x+1]
       vet_qualquer[x+1]=aux  
       aux1=vet2[x]     
       vet2[x]=vet2[x+1]
       vet2[x+1]=aux1  

#gerando individuos
for t in range (0,200):
 for x in range (0,8):
    soma=0
    for y in range (0,8):
        n=randint(0,s[x])
        pedidos[x][y]=n
        soma=pedidos[x][y]+soma
        if soma>r[x]:
           pedidos[x][y]=0
           soma=soma-pedidos[x][y]
        indiv.append(pedidos[x][y])     
         

#separando individuos
for x in range (0,200):
 I[x]=indiv[z:w]
 z=z+tam
 w=w+tam

 
#verificando a taxa de cruzamento e de mutação
t=0  
count=0  
z=199
k=1
while t<20000:
  n=random.random()
  if n<TC:
      s=randint(1,62)
      I[t+200]=I[t][0:s]+I[t+1][s:64]
      I[t+201]=I[t+1][0:s]+I[t][s:64]
  else:
        I[t+200]=I[t]
        I[t+201]=I[t+1]
  m=random.random()
  if m<TM:
   j=randint(0,63)
   n1=randint(0,10)
   n2=randint(0,10)
   I[t+200][j]=n1
   I[t+201][j]=n2      
  t=t+2

#os filhos resultantes de 100 geraões de cruzamentos e mutações
F=I[20000:20200]  

#a lista função objetivo, pedidos * beneficio
count=0
for t in range (0,200):
 soma_z=0   
 for x in range (0,tam):
         funcao_z.append(F[t][x]*lista_beneficio[x])
         soma_z=funcao_z[x+count]+soma_z
 count=64+count        
 lista_somaz.append(soma_z)

z=0
w=tam
#criando individuo da funcao z
for x in range (0,200):
 Z[x]=funcao_z[z:w]
 z=z+tam
 w=w+tam 
 

 


z=0
w= 8
#ordenando ordem crescente por funcao z
for t in range (0,200):
 decres1(0,Z[t], F[t], lista_beneficio,B1)
 Beneficio[t]=B1[z:w]
 z=z+8
 w=w+8    

   
lista_somaz1=[]   
#penalizando  os individuos
for t in range (0,200):
     count = 0
     somaz1=0
     for x in range (0,8):
         soma=0
         count1=0
         for y in range (count, count+8):              
               soma=F[t][y]+soma
               if soma>r[x]:
                   resultado=soma-r[x]
                   F[t][y]=F[t][y]-resultado
                   Z[t][y]=F[t][y]*Beneficio[t][x][count1]
                   soma=r[x]
               count1=count1+1
               somaz1=Z[t][y]+somaz1
         count=count+8
     lista_somaz1.append(somaz1)    

for t in range (0,200):
    tamanho.append(t)


#ordenando em ordem crescente a lista que soma o custo total de um individuo
decres2(lista_somaz1, tamanho)



print ' Solucao para o problema' , 'Individuo', F[tamanho[0]]
print ' Custo da compra', 'R$',lista_somaz1[0]*-1,' '
print 'Economia de', 'R$',max(lista_somaz1)-min(lista_somaz1) ,'em relacao ao maior gasto.' 


