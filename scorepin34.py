print("=== Student Score Evaluation Program (>-<) ===")

math = int(input("Enter Mathematics score (Integer): "))
science = int(input("Enter Science score (Integer): "))
english = int(input("Enter English score (Integer): "))

total = math + science + english
print(f"Total Score: {total}")

average = total / 3
print(f"Average Score: {average:.2f}")

if average < 60:
    print("Performance Level: Needs Improvement")
elif average < 80:
    print("Performance Level: Pass")
else:
    print("Performance Level: Excellent")

print("Programmer: [Warissara]")
