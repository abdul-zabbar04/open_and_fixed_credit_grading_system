print("1. EEE")
print("2. CSE")
print("3. ME")
print("4. CE")
print("5. BBA")
dept= int(input("Select your department: "))
from functions import Subject_GPA, Calculate_CGPA
# EEE Department
if dept==1:
    # Subject 1
    print("Enter your Electrical Circuits course marks(Credit: 6).")
    gpa1= Subject_GPA()
    print("Your grade point in Electrical Circuits is:", gpa1)

    # Subject 2
    print("Enter your Electronic Circuits course marks(Credit: 6).")
    gpa2= Subject_GPA()
    print("Your grade point in Electronic Circuits is:", gpa2)

    # Subject 3
    print("Enter your Machine course marks(Credit: 6).")
    gpa3= Subject_GPA()
    print("Your grade point in Machine is:", gpa3)

    # Subject 4
    print("Enter your Power System course marks(Credit: 6).")
    gpa4= Subject_GPA()
    print("Your grade point in Power System is:", gpa4)

    # Subject 5
    print("Enter your VLSI course marks(Credit: 3).")
    gpa5= Subject_GPA()
    print("Your grade point in VLSI is:", gpa5)

    # average CGPA calculation
    avg_cgpa= Calculate_CGPA(gpa1, 6, gpa2, 6, gpa3, 6, gpa4, 6, gpa5, 3)
    print("Your average CGPA is:", avg_cgpa)

# CSE Department
elif dept==2:
    # Subject 1
    print("Enter your Data Structures course marks(Credit: 3).")
    gpa1= Subject_GPA()
    print("Your grade point in Data Structures is:", gpa1)

    # Subject 2
    print("Enter your Algorithms course marks(Credit: 3).")
    gpa2= Subject_GPA()
    print("Your grade point in Algorithms is:", gpa2)

    # Subject 3
    print("Enter your Database Systems course marks(Credit: 2).")
    gpa3= Subject_GPA()
    print("Your grade point in Database Systems is:", gpa3)

    # Subject 4
    print("Enter your Operating Systems course marks(Credit: 2).")
    gpa4= Subject_GPA()
    print("Your grade point in Operating Systems is:", gpa4)

    # Subject 5
    print("Enter your Computer Networks course marks(Credit: 3).")
    gpa5= Subject_GPA()
    print("Your grade point in Computer Networks is:", gpa5)

    # average CGPA calculation
    avg_cgpa= Calculate_CGPA(gpa1, 3, gpa2, 3, gpa3, 2, gpa4, 2, gpa5, 3)
    print("Your average CGPA is:", avg_cgpa)
# ME Department
elif dept==3:
    # Subject 1
    print("Enter your Thermodynamics course marks(Credit: 3).")
    gpa1= Subject_GPA()
    print("Your grade point in Thermodynamics is:", gpa1)
    # Subject 2
    print("Enter your Fluid Mechanics course marks(Credit: 4).")
    gpa2= Subject_GPA()
    print("Your grade point in Fluid Mechanics is:", gpa2)
    # Subject 3
    print("Enter your Machine Design course marks(Credit: 2).")
    gpa3= Subject_GPA()
    print("Your grade point in Machine Design is:", gpa3)
    # Subject 4
    print("Enter your Manufacturing Processes course marks(Credit: 3).")
    gpa4= Subject_GPA()
    print("Your grade point in Manufacturing Processes is:", gpa4)
    # Subject 5
    print("Enter your Heat Transfer course marks(Credit: 2).")
    gpa5= Subject_GPA()
    print("Your grade point in Heat Transfer is:", gpa5)
    # average CGPA calculation
    avg_cgpa= Calculate_CGPA(gpa1, 3, gpa2, 4, gpa3, 2, gpa4, 3, gpa5, 2)
    print("Your average CGPA is:", avg_cgpa)

# CE Department
elif dept==4:
    # Subject 1
    print("Enter your Structural Analysis course marks(Credit: 4).")
    gpa1= Subject_GPA()
    print("Your grade point in Structural Analysis is:", gpa1)
    # Subject 2
    print("Enter your Geotechnical Engineering course marks(Credit: 3).")
    gpa2= Subject_GPA()
    print("Your grade point in Geotechnical Engineering is:", gpa2)
    # Subject 3
    print("Enter your Transportation Engineering course marks(Credit: 3).")
    gpa3= Subject_GPA()
    print("Your grade point in Transportation Engineering is:", gpa3)
    # Subject 4
    print("Enter your Environmental Engineering course marks(Credit: 2).")
    gpa4= Subject_GPA()
    print("Your grade point in Environmental Engineering is:", gpa4)
    # Subject 5
    print("Enter your Hydraulics course marks(Credit: 3).")
    gpa5= Subject_GPA()
    print("Your grade point in Hydraulics is:", gpa5)
    # average CGPA calculation
    avg_cgpa= Calculate_CGPA(gpa1, 4, gpa2, 3, gpa3, 3, gpa4, 2, gpa5, 3)
    print("Your average CGPA is:", avg_cgpa)

# BBA Department
elif dept==5:
    # Subject 1
    print("Enter your Marketing course marks(Credit: 3).")
    gpa1= Subject_GPA()
    print("Your grade point in Marketing is:", gpa1)
    # Subject 2
    print("Enter your Finance course marks(Credit: 3).")
    gpa2= Subject_GPA()
    print("Your grade point in Finance is:", gpa2)
    # Subject 3
    print("Enter your Human Resource Management course marks(Credit: 4).")
    gpa3= Subject_GPA()
    print("Your grade point in Human Resource Management is:", gpa3)
    # Subject 4
    print("Enter your Accounting course marks(Credit: 3).")
    gpa4= Subject_GPA()
    print("Your grade point in Accounting is:", gpa4)
    # Subject 5
    print("Enter your Business Law course marks(Credit: 3).")
    gpa5= Subject_GPA()
    print("Your grade point in Business Law is:", gpa5)
    # average CGPA calculation
    avg_cgpa= Calculate_CGPA(gpa1, 3, gpa2, 3, gpa3, 4, gpa4, 3, gpa5, 3)
    print("Your average CGPA is:", avg_cgpa)

else:
    print("Invalid Department Selection")