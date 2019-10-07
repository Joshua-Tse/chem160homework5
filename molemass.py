names=["H", "C", "N", "O", "P", "S"]
masses=[1.00794,12.0107,14.00674,15.9994,30.973761,32.066]
Dict2={}
for i in range(len(names)):
    Dict2[names[i]]=masses[i]
def molemass(x):
    string=0
    string = x
    mm=0
    for i in string:
        mm+=Dict2[i]
    print (mm)