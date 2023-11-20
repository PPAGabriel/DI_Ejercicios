''' Prueba de números

a=int(2)
a='4'
b=3
print (b*a)
'''

'''Operadores
+
-
- negacion numerica
*
** exponente
/
// division entera
% modulo o resto

&
|
^ xor
~ not
<< desplazamiento a la izquierda
>> desplazamiento a la derecha

dir =128^255
print(dir)

division=128<<2
print(division)

'''

'''
Una lista es una coleccion ordenada de elementos

lista=[1,2,3,4,5]
print(lista[3])

lista=[[1,2,3,4],
    [4,5,7,8],
    [9,10,11,12]]

print(lista[1][2])

lista2=[1,2.0,"Hola que tal",[3+7j,23]]
print(lista2[3][0])

l=list()  -> Lista vacia

lista2=[1,2.0,"Hola que tal",[3+7j,23],22,33,44,55]
print(lista2[0:8])

lista2[0:3]=['UN','DOS','TRES','CUATRO']
print(lista2)

Tuplas -> Son como las listas pero ordenadas y finitas, es decir, no se puede expandir su espacio

t=(1,2,3,4,5,2.0,"hola",4+5j)
print(t[2])

t2=tuple(["uno","dos"])
print(type(t2))
print(t2)

diccionario={
1: "Uno",
2: "Dos",
3: "Tres",
4: "Cuatro"
}

print(diccionario[3])

diccionario[3]=0b000011
print(diccionario[3])

'''

# CONDICIONALES

variable=2

#if variable==3:
#El bloque de codigo se marca con ':'
#Se tabula el codigo con espacios
#El numero de espacios es libre, pero siempre lo mismo dentro del bloque de codigo
   # print("La variable tiene el valor adecuado")
   # print("sigo dentro de la condicion")
#print("Estoy fuera de la condicion")

#else:
 #   print("La variable no es correcta")



"""
if variable==3:
    print("La variable vale 3")
elif variable==6:
    print("La variable vale 3")
else:
    print("La variable no vale ni 3 ni 6")

# var=(variable%2)? "par"?:"impar"

var="par" if(variable%2==0) else "impar"
print(var)

while variable<20:
    variable=variable+1
    print("El valor es: "+str(variable))
    if variable==16:
        break
    else:
        print("Sigo en bucle")
"""


numeros=[1,2,3,4,5]
suma=0
for numero in numeros:
    print(numero)
    suma+=numero
    print("suma parcial: ", suma)
print(suma,"\n")

# for (int i, i<20,i++)

for i in range(5,17,3):
    print(i)

numeros=("cero","un","dos","tres")
for i in range(len(numeros)):
    print(numeros[i])

for i,num in enumerate(numeros): #devuelve una tupla enumerando el elemento por un lado y por otro el valor de dicha posicion
    #print(i) de solo tener declarado "i" en el for
    print(i, numeros[i])
    #o mejor de esta manera
    print(i,num)

    print("\n")

#############################################################################################

# FUNCIONES

def nome_da_funcion(parametro1,parametro2):

    '''

    Función de ejemplo para mostrar como se escriben las funciones.

    La función hace una suma, si es numero, del parametro 1 y 2.
    Si es una cadena, hace una concatenación.

    :param parametro1:
    :param parametro2:
    :return:
    '''

    print(parametro1)
    return (parametro1+parametro2)

print(nome_da_funcion(1,2))
print(nome_da_funcion("Hola ","que tal"))

print(nome_da_funcion(parametro2=" que tal",parametro1="Hola")) #independiente del orden, a diferencia de java, si le especificamos el valor, no tiene problema en darle un valor



#Podemos darle un valor por defecto comop arametro y multiplicara N veces la cadena dada en otro parametro sin necesidad de darle mas informacion a la funcion
def repetir(cadena,veces=2):
    print(cadena*veces)

repetir("Hola ",5)
repetir("Adios ")

