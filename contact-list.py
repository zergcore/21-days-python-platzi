# En este desafío, debes construir una lista de contactos mediante una hash table.

# Tu objetivo será implementar la lógica de la clase ContactList para agregar contactos y realizar las operaciones correspondientes.

# La hash table (ContactList) deberá tener los siguientes métodos:

# insert(name, phone): este método recibirá el nombre y el número de teléfono de un contacto y agregará este último a la hash table.

# get(name): este método recibirá el nombre de un contacto y devolverá su número de teléfono. Si el contacto no existe, retornará None.

# retrieveAll(): este método devolverá una lista con todos los buckets utilizados en la hash table.

# delete(name): este método recibirá el nombre de un contacto y eliminará dicho contacto de la hash table. En caso de no encontrar el nombre, debe retornar None.

# El código original ya tiene una implementación del método hash, por lo que no tienes que preocuparte por ello.

# Ejemplo 1:

# Input
# contactList = ContactList(10)
# contactList.insert("Mr michi", "123-456-7890")

# contactList.retrieveAll()

# Output: [["Mr michi", "123-456-7890"]]

# Ejemplo 2:

# Input:
# contactList = ContactList(10)
# contactList.insert("Mr michi", "123-456-7890")

# contactList.get("Mr Michi")

# Output: "123-456-7890"

# Ejemplo 3:

# Input:
# contactList = ContactList(10)
# contactList.insert("Mr michi", "123-456-7890")
# contactList.delete("Mr michi")

# contactList.get("Mr Michi")

# Output: None

class ContactList:
  def __init__(self, size):
    self.buckets = [None] * size
    self.numBuckets = size

  def hash(self, key):
    total = 0
    for char in key:
      total += ord(char)
    return total % self.numBuckets

  def insert(self, name, phone):
    index = self.hash(name)
    if self.buckets[index] is None:
      self.buckets[index] = []
    for i, contact in enumerate(self.buckets[index]):
      if contact[0] == name:
        self.buckets[index][i] = [name, phone]
        return
    self.buckets[index].append([name, phone])

  def get(self, name):
    index = self.hash(name)
    if self.buckets[index] is not None:
      for contact in self.buckets[index]:
        if contact[0] == name:
          return contact[1]
    return None

  def retrieveAll(self):
    allBuckets = []
    for bucket in self.buckets:
      if bucket is not None:
        allBuckets.extend(bucket)
    return allBuckets

  def delete(self, name):
    index = self.hash(name)
    if self.buckets[index] is not None:
      for i, contact in enumerate(self.buckets[index]):
        if contact[0] == name:
          del self.buckets[index][i]
          return
    return None

# Ejemplo 1
contactList = ContactList(10)
contactList.insert("Mr michi", "123-456-7890")
print(contactList.retrieveAll())