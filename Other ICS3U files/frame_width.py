#fRAME 

#Initializing Variables
portrait_width=int(input("Enter portrait width: "))
portrait_length=int(input("Enter portrait length: "))
matte_width=int(input("Enter matte width: "))
frame_width=int(input("Enter frame width: "))


#Set Defaults
if(portrait_width<1):
    portrait_width=1
if(portrait_length<1):
    portrait_length=1
if(matte_width<1):
    matte_width=1
if(frame_width<1):
    frame_width=1
total_length = 2*frame_width+2*matte_width+portrait_length
total_width = 2*frame_width+2*matte_width+portrait_width
print("")


#Printing the Layout
for i in range(1,total_length+1): #The counter variable i controls the whole procedure, each line is printed based on the value of i
    
    if(i<=frame_width): #This block controls the frame above the matte
        for k in range(0,total_width):
            print("#",end=" ")
        print("")
        
    if(frame_width<i<=(matte_width+frame_width)): #This block controls the matte above the portrait 
        for k in range(0,frame_width):
            print("#",end=" ")
        for k in range(0,(total_width-2*(frame_width))):
            print("+",end=" ")
        for k in range(0,frame_width):
            print("#",end=" ")
        print("")
        
    if((matte_width+frame_width)<i<=(matte_width+frame_width+portrait_length)): #This block controls the actual portrait
        for k in range(0,frame_width):
            print("#",end=" ")
        for k in range(0,matte_width):
            print("+",end=" ")
        for k in range(0,portrait_width):
            print("X",end=" ")
        for k in range(0,matte_width):
            print("+",end=" ")
        for k in range(0,frame_width):
            print("#",end=" ")
        print("")
        
    if((matte_width+frame_width+portrait_length)<i<=(2*matte_width+frame_width+portrait_length)): #This block controls the matte below the portrait
        for k in range(0,frame_width):
            print("#",end=" ")
        for k in range(0,(total_width-2*(frame_width))):
            print("+",end=" ")
        for k in range(0,frame_width):
            print("#",end=" ")
        print("")
        
    if((2*matte_width+frame_width+portrait_length)<i<=2*matte_width+2*frame_width+portrait_length): #This block controls the frame below the matte
        for k in range(0,total_width):
            print("#",end=" ")
        print("")

