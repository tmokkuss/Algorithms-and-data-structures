from collections import Counter

all_p = []
current_vessel = []
while True:
    try:
        num = input().strip()
        if num == '-1':
            all_p += current_vessel
            current_vessel = []
        elif num == '':
            break
        else:
            current_vessel.append(num)
    except:
        break


counts = Counter(all_p)

unique_particles = [particle for particle, count in counts.items() if count == 1]
print(counts)
print(' '.join(unique_particles))
