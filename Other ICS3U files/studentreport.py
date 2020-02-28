#Student information

studentfile = open("midterm_final_marks.txt","r")
studentreport = open("student_report.txt","w")

donereadingfile = False#while loop boolean counter

while(not donereadingfile):
    line  = studentfile.readline()
    #initializing variables
    inc=0
    dec=0
    avg_mid=0
    avg_fin=0

    if(line=="ENDENDEND"):
        donereadingfile = True

    else:
        student_no = line
        student_no = student_no.rstrip("\n")

        line  = studentfile.readline()
        sub_no = int(line)#Read from file as str
        studentreport.write("Student Number: "+student_no)
        
        for i in range(0,sub_no):#To read as many lines as there are subjects

            line = studentfile.readline()
            
            mid,fin = line.split("$")
            mid = int(mid.rstrip("\n"))
            fin = int(fin.rstrip("\n"))
            
            if(mid<fin):#To see how many marks increased
                inc = inc+1
            elif(mid>fin):
                dec = dec+1
                
            avg_mid +=mid
            avg_fin +=fin
            
        studentreport.write("\nAverage Midterm: "+str(round(avg_mid/sub_no,1)))
        studentreport.write("\nAverage Final: "+str(round(avg_fin/sub_no,1)))
        
        avg_mid=0#Resets variables
        avg_fin=0
        
        if(inc>dec):
            studentreport.write("\nAWARD\n")
        else:
            studentreport.write("\nNO AWARD\n")
            
        studentreport.write("\n")#Aesthetics, leaves line after each student

        inc=0#Resets variables
        dec=0

#To close the files
studentfile.close()
studentreport.close()

print("program executed successfully")
