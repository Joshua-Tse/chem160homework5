names=["H", "C", "N", "O", "P", "S"]
masses=[1.00794,12.0107,14.00674,15.9994,30.973761,32.066]
Dict2={}
for i in range(len(names)):
    Dict2[names[i]]=masses[i]
def molemass2(x):
    string = x
    mm=0
    previous=0
    for i in string:
        if i.isdigit() == True:
            mm-= previous
            previous=previous *int(i)
            mm+= previous
        if i.isdigit() == False:
            previous=Dict2[i]
            mm+=Dict2[i]
    print (mm)
