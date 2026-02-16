age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ") == "yes"
is_student = input("Are you a student? (yes/no): ") == "yes"

can_enter = (age >= 18 and has_ticket) or is_student

print("Age:", age)
print("Has ticket:", has_ticket)
print("Is student:", is_student)
print("Can enter:", can_enter)