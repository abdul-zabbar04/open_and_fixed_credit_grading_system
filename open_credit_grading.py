print("1. EEE")
print("2. CSE")
print("3. ME")
print("4. CE")
print("5. BBA")
dept= int(input("Select your department: "))
from functions import Check_CT, Check_Midterm, Check_Final, Subject_GPA
# EEE Department
if dept==1:
    # Subject 1
    print("Enter your Electrical Circuits course marks.")
    ct= int(input("CT marks(out of 20):"))
    checked= Check_CT(ct)
    if checked == False:
        print("Invalid CT marks")
        exit()

    mid= int(input("Midterm marks(out of 30):"))
    checked= Check_Midterm(mid)
    if checked == False:
        print("Invalid Midterm marks")
        exit()
    final= int(input("Final marks(out of 50):"))
    checked= Check_Final(final)
    if checked == False:
        print("Invalid Final marks")
        exit()
    total= ct+mid+final
    from functions import Grade_Point
    gpa1= Grade_Point(total)
    print("Your grade point in Electrical Circuits is:", gpa1)

    # Subject 2
    print("Enter your Electronic Circuits course marks.")
    ct= int(input("CT marks(out of 20):"))
    checked= Check_CT(ct)
    if checked == False:
        print("Invalid CT marks")
        exit()

    mid= int(input("Midterm marks(out of 30):"))
    checked= Check_Midterm(mid)
    if checked == False:
        print("Invalid Midterm marks")
        exit()
    final= int(input("Final marks(out of 50):"))
    checked= Check_Final(final)
    if checked == False:
        print("Invalid Final marks")
        exit()
    total= ct+mid+final
    from functions import Grade_Point
    gpa2= Grade_Point(total)
    print("Your grade point in Electronic Circuits is:", gpa2)

    # Subject 3
    print("Enter your Machine course marks.")
    ct= int(input("CT marks(out of 20):"))
    checked= Check_CT(ct)
    if checked == False:
        print("Invalid CT marks")
        exit()

    mid= int(input("Midterm marks(out of 30):"))
    checked= Check_Midterm(mid)
    if checked == False:
        print("Invalid Midterm marks")
        exit()
    final= int(input("Final marks(out of 50):"))
    checked= Check_Final(final)
    if checked == False:
        print("Invalid Final marks")
        exit()
    total= ct+mid+final
    from functions import Grade_Point
    gpa3= Grade_Point(total)
    print("Your grade point in Machine is:", gpa3)

    # Subject 4
    print("Enter your Power System course marks.")
    ct= int(input("CT marks(out of 20):"))
    checked= Check_CT(ct)
    if checked == False:
        print("Invalid CT marks")
        exit()

    mid= int(input("Midterm marks(out of 30):"))
    checked= Check_Midterm(mid)
    if checked == False:
        print("Invalid Midterm marks")
        exit()
    final= int(input("Final marks(out of 50):"))
    checked= Check_Final(final)
    if checked == False:
        print("Invalid Final marks")
        exit()
    total= ct+mid+final
    from functions import Grade_Point
    gpa4= Grade_Point(total)
    print("Your grade point in Power System is:", gpa4)

    # Subject 5
    print("Enter your VLSI course marks.")
    ct= int(input("CT marks(out of 20):"))
    checked= Check_CT(ct)
    if checked == False:
        print("Invalid CT marks")
        exit()

    mid= int(input("Midterm marks(out of 30):"))
    checked= Check_Midterm(mid)
    if checked == False:
        print("Invalid Midterm marks")
        exit()
    final= int(input("Final marks(out of 50):"))
    checked= Check_Final(final)
    if checked == False:
        print("Invalid Final marks")
        exit()
    total= ct+mid+final
    from functions import Grade_Point
    gpa5= Grade_Point(total)
    print("Your grade point in VLSI is:", gpa5)

    # average CGPA calculation
    avg_gpa= (gpa1+gpa2+gpa3+gpa4+gpa5)/5
    print("Your average CGPA is:", avg_gpa)

