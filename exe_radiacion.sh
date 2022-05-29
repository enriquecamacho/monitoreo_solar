sudo systemctl enable serial-getty@ttyAMA0.service
sudo hwclock -s
COORD=$(sudo python gpdemo.py)
ALTI=$(python3 altitud1.py)
echo $COORD
echo "0.0" > MotorA.dat
echo "0.0" > residuoA.dat
DATE=$(sudo hwclock -r)
echo ${DATE:0:26}
python3 sun_hori.py -t "now" $COORD $ALTI >> MotorA.dat
python3 giro_angulos.py &
wait
DATE=$(sudo hwclock -r)
echo ${DATE:0:26}
python3 sun_hori.py -t "now" $COORD $ALTI >> MotorA.dat
python3 giro_angulos.py &
wait
sleep 120s

while true
do
DATE=$(sudo hwclock -r)
echo ${DATE:0:26}
python3 sun_hori.py -t "now" $COORD $ALTI >> MotorA.dat
python3 giro_angulos.py &
wait
more MotorA.dat
sleep 120s
done
