#representing tridoku in the format top,left,middle,right
vertices=[[[0,2,3,0],'T'],[[0,4,1,2],'L'],[[3,4,2,1],'M'],[[2,1,4,0],'R']]

#global variables for displaying entered values
global Apple
Apple="_"
global Mango
Mango="_"
global Pear
Pear="_"
global Grapes
Grapes="_"

#to display pramid
display=[["Apple"],[2,3,"Mango"],["Grapes",4,2,1,2],[4,1,2,3,1,4,"Pear"]]

side_tri=[]

#printing the pyramid
def printit():
    indent=4
    for i in range(len(display)):
        print(' '*(indent-(i+1)),end='')
        for j in display[i]:

            print(j,'',end='')
            
        print('\n')
    print("\nApple: ",Apple,"\nMango: ",Mango,"\nPear: ",Pear,"\nGrapes: ",Grapes,"\n")

#Findig the values at the border of tridoku's three faces
def side_triangles(face):
    
    new=[]
    if face=="left":
        for i in vertices:
            if i[1]=='T' or i[1]=='L':
                new.append(i[0][0])  
                new.append(i[0][1])
               

    elif face=="right":
        for i in vertices:
            if i[1]=='T' or i[1]=='R':
                new.append(i[0][0])
                new.append(i[0][3])
                

    elif face=="bottom":
        for i in vertices:
            if i[1]=='L' or i[1]=='R':
                new.append(i[0][1])
                new.append(i[0][3])
               
       
    side_tri.append(new)


#check whether value for a blank is appropriate
def check_add(position,value,side1,side2=0):
    if value in side_tri[side1]:
            
                
            print("Sorry cannot add number")
            return(False)
    else:
        if side2!=0:
            if value in side_tri[side1]:
            
                
                print("Sorry cannot add number")
                return(False)
            
    
    if value in vertices[position][0]:
            print("Sorry cannot add element")
            return(False)
    print("Number added successfully")
    return(True)

#add values if appropriate 
def add():
    print("\n\t1.Apple\n\t2.Mango\n\t3.Grapes\n\t4.Pear\nChoose which blank to fill")
    
    pos1=input("Please enter the blank name : ")
    pos2=int(input("Please enter any number : "))
    global Apple
    global Mango
    global Pear
    global Grapes
    
    if pos1=="Apple":
        chk=check_add(0,pos2,0,1)
        
        if chk==True:
            Apple=pos2
            vertices[0][0][0]=pos2

        
        
    elif pos1=="Mango":
        chk=check_add(0,pos2,0)
        if chk:        
            Mango=pos2
            vertices[0][0][3]=pos2
        
        
                
    elif pos1=="Grapes":
        chk=check_add(1,pos2,1)
        if (chk):
            Grapes=pos2
            vertices[1][0][0]=pos2
        
            
    elif pos1=="Pear":
        chk=check_add(3,pos2,0,2)
        if (chk):
            Pear=pos2
            vertices[3][0][3]=pos2
     
    side_tri.clear()           
    side_triangles("right")
    side_triangles("left")
    side_triangles("bottom")
    
#delete value from Trikodu 
def delete():
    global Apple
    global Mango
    global Pear
    global Grapes
    print("\n\t1.Apple\n\t2.Mango\n\t3.Grapes\n\t4.Pear\nChoose which blank to fill")
    pos1=input("Please enter the blank name to delete it's value : ")
    #if pos1=="apple"
    if pos1=="Apple":
        Apple="_"
        vertices[0][0][0]=0

    elif pos1=="Mango":      
            Mango="_"
            vertices[0][0][3]=0      
                
    elif pos1=="Grapes":
    
            Grapes="_"
            vertices[1][0][0]=0
        
            
    elif pos1=="Pear":

            Pear="_"
            vertices[3][0][3]=0
    
    side_tri.clear()           
    side_triangles("right")
    side_triangles("left")
    side_triangles("bottom")    
    print("Number deleted Successfully")


#values of the three Faces/sides of the Tridoku
side_triangles("right")
side_triangles("left")
side_triangles("bottom")

#main block to call other functions   
while True:
    
    print("The Tridoku")
    print("Let's fill the values named as fruit with right vlues to complete Tridoku\n\n")
    printit()
    print("Please select an option\n\t1.Add a Number\n\t2.Delete a Number")
    val=input("Please enter a choice : ")
    if val=="Add":
        add()
    elif val=="Delete":
        delete()
    else:
        print("Please enter appropriate option\n")
   

    if Apple!='_' and Grapes!='_' and Pear!='_' and Mango!='_':
            printit()
            print("\nThe Tridoku is Successfull solved ")
            break
    
        
    exit_val=input("Do you want to continue(y/n) : ")
    if exit_val!="y" and exit_val!="Y":
       
        break

