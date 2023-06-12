from datetime import datetime, timedelta

def find_top_employee(messages):
    message_counts = {}

    current_time = datetime.now()

    last_week = current_time - timedelta(days=7)

    for message in messages:
        employee = message['employee']
        timestamp = message['timestamp']

        if timestamp >= last_week:
            if employee in message_counts:
                message_counts[employee] += 1
            else:
                message_counts[employee] = 1

    # Найти сотрудника с наибольшим количеством сообщений
    top_employee = max(message_counts, key=message_counts.get)
    message_count = message_counts[top_employee]

    return top_employee, message_count

messages = [
    {'employee': 'Biba', 'timestamp': datetime(2023, 6, 1, 8, 30)},
    {'employee': 'Alexander', 'timestamp': datetime(2023, 6, 2, 10, 15)},
    {'employee': 'Biba', 'timestamp': datetime(2023, 6, 3, 14, 45)},
    {'employee': 'Dmitrii', 'timestamp': datetime(2023, 6, 4, 9, 0)},
    {'employee': 'Alexander', 'timestamp': datetime(2023, 6, 4, 11, 30)},
    {'employee': 'Dmitrii', 'timestamp': datetime(2023, 6, 5, 16, 20)},
    {'employee': 'Biba', 'timestamp': datetime(2023, 6, 6, 13, 10)},
    {'employee': 'Alexander', 'timestamp': datetime(2023, 6, 7, 9, 45)},
    {'employee': 'Dmitrii', 'timestamp': datetime(2023, 6, 7, 11, 0)}
]

top_employee, message_count = find_top_employee(messages)
print("Наибольшее количество сообщений получил сотрудник:", top_employee)
print("Количество сообщений:", message_count)
