
# Простой To-Do List на Python

tasks = []

while True:
    print("\nСписок задач:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    task = input("Введите новую задачу (или 'выход' для завершения): ")
    
    if task.lower() == 'выход':
        break
    
    tasks.append(task)
    print(f"Задача '{task}' добавлена!")
