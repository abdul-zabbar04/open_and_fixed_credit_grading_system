def Check_CT(marks):
    if marks < 0 or marks > 20:
        return False
    return True

def Check_Midterm(marks):
    if marks < 0 or marks > 30:
        return False
    return True

def Check_Final(marks):
    if marks < 0 or marks > 50:
        return False
    return True

# Subject wise grade point function
def Grade_Point(total_marks):
    if total_marks >= 80:
        return 4.00
    elif total_marks >= 75:
        return 3.75
    elif total_marks >= 70:
        return 3.50
    elif total_marks >= 65:
        return 3.25
    elif total_marks >= 60:
        return 3.00
    elif total_marks >= 55:
        return 2.75
    elif total_marks >= 50:
        return 2.50
    elif total_marks >= 45:
        return 2.25
    elif total_marks >= 40:
        return 2.00
    else:
        return 0.00
    
# Function to get GPA for a subject
def Subject_GPA():
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
    gpa= Grade_Point(total)
    return gpa

def Calculate_CGPA(gpa1, credit1, gpa2, credit2, gpa3, credit3, gpa4, credit4, gpa5, credit5):
    total_quality_points = (gpa1 * credit1) + (gpa2 * credit2) + (gpa3 * credit3) + (gpa4 * credit4) + (gpa5 * credit5)
    total_credits = credit1 + credit2 + credit3 + credit4 + credit5
    cgpa = total_quality_points / total_credits
    return cgpa


