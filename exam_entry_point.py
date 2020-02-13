import examination_system
for i in range(0,6):
	print("1.Admin Signin\n2.Student Signin\n3.Exit")
	ch=int(input("Enter your choice: "))
	
	if ch==1:
		yn=input("New admin?....(Y/N)")
		if yn == "Y":
			print("Admin Sign Up")
			user_name=input("Enter admin username: ")
			pass_word=input("Enter admin password: ")
			examination_system.adminsignin(user_name,pass_word)
		elif yn == "N":
			examination_system.adminsignin(user_name,pass_word)
			
	if ch==2:
		yn=input("New student?....(Y/N)")
		if yn == "Y":
			print("Student Sign Up")
			suser_name=input("Enter student username: ")
			spass_word=input("Enter student password: ")
			examination_system.studentsignin(suser_name,spass_word)
		elif yn == "N":
			examination_system.studentsignin(suser_name,spass_word)
			
	if ch==3:
		break
	

