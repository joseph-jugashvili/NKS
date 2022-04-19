t = 645

intensity = 601

gamma = 0.89

work_hours = [139, 1774, 846, 282, 836, 704, 92, 50, 478,
              573, 311, 1466, 125, 181, 206, 270, 394,
              1854, 39, 34, 425, 631, 361, 115, 841, 1139,
              191, 677, 944, 401, 269, 735, 235, 148, 74,
              371, 324, 635, 421, 925, 195, 229, 276,
              1184, 172, 1017, 323, 658, 183, 769, 516,
              364, 1301, 1699, 71, 74, 143, 1885, 505, 70,
              249, 408, 224, 17, 1197, 86, 834, 127, 121,
              794, 144, 325, 251, 863, 75, 1078, 98, 114,
              226, 489, 250, 323, 505, 0, 151, 219, 169,
              177, 456, 43, 400, 142, 1754, 110, 540, 756,
              1605, 195, 593, 103]

work_hours.sort()

sumed_work_hours = 0
for i in work_hours:
    sumed_work_hours += i
avarage = sumed_work_hours / len(work_hours)

print("Sorted hours: ", work_hours)
print("Avarage: ", avarage)

max_hours = work_hours[-1]
h = work_hours[-1] / 10

print("Max hours: ", max_hours)
print("Length: ", h)

intervals = []
i = 0
for _ in range(11):
    intervals.append(i)
    i += h

print("Intervals: ", intervals)
frequensy_possibilities = []
for i in range(len(intervals) - 1):
    times = []
    for time in work_hours:
        if intervals[i] < time <= intervals[i + 1]:
            times.append(time)
    frequensy_possibilities.append(len(times) / (len(work_hours) * h))
print("Failure probability: ", frequensy_possibilities)

probabilities = []

for time in intervals:
    frequensies = 0
    for i in range(0, int(time // h)):
        frequensies += frequensy_possibilities[i]

    current_frequensy_possibilities = frequensy_possibilities[int(time // h)] if not int(time // h) >= len(
        frequensy_possibilities) else 0
    integral = frequensies * h + current_frequensy_possibilities * (time % h)
    probabilities.append(1 - integral)

print("Probabilities: ", probabilities)

t_y_index = 0
for i in range(len(probabilities)):
    if probabilities[i] <= gamma:
        t_y_index = i
        break

print("T_y index: ", t_y_index)

t_i = t_y_index * h
t_i_decreased = (t_y_index - 1) * h

frequensies_t_i = 0
for i in range(0, int(t_i // h)):
    frequensies_t_i += frequensy_possibilities[i]

integral_t_i = frequensies_t_i * h + frequensy_possibilities[int(t_i // h)] * (t_i % h)

frequensies_t_i_decreased = 0
for i in range(0, int(t_i_decreased // h)):
    frequensies_t_i_decreased += frequensy_possibilities[i]

integral_t_i_decreased = frequensies_t_i_decreased * h + frequensy_possibilities[
    int(frequensies_t_i_decreased // h)] * (t_i_decreased % h)

t_y = t_i - h * (1 - integral_t_i - gamma) / ((1 - integral_t_i) - (1 - integral_t_i_decreased))

print("T_y : ", t_y)

frequensies_t = 0
for i in range(0, int(t // h)):
    frequensies_t += frequensy_possibilities[i]

probability_of_failure_free_operation = 1 - (frequensies_t * h + frequensy_possibilities[int(t // h)] * (t % h))

print("Probability of failure free operation : ", probability_of_failure_free_operation)

intensities = 0
for i in range(0, int(intensity // h)):
    intensities += frequensy_possibilities[i]

failure_intensity = frequensy_possibilities[int(intensity // h)] / (
            1 - (intensities * h + frequensy_possibilities[int(intensity // h)] * (intensity % h)))

print("Failure intensity : ", failure_intensity)
