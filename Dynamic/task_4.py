def select_tasks(tasks):
    sorted_tasks = sorted(tasks, key=lambda x: x[1])  # Сортировка задач по возрастанию временных ограничений
    selected_tasks = []
    end_time = 0

    for task in sorted_tasks:
        if task[0] >= end_time:  # Проверка на пересечение с предыдущими задачами
            selected_tasks.append(task)
            end_time = task[1]

    return selected_tasks

n = int(input("Введите количество задач: "))
tasks = []

for i in range(n):
    start_time, end_time = map(int, input("Введите временные ограничения задачи {}: ".format(i + 1)).split())
    tasks.append((start_time, end_time))

result = select_tasks(tasks)
print("Результирующее подмножество задач:")
for task in result:
    print("Время выполнения: {}-{}".format(task[0], task[1]))
