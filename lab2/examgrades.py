score = int(input('Input Student Score: '))

if 0 > score or score > 100:
    print("Must choose a number between 0 and 100")

if score < 50:
    print("FAILED!")
elif score <= 60:
    print("Pass!")
elif score <= 70:
    print("Merit")
else:
    print("Distinction")
