
with open("damaging.csv", "rt") as dam1, open("goodfaith.csv", "rt") as gf1, open("damaging1.csv", "rt") as dam2, open("goodfaith1.csv", "rt") as gf2, open("gf_missIds", "wt") as gf_out, open("dam_missIds", "wt") as dam_out:

	damLines1 = dam1.readlines()
	gfLines1 = gf1.readlines()	
	damLines2 = dam2.readlines()
	gfLines2 = gf2.readlines()
	
	for i in range(len(damLines1)):
		revId1 = damLines1[i].split(",")[0].strip()
		for i in range(len(damLines2)):
			revId2 = damLines2[i].split(",")[0].strip()
			if revId1 == revId2:
				damClass1 = damLines1[i].split(",")[1].strip()
				damClass2 = damLines2[i].split(",")[1].strip()
				if damClass1 != damClass2:
					dam_out.write(revId1 + "\n")
				break

	for i in range(len(gfLines1)):
		revId1 = gfLines1[i].split(",")[0].strip()
		for i in range(len(gfLines2)):
			revId2 = gfLines2[i].split(",")[0].strip()
			if revId1 == revId2:
				gfClass1 = gfLines1[i].split(",")[1].strip()
				gfClass2 = gfLines2[i].split(",")[1].strip()
				if gfClass1 != gfClass2:
					gf_out.write(revId1 + "\n")
				break
