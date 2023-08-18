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