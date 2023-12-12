# A class of 15 students with 5 subjects and 5 diffrent max marrks 

max_marks = [100,75,100,35,50]

marks_stu = {"stu1" :[55,35,65,20,33],
"stu2" :[95,35,70,25,36],
"stu3" :[50,60,65,22,45],
"stu4" :[58,65,87,16,54],
"stu5" :[35,44,76,24,49],
"stu6" :[22,54,54,10,35],
"stu7" :[56,56,86,6,45],
"stu8" :[75,74,88,5,5],
"stu9" :[99,32,24,4,24],
"stu10" :[13,45,86,33,34], 
"stu11" :[56,54,65,23,43], 
"stu12" :[35,67,56,32,40], 
"stu13" :[45,13,36,30,44],
"stu14" :[29,45,22,23,33],  
"stu15" :[59,24,65,34,23]}


final_dict = {}
for x,y in zip(marks_stu.keys(),marks_stu.values()):
    per_stu = []
    print("Name : "+ x)
    for z,a in zip(y,max_marks):
        per = round((z/a)*100,2)
        per_stu.append(per)  
    grade =  []
    for p in per_stu:
        if p <100 and p >80:
            txt ="Grade : A and" ,"Percentage : " +str(p)
            grade.append(txt)
        elif p <=80 and p>60:
            txt ="Grade : B and" ,"Percentage : " +str(p)  
            grade.append(txt)
        elif p <=60 and p>50:
            txt ="Grade : C and" ,"Percentage : " +str(p) 
            grade.append(txt)
        elif p <=50:
            txt = "Grade : D and" ,"Percentage : " +str(p)
            grade.append(txt)
    final_dict[x]=grade
        
        
        
        
        
        
        
        
        
        
        
