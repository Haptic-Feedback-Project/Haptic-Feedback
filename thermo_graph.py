import matplotlib.pyplot as plt

ax = []
ay = []
az = []
gx = []
gy = []
gz = []
temperature = []
time = []
sensitivity = 2
MAX_INT = 32767

# temperature formula


file = open('thermo_data.txt', 'r')

while(1):
	line = file.readline()
	if not line:
		break

	data = float(line) * (sensitivity / MAX_INT)
	ax.append(data)

	line = file.readline()
	data = float(line) * (sensitivity / MAX_INT)
	ay.append(data)

	line = file.readline()
	data = float(line) * (sensitivity / MAX_INT)
	az.append(data)

	sensitivity = 250

	line = file.readline()
	data = float(line) * (sensitivity / MAX_INT)
	gx.append(data)

	line = file.readline()
	data = float(line) * (sensitivity / MAX_INT)
	gy.append(data)

	line = file.readline()
	data = float(line) * (sensitivity / MAX_INT)
	gz.append(data)

	#Not sure whether we need it for temperature
	line = file.readline()
	data = ((float(line) + 521.0) / 340.0) + 35.0
	temperature.append(data)

	line = file.readline()
	time.append(float(line))



file.close()

#time = range(time) 

g1 = plt.figure(1)

plt.plot(temperature, gx, label='acceleration vector for gx')

plt.xlabel('Rotations')
plt.ylabel('Degrees')
plt.title('Rotations over Degrees')
plt.legend()

g1 = plt.figure(2)

plt.plot(temperature, gy, label='acceleration vector for gy')

plt.xlabel('Rotations')
plt.ylabel('Degrees')
plt.title('Rotations over Degrees')
plt.legend()

g1 = plt.figure(3)

plt.plot(temperature, gz, label='acceleration vector for gz')

plt.xlabel('Rotations')
plt.ylabel('Degrees')
plt.title('Rotations over Degrees')
plt.legend()


plt.show()
