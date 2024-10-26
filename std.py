Marks={"Raju":{"Eng":0,"Phy":90,"Math":46},
       "pinky":{"Phy":45,"Eng":65,"Math":0},
       "Sita":{"Math":46,"Eng":50,"Phy":45},
       "Mahesh":{"Eng":0,"Phy":19,"Math":99}}

std_names=list(Marks.keys())
print(std_names)
std_scr=[]


for names,marks in Marks.items():
    for sub,scr in marks.items():
        if sub=="Eng":
            std_scr.append(scr)
print(std_scr)

idx=max(std_scr)
index=std_scr.index(idx)
print(std_names[index])
