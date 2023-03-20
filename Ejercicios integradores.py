# Ejercicios integradores para revisar en la clase 7
#
# Punto 1: Escribir una función que calcule el máximo común divisor entre dos números.
#
def a(b, c):
    for i in range(1, b+1):
        for j in range(1, b+1):
            if (c % j == 0 and j == i):
                max = j
                
    print("El maximo comun divisor es: ", max)


b = int(input("Ingrese un numero: "))
c = int(input("Ingrese el segundo numero: "))
a(b, c)
#
#
# Punto 2: Escribir una función que calcule el mínimo común múltiplo entre dos números
#


def a(b, c):
    if (b < c):
        menor = b
    else:
        menor = c

    while not (menor % b == 0 and menor % c == 0):
        menor += 1

    print("El minimo comun multiplo es: ", menor)


b = int(input("Ingrese el primer numero: "))
c = int(input("Ingrese el segundo numero: "))

a(b, c)
#
#
# Punto 3: Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
#


def contador(cadena: str) -> dict:
    frase = cadena.split(" ")
    diccionario = {}

    for palabra in frase:
        if palabra in diccionario:
            diccionario[palabra] = diccionario[palabra] + 1
        else:
            diccionario[palabra] = 1

    return diccionario


print(contador("Más vale trote que dure y no galope que canse."))
#
#
# Punto 4: Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
#


def contador(cadena: str) -> dict:

  frase = cadena.split(" ")
  diccionario = {}
  for palabra in frase:
    if palabra in diccionario:
      diccionario[palabra] = diccionario[palabra] + 1
    else:
      diccionario[palabra] = 1
  return diccionario


print(contador("Más vale trote que dure y no galope que canse."))


def frecuentes(palabraFrecuente: dict) -> tuple:

  max = 0
  for palabra in palabraFrecuente:
    if palabraFrecuente[palabra] > max:
      repetida = palabra
      max = palabraFrecuente[palabra]
  return (repetida, palabraFrecuente[repetida])


print(frecuentes(contador("Más vale trote que dure y no galope que canse.")))
#
#
# Punto 5: Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.
#


def get_int() -> int:
     while True:
         try:
             a = input("Ingrese número: ")
             num = int(a)
             print(num)
             break
         except ValueError:
             print("No se puede obtener el numero correcto.")


def main():
     get_int()


main()
#
#
# Punto 6: Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
# • Un constructor, donde los datos pueden estar vacíos.
# • Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
# • mostrar(): Muestra los datos de la persona.
# • Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
#


class Persona():

  def __init__(self, name: str = None, olds: int = None, idcard: int = None) -> None:
    self.name = name
    self.olds = olds
    self.idcard = idcard

  def __str__(self) -> str:
    return f"Person (Name:{self.nome}, Olds:{self.olds}, Idcard:{self.idcard})"

  def getName(self) -> str:
    return self.name

  def getOlds(self) -> int:
    return self.olds

  def getIdcard(self) -> int:
    return self.idcard

  def setName(self, nombre: str) -> None:
    if len(name) > 1:
      self.name = name
    else:
      raise Exception("Es obligatorio al menos 2 letras")

  def setOlds(self, olds: int) -> None:
    if olds >= 0 and olds <= 120:
      self.edad = olds
    else:
      raise Exception("La Edad entre 0 y 120 años")

  def setIdcard(self, idcard: int) -> None:
    if idcard >= 1000000 and dni < 100000000:
      self.idcard = idcard
    else:
      raise Exception(
          "El Documento de Identidad entre 7 y 9 dígitos numéricos")

  def view(self) -> None:
    print(self)

  def Mayor(self) -> bool:
    if self.olds == None:
      raise Exception("La persona no es mayor de edad")
    return self.olds >= 21

  def main():
    persona1 = Person("Santiago", 41, "29246136")
    persona1.view()
    main()
#
#
# Punto 7: Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase:
# • Un constructor, donde los datos pueden estar vacíos.
# • Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
# • mostrar(): Muestra los datos de la cuenta.
# • ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
# • retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
#


class Person():

  def __init__(self, name: str = None, olds: int = None, idcard: int = None) -> None:
    self.name = name
    self.olds = olds
    self.idcard = idcard

  def __str__(self) -> str:
    return f"Person (Name:{self.nome}, Olds:{self.olds}, Idcard:{self.idcard})"

  def getName(self) -> str:
    return self.name

  def getOlds(self) -> int:
    return self.olds

  def getIdcard(self) -> int:
    return self.idcard

  def setName(self, nombre: str) -> None:
    if len(name) > 1:
      self.name = name
    else:
      raise Exception("Es obligatorio al menos 2 letras")

  def setOlds(self, olds: int) -> None:
    if olds >= 0 and olds <= 120:
      self.edad = olds
    else:
      raise Exception("La Edad entre 0 y 120 años")

  def setIdcard(self, idcard: int) -> None:
    if idcard >= 1000000 and dni < 100000000:
      self.idcard = idcard
    else:
      raise Exception(
          "El Documento de Identidad entre 7 y 9 dígitos numéricos")

  def view(self) -> None:
    print(self)

  def Mayor(self) -> bool:
    if self.olds == None:
      raise Exception("La persona no es mayor de edad")
    return self.olds >= 21


