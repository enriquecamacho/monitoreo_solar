import matplotlib.pyplot as plt

archivo1 = open("residuos.dat","r")
archivo2 = open("error.dat","r")

residuos=[]
error=[]

residuos = archivo1.readlines()
error = archivo2.readlines()

'''
for i in archivo2:
    residuos.append()
for i in archivo2:
    error.append(archivo2[i])
'''
archivo1.close()
archivo2.close()

x=[]
y=0
errorf=[]
for i in error:
    x.append(y)
    errorf.append(error[y])
    y=y+1

plt.plot(x,errorf)
plt.savefig("graph.png")
