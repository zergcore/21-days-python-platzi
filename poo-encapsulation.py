# En este desafío, debes implementar la lógica de la clase "Usuario" que represente un usuario en una red social y utilizar encapsulamiento para proteger sus datos privados.

# La clase debe tener las siguientes variables privadas:

# name
# age
# friends (lista de diccionarios Usuario)
# messages (lista de strings)
# Además, debes proporcionar los siguientes métodos públicos:

# addFriend(friend): agrega un usuario a la lista de amigos del usuario actual.
# sendMessage(message, friend): agrega un mensaje a la lista de mensajes del usuario actual y al amigo especificado.
# showMessages(): devuelve la lista de mensajes del usuario actual.
# También debes tener definidos los getters y setters para acceder a los datos privados como el nombre y la edad, los cuales pueden ser modificados mediante su propio setter.

# Ejemplo 1:

# Input:

# usuario1 = User("Juan", 20)
# usuario2 = User("Maria", 25)
# usuario1.addFriend(usuario2)
# usuario1.sendMessage("Hola Maria!", usuario2)

# usuario1.showMessages()

# Output:

# ["Hola Maria!"]

# Ejemplo 2:

# Input:

# usuario1 = User("Juan", 20)
# usuario1.name = "Pepito"
# print(usuario1.name)

# Output:

# "Pepito"

class User:
  def __init__(self, name, age):
    self.__name = name
    self.__age = age
    self.__friends = []
    self.__messages = []

  def addFriend(self, friend):
    self.__friends.append(friend)
  
  def sendMessage(self, message, friend):
    self.__messages.append(message)
    friend.__messages.append(message)
  
  def showMessages(self):
    return self.__messages

  @property
  def name(self):
    return self.__name

  @property 
  def age(self):
    return self.__age

  @name.setter
  def name(self, name):
    self.__name = name

  @age.setter
  def age(self, age):
    self.__age = age

usuario1 = User("Juan", 20)
usuario2 = User("Maria", 25)
usuario1.addFriend(usuario2)
usuario1.sendMessage("Hola Maria!", usuario2)

print(usuario1.showMessages())