# CSE Department
elif dept==2:
    # Subject 1
    print("Enter your Data Structures course marks.")
    gpa1= Subject_GPA()
    print("Your grade point in Data Structures is:", gpa1)

    # Subject 2
    print("Enter your Algorithms course marks.")
    gpa2= Subject_GPA()
    print("Your grade point in Algorithms is:", gpa2)

    # Subject 3
    print("Enter your Database Systems course marks.")
    gpa3= Subject_GPA()
    print("Your grade point in Database Systems is:", gpa3)

    # Subject 4
    print("Enter your Operating Systems course marks.")
    gpa4= Subject_GPA()
    print("Your grade point in Operating Systems is:", gpa4)

    # Subject 5
    print("Enter your Computer Networks course marks.")
    gpa5= Subject_GPA()
    print("Your grade point in Computer Networks is:", gpa5)

    # average CGPA calculation
    avg_gpa= (gpa1+gpa2+gpa3+gpa4+gpa5)/5
    print("Your average CGPA is:", avg_gpa)
# ME Department
elif dept==3:
    # Subject 1
    print("Enter your Thermodynamics course marks.")
    gpa1= Subject_GPA()
    print("Your grade point in Thermodynamics is:", gpa1)
    # Subject 2
    print("Enter your Fluid Mechanics course marks.")
    gpa2= Subject_GPA()
    print("Your grade point in Fluid Mechanics is:", gpa2)
    # Subject 3
    print("Enter your Machine Design course marks.")
    gpa3= Subject_GPA()
    print("Your grade point in Machine Design is:", gpa3)
    # Subject 4
    print("Enter your Manufacturing Processes course marks.")
    gpa4= Subject_GPA()
    print("Your grade point in Manufacturing Processes is:", gpa4)
    # Subject 5
    print("Enter your Heat Transfer course marks.")
    gpa5= Subject_GPA()
    print("Your grade point in Heat Transfer is:", gpa5)
    # average CGPA calculation
    avg_gpa= (gpa1+gpa2+gpa3+gpa4+gpa5)/5
    print("Your average CGPA is:", avg_gpa)

# CE Department
elif dept==4:
    # Subject 1
    print("Enter your Structural Analysis course marks.")
    gpa1= Subject_GPA()
    print("Your grade point in Structural Analysis is:", gpa1)
    # Subject 2
    print("Enter your Geotechnical Engineering course marks.")
    gpa2= Subject_GPA()
    print("Your grade point in Geotechnical Engineering is:", gpa2)
    # Subject 3
    print("Enter your Transportation Engineering course marks.")
    gpa3= Subject_GPA()
    print("Your grade point in Transportation Engineering is:", gpa3)
    # Subject 4
    print("Enter your Environmental Engineering course marks.")
    gpa4= Subject_GPA()
    print("Your grade point in Environmental Engineering is:", gpa4)
    # Subject 5
    print("Enter your Hydraulics course marks.")
    gpa5= Subject_GPA()
    print("Your grade point in Hydraulics is:", gpa5)
    # average CGPA calculation
    avg_gpa= (gpa1+gpa2+gpa3+gpa4+gpa5)/5
    print("Your average CGPA is:", avg_gpa)

# BBA Department
elif dept==5:
    # Subject 1
    print("Enter your Marketing course marks.")
    gpa1= Subject_GPA()
    print("Your grade point in Marketing is:", gpa1)
    # Subject 2
    print("Enter your Finance course marks.")
    gpa2= Subject_GPA()
    print("Your grade point in Finance is:", gpa2)
    # Subject 3
    print("Enter your Human Resource Management course marks.")
    gpa3= Subject_GPA()
    print("Your grade point in Human Resource Management is:", gpa3)
    # Subject 4
    print("Enter your Accounting course marks.")
    gpa4= Subject_GPA()
    print("Your grade point in Accounting is:", gpa4)
    # Subject 5
    print("Enter your Business Law course marks.")
    gpa5= Subject_GPA()
    print("Your grade point in Business Law is:", gpa5)
    # average CGPA calculation
    avg_gpa= (gpa1+gpa2+gpa3+gpa4+gpa5)/5
    print("Your average CGPA is:", avg_gpa)

else:
    print("Invalid Department Selection")