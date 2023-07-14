class assignment():
    def Subfields():
        print("Sub-fields in AI are:")
        listsubfields=['Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        for val in listsubfields:
                if((val=='Machine Learning')or(val=='Neural Networks')
                   or(val=='Vision')or(val=='Robotics')or(val=='Speech Processing')
                   or(val=='Natural Language Processing')):
                    print(val)
    def OddEven():
        num= int(input("Enter a number: "))
        if((num%2)==0):
            print(num ," is Even number")
        else:
            print(num ," is Odd number")
            
    def Elegible():
        gender="Male"
        age= 20
        print("Your Gender:",gender)
        print("Your Age:",age)
        if(((gender=="Male") or(gender=="Female")) and (age<=20)):
            print("NOT ELIGIBLE")
        elif(((gender=="Male") or(gender=="Female")) and (age<=40)):
            print("ELIGIBLE")
        else:
            print("Please enter the valid input")
            
    def percentage():
        Sub1= 98
        Sub2= 87
        Sub3= 95
        Sub4= 95
        Sub5= 93
        print("Subject1= ",Sub1)
        print("Subject2= ",Sub2)
        print("Subject3= ",Sub3)
        print("Subject4= ",Sub4)
        print("Subject5= ",Sub5)
        Totalmarks= Sub1+Sub2+Sub3+Sub4+Sub5
        print("Total :  ",Totalmarks)
        percentageval= Totalmarks/5
        print("Percentage : ",percentageval)
        
    def triangle():
        height=32
        breadth=34
        height1=2
        height2= 4
        breadth2=4
        print("Height:",height)
        print("Breadth:",breadth)
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ", (height*breadth)/2)
        print("Height1:",height1)
        print("Height2:",height2)
        print("Breadth:",breadth2)
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",height1+height2+breadth2)