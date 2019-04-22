
with open("damaging.csv", "rt") as dam, open("goodfaith.csv", "rt") as gf, open("missIds", "wt") as out:
	lines1 = dam.readlines()
	lines2 = gf.readlines()	
	
	for i in range(len(lines1)):
		class1 = lines1[i].split(",")[1]
		class2 = lines2[i].split(",")[1]
		print(class1 + " " + class2)
		if class1 != class2:
			out.write(lines1[i].split(",")[0] + "\n")
	


			
