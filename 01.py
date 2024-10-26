from emp import sridevipg
m1=sridevipg("MANI",8897672572,"12-12-2022",7000,5000)
print()
print(f"PGNAME :{m1.pgname}\nADDRES :{m1.adds}\nCONTACT :{m1.contact}")
print()
print()
print(f"NAME :{m1.name}\nPHON NUMBER :{m1.phon}\nSTARTING DATE :{m1.startdate}\nRENT :{m1.rent}\nTAX :{m1.tax}\nTOTALRENT :{m1.totalpay()}")




m2=sridevipg("MAHESH",8897546472,"12-34-2022",5000,400)
print()
print(f"PGNAME :{m2.pgname}\nADDRES :{m2.adds}\nCONTACT :{m2.contact}")
print()
print()
print(f"NAME :{m2.name}\nPHON NUMBER :{m2.phon}\nSTARTING DATE :{m2.startdate}\nRENT :{m2.rent}\nTAX :{m2.tax}\nTOTALRENT :{m2.totalpay()}")