class Account():

  def __init__(self, owner:Person = None, qty: float = 0.0) -> None:
    self.owner = owner
    self.qty = qty

  def __str__(self) -> str:
    return f"Account (Owner:{self.owner}, Qty:{self.qty})"

  def getOwner(self) -> Person:
    return self.owner

  def getQty(self) -> float:
    return self.qty

  def setOwner(self, owner:Person) -> None:
    if owner != None:
      self.owner = owner
    else:
      raise Exception("No puede estar vacio (o NULL)")

  def setQty(self, qty:float) -> None:
    if qty != None:
      self.qty = qty
    else:
      raise Exception("No puede ser cero (o NULL)")

  def view(self) -> None:

    print(self)

  def entry(self, qty:float) -> None:

    if qty != None:
      if qty > 0:
        self.qty += qty
      elif qty < 0:
        raise Exception("No puede ser negativa")
    else:
      raise Exception("No puede ser cero (o NULL)")

  def retire(self, qty:float) -> None:
      
    if qty != None:
        if qty > 0:
              self.qty -= qty
        elif qty < 0:
            raise Exception("No puede ser negativa")
    else:
        raise Exception("No puede ser cero (o NULL)")
#
#
# Punto 8: Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase:
# • Un constructor.
# • Los setters y getters para el nuevo atributo.
# • En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario.
# • Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
# • El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.
#


class Person():

  def __init__(self, name: str = None, olds: int = None, idcard: int = None) -> None:
    self.name = name
    self.olds = olds
    self.idcard = idcard

  def __str__(self) -> str:
    return f"Person (Name:{self.nome}, Olds:{self.olds}, Idcard:{self.idcard})"

  def getName(self) -> str:
    return self.name

  def getOlds(self) -> int:
    return self.olds

  def getIdcard(self) -> int:
    return self.idcard

  def setName(self, nombre: str) -> None:
    if len(name) > 1:
      self.name = name
    else:
      raise Exception("Es obligatorio al menos 2 letras")

  def setOlds(self, olds: int) -> None:
    if olds >= 0 and olds <= 120:
      self.edad = olds
    else:
      raise Exception("La Edad entre 0 y 120 años")

  def setIdcard(self, idcard: int) -> None:
    if idcard >= 1000000 and dni < 100000000:
      self.idcard = idcard
    else:
      raise Exception(
          "El Documento de Identidad entre 7 y 9 dígitos numéricos")

  def view(self) -> None:
    print(self)

  def Mayor(self) -> bool:
    if self.olds == None:
      raise Exception("La persona no es mayor de edad")
    return self.olds >= 21


class Account():

  def __init__(self, owner:Person = None, qty: float = 0.0) -> None:
    self.owner = owner
    self.qty = qty

  def __str__(self) -> str:
    return f"Account (Owner:{self.owner}, Qty:{self.qty})"

  def getOwner(self) -> Person:
    return self.owner

  def getQty(self) -> float:
    return self.qty

  def setOwner(self, owner:Person) -> None:
    if owner != None:
      self.owner = owner
    else:
      raise Exception("No puede estar vacio (o NULL)")

  def setQty(self, qty:float) -> None:
    if qty != None:
      self.qty = qty
    else:
      raise Exception("No puede ser cero (o NULL)")

  def view(self) -> None:

    print(self)

  def entry(self, qty:float) -> None:

    if qty != None:
      if qty > 0:
        self.qty += qty
      elif qty < 0:
        raise Exception("No puede ser negativa")
    else:
      raise Exception("No puede ser cero (o NULL)")

  def retire(self, qty:float) -> None:
      
    if qty != None:
        if qty > 0:
              self.qty -= qty
        elif qty < 0:
            raise Exception("No puede ser negativa")
    else:
        raise Exception("No puede ser cero (o NULL)")
        

class youngAccount(Account):

    def __init__(self,owner,qty,discount):
        super().__init__(owner,qty)
        self.discount = discount

    def getDiscount(self):
        return self.discount
    
    def setOwner(self,value):
        self.discount = value

    def __ownerOk(self):
        if(super().getOwner().olds() and super().getOwner().getOlds() <= 25):
            return True
        else:
            return False
        
    def retire(self,qty):
        if(self.__ownerOk()):
            super().retire(qty)
        else:
            print("No es mayor de edad, no puede retirar dinero.")
    
    
    def view(self):
        print("Cuenta Joven")
        print("Descuento: "+ f'{self.discount}' + "%")
        
    def main():
      person1 = Person("Santiago",41,"29246136")
      person1.viewr()
      youngAccount = youngAccount(person1,1000,35)
      youngAccount.view()
      print(youngAccount.getQty())
      youngAccount.retire(1000)
      print(youngAccount.getQty())

      main()    


#
# Fin.