# En este desafío, implementarás la lógica de un planificador de tareas en Python. El objetivo es construir la función closure llamada createTaskPlanner, que devolverá una serie de métodos para administrar las tareas. A continuación, se detallan los métodos que deben implementarse:

# addTask(task): recibe un diccionario que contiene la información de la tarea y la agrega al array de tareas. El diccionario debe contener las siguientes claves: 'id', 'name', 'priority', 'tags' y 'completed'. La clave 'completed' se establecerá automáticamente como False al agregar una tarea.

# removeTask(value): recibe el id o nombre de la tarea y la elimina del array de tareas.

# getTasks(): devuelve el array de tareas.

# getPendingTasks(): devuelve solo las tareas pendientes.

# getCompletedTasks(): devuelve solo las tareas completadas.

# markTaskAsCompleted(value): recibe el id o nombre de la tarea y la marca como completada.

# getSortedTasksByPriority(): devuelve una copia de las tareas ordenadas según su prioridad (3: poco urgente, 2: urgente, 1: muy urgente), sin modificar la lista original de tareas.

# filterTasksByTag(tag): filtra las tareas por una etiqueta específica. updateTask(taskId, updates): busca la tarea correspondiente al id especificado y actualiza sus propiedades con las especificadas en el diccionario de actualizaciones.

# Ejemplo 1:

# Input: 

# planner = createTaskPlanner()

# planner['addTask']({
#     'id': 1,
#     'name': 'Comprar leche',
#     'priority': 1,
#     'tags': ['shopping', 'home']
# })

# planner['addTask']({
#     'id': 2,
#     'name': 'Llamar a Juan',
#     'priority': 3,
#     'tags': ['personal']
# })

# planner['markTaskAsCompleted']('Llamar a Juan')

# print(planner['getCompletedTasks']())

# Output:

# [{
#   'id': 2,
#   'name': 'Llamar a Juan',
#   'completed': True,
#   'priority': 3,
#   'tags': ['personal']
# }]

# Ejemplo 2:


# Input:
# planner = createTaskPlanner()

# planner['addTask']({
#     'id': 1,
#     'name': 'Comprar leche',
#     'priority': 1,
#     'tags': ['shopping', 'home']
# })

# planner['addTask']({
#     'id': 2,
#     'name': 'Llamar a Juan',
#     'priority': 3,
#     'tags': ['personal']
# })

# print(planner['filterTasksByTag']('shopping'))

# Output:

# [{
#     'id': 1,
#     'name': 'Comprar leche',
#     'completed': False,
#     'priority': 1,
#     'tags': ['shopping', 'home']
# }]

def createTaskPlanner():
  tasks = list()

  def addTask(task):
    if len(set(['id', 'name', 'priority', 'tags']) & set(task.keys())) == 4:
      new_task = task.copy()
      new_task['completed'] = False
      tasks.append(new_task)


  def removeTask(value):
    if isinstance(value, int):
      tasks[:] = [task for task in tasks if task['id'] != value]
    elif isinstance(value, str):
      tasks[:] = [task for task in tasks if task['name'] != value]

  def getTasks():
    return tasks
  
  def getPendingTasks():
    pendingTasks = [task for task in tasks if not task['completed']]
    return pendingTasks
  
  def getCompletedTasks():
    return [task for task in tasks if task["completed"]]
  
  def markTaskAsCompleted(value):
    if isinstance(value, int):
      for task in tasks:
        if task['id'] == value:
          task['completed'] = True
          break
    elif isinstance(value, str):
      for task in tasks:
        if task['name'] == value:
          task['completed'] = True
          break
  
  def getSortedTasksByPriority():
    return sorted(tasks, key=lambda task: task['priority'])
  
  def filterTasksByTag(tag):
    return [task for task in tasks if tag in task["tags"]]
  
  def updateTask(taskId, updates):
    for task in tasks:
      if task['id'] == taskId:
        task.update(updates)
        break
  
  return {
    'addTask': addTask,
    'removeTask':removeTask,
    'getTasks':getTasks,
    'getPendingTasks':getPendingTasks,
    'getCompletedTasks':getCompletedTasks,
    'markTaskAsCompleted':markTaskAsCompleted,
    'getSortedTasksByPriority': getSortedTasksByPriority,
    'filterTasksByTag': filterTasksByTag,
    'updateTask': updateTask,
    }

planner = createTaskPlanner()

planner['addTask']({
    'id': 1,
    'name': 'Comprar leche',
    'priority': 1,
    'tags': ['shopping', 'home']
})

planner['addTask']({
    'id': 2,
    'name': 'Llamar a Juan',
    'priority': 3,
    'tags': ['personal']
})

# planner['removeTask'](1)

print(planner['getTasks']())

print(planner['getPendingTasks']())

print(planner['getCompletedTasks']())

planner['markTaskAsCompleted']('Llamar a Juan')

print(planner['getCompletedTasks']())

print(planner['filterTasksByTag']('shopping'))