

def adminsignin(user_name,pass_word):
	import time
	import os
	print("Admin Sign In")
	user_name1=input("Enter admin username: ")
	pass_word1=input("Enter admin password: ")
	adminlist=[user_name,pass_word]
	if user_name1 == adminlist[0] and pass_word1 == adminlist[1]:
		print("Username and Password matched")
		print("You are successfully signed in!!!")
	else:
		print("Incorrect username or password")
	import cx_Oracle
	conn = cx_Oracle.connect('hr/hr@xe')
	cursor = conn.cursor()
	cursor.execute('create table ques(qno number,question varchar2(20),aopt varchar2(10),\
	bopt varchar2(10),copt varchar(10),dopt varchar2(10),correct varchar2(10))')
	for i in range(0,4):
		qn=int(input("Enter question no:"))
		ques=input("Enter question:")
		a=input("Enter option A:")
		b=input("Enter option B:")
		c=input("Enter option C:")
		d=input("Enter option D:")
		corr=input("Enter correct answer:")
		cursor.execute('insert into ques(qno,question,aopt,bopt,copt,dopt,correct) \
		values(:qno,:question,:aopt,:bopt,:copt,:dopt,:correct)',\
		{'qno':qn,'question':ques,'aopt':a,'bopt':b,'copt':c,'dopt':d,'correct':corr})
		conn.commit()
	print("Display questions:")
	cursor.execute('select * from ques')
	for row in cursor:
		print(row)
	time.sleep(1)
	
	conn.close()
		
def studentsignin(suser_name,spass_word):
	import time
	import os
	print("Student Sign In")
	suser_name1=input("Enter student name:")
	spass_word1=input("Enter student password: ")
	studentlist = [suser_name,spass_word]
	if suser_name1 == studentlist[0] and spass_word1 == studentlist[1]:
		print("Username and Password matched")
		print("You are successfully signed in!!!")
	else:
		print("Incorrect username or password")
	import cx_Oracle
	conn = cx_Oracle.connect('hr/hr@xe')
	cursor = conn.cursor()
	print("Display questions:")
	cursor.execute('select * from ques')
	count=0
	time.sleep(1)
	for row in cursor:
		print("QuestionNo:  ",row[0])
		print("Qusetion:    ",row[1])
		print("Option A:    ",row[2])
		print("Option B:    ",row[3])
		print("Option C:    ",row[4])
		print("Option D:    ",row[5])
		ans=input("Enter your answer:")
		os.system("cls")
		if ans in row[6] :
			count=count+1
		time.sleep(1)
	print("Your total score is:"+str(count)+"/4")
	conn.commit()
	conn.close()
		
