# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20210160 / w1912822
# Date: 25/03/2022

#Create veriables
Pass=0
defer=0
fail=0
option=0
progress=0
trailer=0
retriever=0
excluded=0
total_outcome=0
pro_count = 0
trail_count=0
retri_count=0
exclude_count=0




#process
def student():
    global pro_count,trail_count,retri_count,exclude_count
    rlist=[0,20,40,60,80,100,120]

            
    while True: #identyfing the values enterd by user is in the relevant range
        try:
            Pass=int(input("Please enter your credits at pass : "))

        except ValueError:
            print("Integer required") #when user input is not an int

        else:
            if Pass not in rlist:
                print("Out of range") #when user input is no in rlist
            else:
                break

    while True:
        try:
            defer=int(input("Please enter your credits at defer : "))
        except ValueError:
            print("Integer required")

        else:
            if defer not in rlist:
                print("Out of range")
            else:
                break

    while True:
        try:
            fail=int(input("Please enter your credits at fail : "))
        except ValueError:
            print("Integer required")

        else:
            if fail not in rlist:
                print("Out of range")
            else:
                break
            
    
    total = Pass + defer + fail
    if total != 120:
        print("Total incorrect")#when  the sum of the pass,defer and fail  is over 120
        student() #calling function
    
               
    if Pass==120:
        print("Progress")
        pro_count+=1
    elif fail>=80:
        print("Exclude")
        exclude_count+=1
    elif Pass==100:
        print("Progress(module trailer)")
        trail_count +=1
    else:
        print("Do not progress - modile retriever")
        retri_count+=1
     

def staff():
    while True:
        global pro_count,trail_count,retri_count,exclude_count
        student() #calling the fnction
        total_outcome=pro_count+trail_count+retri_count+exclude_count     
        print('Would you like to enter another set of data?')
        option=input("Enter 'y' for yes or 'q' to quit and view results : ") #Ask the user to continue or quit the program.

        if option=='y':
            print()
            continue
        elif option=='q':
            print(' _ '*20)
            print()
            print('Horizontal Histogram')
            print('Progress',pro_count,' :','*'*pro_count)      #print horizontal histrogram
            print('Trailer',trail_count,'  :','*'*trail_count)
            print('Retriever',retri_count,':','*'*retri_count)
            print('Excluded',exclude_count,' :','*'*exclude_count)
            print()
            print(total_outcome,'outcomes in total.') #print total_outcome 
            print(' _ '*20)
            break
        else:
            print('Invalid input. Please try again with valid inputs!!') #If the user inputs without q or y, display an error message.
            break

#creat a menu
print("student version: 1\nStaff version : 2")
version =input("Select student version or Staff version: ")
if version == '1':
    student()
elif version == '2':
    staff()
else:
    print("Invalid input")
