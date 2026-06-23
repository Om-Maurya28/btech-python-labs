class Student:
    def __init__(self, name, age, marks):
       
        self.name = name
        self.age = age
        self.marks = marks  # list of marks in 5 subjects

    def Evaluate(self):
        total = sum(self.marks)
        percentage = (total / 500) * 100

        print("Total Marks:", total)
        print("Percentage:", percentage, "%")


# ---- Taking input from user ----
try:
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    if age > 25:
            raise ValueError("Error: Age must be 25 or below.")
        
    marks = []
    for i in range(1, 6):
        mark = int(input(f"Enter marks for subject {i}: "))
        marks.append(mark)
    for m in marks:
        if m > 100:
            print("Error: Marks must be 100 or below.")
             

    # Create object
    student1 = Student(name, age, marks)

    # Print details
    print("\nStudent Details")
    print("Name:", student1.name)
    print("Age:", student1.age)
    print("Marks:", student1.marks)

    # Evaluate
    student1.Evaluate()

except ValueError as e:
    print(e)
