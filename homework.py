# Get grades for 6 subjects
g1 = float(input("Grade for subject 1: "))
g2 = float(input("Grade for subject 2: "))
g3 = float(input("Grade for subject 3: "))
g4 = float(input("Grade for subject 4: "))
g5 = float(input("Grade for subject 5: "))
g6 = float(input("Grade for subject 6: "))

# Calculate average
avg = (g1 + g2 + g3 + g4 + g5 + g6) / 6
print("Average:", avg)

# Check reward
if 18 <= avg <= 20:
    print("Prize: PlayStation!")
elif 16 <= avg < 18:
    print("Prize: Bicycle!")
else:
    print("Sorry, no prize!")