#Tambien permite optimizar los parametro a la hora de hacer operaciones con numeros, y en caso de querer modificar solo un parametro, debemos indicar cual deseamos cambiar
def volumenParalelogramo(lado1=1,lado2=1,altura=1):
    return lado1*lado2*altura

print(volumenParalelogramo())
print(volumenParalelogramo(5))
print(volumenParalelogramo(5,5))
print(volumenParalelogramo(5,5,5))
print(volumenParalelogramo(altura=5))

print("\n")

def sumaMuchosParametros(valor1,valor2,*otros): #esta funcion tendra dos parametros obligatorios como minimo, y con el asteriscos indicamos que puede tener ilimitados parametros posteriormente
    suma=valor1+valor2
    for valor in otros:
        suma+=valor
    print(suma)

sumaMuchosParametros(1,2,3,4,5)

def usuarioCOnDatosExtendidos(nome,dni,edade,**outros): #con doble astericos podemos asignar parametros ya de distintos tipos
    print("Nome: "+nome)
    print("DNI: "+dni)
    print("Edad: ", edade) #al poner la coma no habria problema en darle un valor tipo int
    for clave in outros.keys(): #diccionario.items() nos daria los valores
        print(clave+": ", outros[clave]) #de igual manera, la coma evita el error aceptando cualquier tipo de parametro

usuarioCOnDatosExtendidos("Gabriel","01122333D",33,Sexo="Varón",Vivo=True)

print("\n")

'''
nos damos cuenta que python no trabaja por referencia, sino por valor (con sus excepciones),
 por lo que aunque la variable parezca ser la misma que fue declarada,
  lo que ocurre dentro de la funcion solo ocurre ahi dentro, 
  independiente de que se llamen igual variables internas como las externas
'''

var=5
def funcion(valor):
    var=valor
    print(var)

funcion(9)
print(var) #efectivamente: da 5 mientras que la funcion da 9

#######################################################################

# EJERCICIO 7.1

def ordenTupla(tupla):
    flag=True

    for i in range(len(tupla)):
        if i==(len(tupla)-1):
            break
        else:
            flag= tupla[i]<tupla[i+1]

        if flag==True:
            continue
        else:
            break
    return flag


if ordenTupla((1,2,3,4))==True:
    print("La tupla esta ordenada")
else:
    print("La tupla no esta ordenada")

# EJERCICIO 7.2

#primer apartado

def encajanFichas(f1,f2):

    if f1[0]==f2[0] or f1[0]==f2[1]:
        return "Encajan"
    elif f1[1] == f2[0] or f1[1] == f2[1]:
        return "Encajan"
    else:
        return "No encajan"

print(encajanFichas((3,4),(5,4)))

#segundo apartado

def encajanFichas2(cadena):

    aux=cadena.split()
    f1=aux[0].split("-")
    f2=aux[1].split("-")

    return encajanFichas(f1,f2)

print(encajanFichas2("3-2 2-5"))


#Hacer del 7.5 al 7.8 !!!!!


#ORIENTACION A OBJETOS


'''
class Punto:

    Clase que define a un punto en un plano bidimensional

    def __init__(self,x,y):
        self.x=x
        self.y=y

p1=Punto(1.0,2.3)

p1.x=15.66

print("Coordenadas del punto:",p1.x,",",p1.y)

'''
##########################################################3

import math

class PrimerCuadranteError (Exception):
    def __int__(self, coordenada):
        self.coordenada = coordenada
    def __str__(self):
        return "Error de coordenadas:" + self.coordenada + " : No es un punto del primer cuadrante "
class Punto:

    def __init__(self,x=0,y=0): #con el __ vuelves privada la variable
        self.setX(x)
        self.setY(y)

    def getY(self):
        return str(self.__y)

    def getX(self):
        return str(self.__x)

    def setX(self,x):
        if x>=0:
            self.__x=x
        else:
            raise PrimerCuadranteError("X")

    def setY(self,y):
        if y >= 0:
            self.__y = y
        else:
            raise PrimerCuadranteError("Y")

    x=property(getX,setX)
    y=property(getY,setY)


    def __aCadea(self):
        return "(x,y)= "+str(self.__x)+", "+str(self.__y)

    def aCadea2(self):
        return self.__aCadea()

