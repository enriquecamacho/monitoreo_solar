import time
archivo=open("MotorA.dat",'r')
angulos=archivo.readlines()
archivo.close()
cambio=float(angulos[1])-float(angulos[0])
signo=1
if cambio<0:
	cambio=cambio*(-1)
	signo=-1
n=int(cambio/0.1125)
error = (float(n)-(cambio/0.1125))
Nangulo=float(angulos[0])+((signo)*(int(n)*0.1125))
#Nangulo=float(angulos[0])+(signo)*cambio
archivo=open("MotorA.dat",'w')
archivo3=open("Posicion.dat",'a')
archivo.write(str(Nangulo)+'\n')
archivo3.write(str(Nangulo)+'\n')
archivo4=open("error.dat",'a')
archivo4.write(str(error))
archivo.close()
archivo4.close()
archivo3.close()
print(angulos)
