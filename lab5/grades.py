import statistics
data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28," \
       "39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83 "
# 1
grades = data.split(",")

# 2
grades[:] = [int(grade) for grade in grades]

minimum = min(grades)
maximum = max(grades)

# 3
grade_av = sum(grades)/len(grades)
average = grade_av.__round__(2)


# 5, 6
mean = statistics.mean(grades)

# 7
med = statistics.median(grades)

print(f"Min: {minimum}, Max: {maximum}, Average: {average}, Mean: {mean}, Median: {med}")

