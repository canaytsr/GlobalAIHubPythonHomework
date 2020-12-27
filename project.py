name="ellie"
surname="green"

Courses_list=["English","Math" ,"Chemistry" ,"Biology", "Physics"]
#dict = {}

def PassOrFail(m,f,p):
    ort=(m*30/100)+(f*50/100)+(p*20/100)
    if ort>=90:
        return "AA"
    elif ort<90 and ort>=70:
        return "BB"
    elif ort<70 and ort>=50:
        return "CC"
    elif ort<50 and ort>=30:
        return "DD"
    else:
        return "FF"
        
selected_list=[]
grade_list=[]
false=0

while false<3:
    input_name=input("Enter your name:")
    input_surname=input("Enter your surname:")
    if name==input_name.lower() and surname==input_surname.lower():
        print("Welcome "+name.capitalize()+" "+surname.capitalize())
        number_of_courses=int(input("How Many Add Courses:"))
        if number_of_courses>=3 and number_of_courses<=5:
            for i in range(number_of_courses):
                print(Courses_list)
                course=input("Enter course:")
                selected_list.append(course.capitalize())
        
                m=int (input("Enter Midterm Grade:"))
                f=int (input("Enter Final Grade:"))
                p=int (input("Enter Project Grade:"))
                grade_list.append(PassOrFail(m,f,p))
            D=dict(zip(selected_list, grade_list))
            #print(D)
            print("**Taken Courses And Grades**")
            for key in D:
                print(" ",key, ':', D[key],end="\n")
            break        
                
        elif number_of_courses<3:
            print("You Failed In Class")
                
        else:
            print("Your Value Should Be Less Than 5")
      
    else:
        print("Wrong name or surname")
        false=false+1

if false==3:
    print("Please Try Again Later")