class Circulo(Punto):
    '''
    Clase que representa un circulo centrado en un punto
    '''
    def __init__(self,x=0,y=0,r=1):
        Punto.__init__(self,x,y)
        self.r=r

    def superficie(self):
        return math.pi*self.r**2

    def perimetro(self):
        return 2*math.pi*self.r

    def __gt__(self, other): #este metodo permite comparar un atributo que deseemos de un objeto
        return self.superficie()>other.superficie()

    def __lt__(self, other):
        return self.superficie()<other.superficie()

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y and self.superficie()==other.superficie()

# tambien existe __ne__ __ge__ __le__

try:
    raise(Exception("Este es otro error indeterminado"))
    p1=Punto(1,3)
    p2=Punto(1,-3)
    p1.x = 6
    print(p1.aCadea2())
    print(p2.aCadea2())
    print(p1.getY())
    print(p1._Punto__x)

    c1 = Circulo(p1.x, p1.y, 3)

    print("La superficie del circulo es:", c1.superficie())
    c1.r = 1
    print("El perimetro del circulo es:", c1.perimetro())
except PrimerCuadranteError as error:
    print(error)
except Exception as error:
    print(error)
finally:
    print("Ejecutando Finally")
#print((p1.x,p1.y))

#print(p1.x,p1.y)






############################################################################

class Cilindro(Circulo):
    def __init__(self,x=0,y=0,r=1,h=1):
        super().__init__(x,y,r)
        self.h=h

    def superficie(self):
        return super().superficie()*2+super().perimetro()*self.h

    def __str__(self):
        return  "Cilindro con centro en: ("+str(self.x)+","+str(self.y)+"), radio:"+str(self.r)+", altura:"+str(self.h)

cil=Cilindro(1,5,3,2)

print("La superficie del cilindro es:",cil.superficie())
print(cil.__str__())

c2=Circulo(1,3,8)

#print(c1>c2)
#print(c1<c2)

#print(c1.__doc__) #imprime la descripcion que hicimos con comillas simples al crear la clase


# Metodos en diccionario

diccionario={
1: "Uno",
2: "Dos",
3: "Tres",
4: ["Cuatro",4,"IV",0b0000100,0o4,0x4,4,0]
}

print(diccionario[3])
print (diccionario.get(5,"No existe el valor")) #se le puede dar un valor por defecto si no encuentra la clave
print(5 in diccionario) #busca si existe la clave y devuelve la respuesta en boolean
print(diccionario.items()) #deuvelve una lista con tuplas donde estan los elementos
print(diccionario.keys()) #devuelve las claves existentes
print(diccionario.values()) #valores sin las claves para diferenciarlo de items

print("Borrando el valor: "+diccionario.pop(2,"No existe la clave"))
print(diccionario.items())

l=list()
l.append("nuevo objeto") #añade un elemento a una lista
l.append([2,3,5])
print(l)

print(l.count([2,3,5])) #cuenta el numero de veces que se repite el elemento en cuestion dentro de la lista
print(len(l)) #este si te devuelve la cantidad de elementos de la lista
l.extend([6,7,8,"nueve"]) #coge los elementos de la coleccion y los añade como nuevos elementos cada uno
print(l)
l.insert(3,"siete") #inserta un elemento en la posicion que deseamos, y corre el resto para adelante
print(l)

print(l.pop(3))
print(l)

l.remove([2,3,5])
l.reverse() #cambia el sentido de los elementos
print(l)

# l.sort() no puede ordenar cuando hay una lista heterogenea con string de por medio

l2=[2,4,3,1,5,9,7,8]
l2.sort()
print(l2)

'''Cadenas'''
c="Hola que tal"
c.count("qu") #cuentas cuantas 'qu' hay
c.find("qu") #nos devuelve la posicion, y si no lo encuentra -1
c.join("varias cadenas") #teoricamente adiciona esto en la cadena, pero la sintaxis falla
print(c.partition(" ")) #te separa la cadena, dandote una tupla
c=c.replace(" ","_")
c.split("_")

