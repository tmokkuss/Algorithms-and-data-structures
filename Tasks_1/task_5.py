today_weather = input()
p_sunny_after_sunny = float(input())
p_cloudy_after_cloudy = float(input())
days = int(input())

if today_weather == 'ясно':
    current_p = [1, 0]
else:
    current_p = [0, 1]

for i in range(days):
    next_p = [p_sunny_after_sunny * current_p[0] + (1 - p_cloudy_after_cloudy) * current_p[1],
              (1 - p_sunny_after_sunny) * current_p[0] + p_cloudy_after_cloudy * current_p[1]]
    current_p = next_p

if current_p[0] > current_p[1]:
    print('ясно', current_p[0])
elif current_p[0] < current_p[1]:
    print('пасмурно', current_p[1])
else:
    print('равновероятно')