###########################################################################################################

# EJERCICIO 6.1

cadena= "recta"

print(cadena[0:2]) #primeros dos caracteres

aux=len(cadena)
print(cadena[(aux-2):aux]) #los ultimos tres caracteres

print(cadena[0:aux:2]) #imprimir cada dos caracteres de cadena

cadena2="Hola mundo!"
print(cadena2[::-1])

cadena3="reflejo"
print(cadena3+cadena3[::-1])

# EJERICICIO 6.2

def insertarCaracter(cadena,caracter):
    nC=""
    longitud=len(cadena)
    for c in range(longitud):
        if (c+1)<longitud:
            nC +=cadena[c]+caracter
        else:
            nC+=cadena[c]
    print(nC)

insertarCaracter("separar",",")

def reemplazarEspacios(cadena,caracter):
    nC = ""
    for c in cadena:
        if c==" ":
            nC += caracter
        else:
            nC+=c
    print(nC)

reemplazarEspacios("meu arquivo de texto.txt","\_")

def reemplazarDigitos(cadena,caracter):
    nC = ""
    for c in cadena:
        if c.isdigit():
            nC += caracter
        else:
            nC+=c
    print(nC)

reemplazarDigitos("Sua clave e: 1540","X")

def insertarCaracter_3(cadena,caracter):
    nC = ""
    for c in range(len(cadena)):
        if (c+1)%3==0:
            nC +=cadena[c]+caracter
        else:
            nC += cadena[c]
    print(nC)

insertarCaracter_3("2552552550",".")

#########################################################################################################

def saludar(lengua):
    def saludar_es():
        print("Hola")

    def saludar_gl():
        print("Ola")

    def saludar_it():
        print("Ciao")

    def saludar_en():
        print("Hello")

    saludo_idiomas={
        "es":saludar_es,
        "gl":saludar_gl,
        "it":saludar_it,
        "en":saludar_en
    }
    return saludo_idiomas[lengua]

f=saludar("es")
f()  #la variable se empieza a comportar como una funcion

# FUNCIONES LAMBDA

#Una posibilidad distinta a las lambda
def es_par(n):
    return (n%2==0)

l=[1,2,3,4]
l2=filter(es_par,l)
for n in l2:
    print(n)

print("------------")
#La opcion de lambda

l3=filter(lambda n:n%2==0,l)
for n in l3:
    print(n)

#List comprehensions
l5=[n**2 for n in l] #eleva a 2 los numeros de la lista

'''
El equivalente:

    for n in l:
        l5.append(n**2)
'''

l4=[n for n in l if n%2==0] #todos los valores de la lista se guardan si cumplen la condicion

print(l4)
print(l5)

m=['a','b']
n=[s*n  for s in m
        for n in l
        if n>0]
print(n)

print("--------")

#Generadores

x=(n**2 for n in l)

for r in x:
    print(r)
print("----------")

#deconstruir el For de Java practicamente
def mi_range(n=0,m=0,i=1):
    while (n<m):
        yield n #produce valores
        n+=i

for n in mi_range(m=5):
    print(n)

#Decoradores

def mi_decorador(funcion):
    def nuevaFuncion(*args):
        print("llamada previa a función: ",funcion.__name__)
        retorno=funcion(*args)
        print("llamada posterior a función: ", funcion.__name__)
        return retorno
    return nuevaFuncion

mi_decorador(saludar("gl"))

##############################################################################################################
def otro_decorador(funcion):
    def nuevaFuncion(*args):
        print("Acciones previas del otro decorador")
        retorno = funcion(*args)
        print("Acciones posteriores al otro decorador")
        return retorno
    return nuevaFuncion

@otro_decorador
@mi_decorador
def otrafuncion(a,b):
    print(a+b)
    return "La suma de a+b es: " + str(a+b)

resultado= otrafuncion(1,2)

print(resultado)

#############################################################################################################



