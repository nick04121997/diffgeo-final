import csv
import sys
import operator
import matplotlib.pyplot as plt
import numpy

filename_in = "public_dataset/100669/100669_session_1/Sorted_ID.csv"
file_in = open(filename_in, "r")
csvreader = csv.reader(file_in)

times = []
accel_x = []
accel_y = []
accel_z = []

for row in csvreader:
	times.append(int(row[0]))
	accel_x.append(float(row[3]))
	accel_y.append(float(row[4]))
	accel_z.append(float(row[5]))

times_diff = numpy.diff(times)
accel_x_diff = numpy.diff(accel_x)
accel_y_diff = numpy.diff(accel_y)
accel_z_diff = numpy.diff(accel_z)

accel_x_deriv = accel_x_diff/times_diff
accel_y_deriv = accel_y_diff/times_diff
accel_z_deriv = accel_z_diff/times_diff

times2 = times[0:len(times)-1]

plt.figure(1)
plt.subplot(2, 1, 1)
plt.plot(times, accel_x)
plt.ylabel('acceleration x')
plt.subplot(2, 1, 2)
plt.plot(times2, accel_x_deriv)
plt.xlabel('time')
plt.ylabel('jerk x')

plt.figure(2)
plt.subplot(2, 1, 1)
plt.plot(times, accel_y)
plt.ylabel('acceleration y')
plt.subplot(2, 1, 2)
plt.plot(times2, accel_y_deriv)
plt.xlabel('time')
plt.ylabel('jerk y')

plt.figure(3)
plt.subplot(2, 1, 1)
plt.plot(times, accel_z)
plt.ylabel('acceleration z')
plt.subplot(2, 1, 2)
plt.plot(times2, accel_z_deriv)
plt.xlabel('time')
plt.ylabel('jerk z')

print("Size times: " + str(len(times)))
print("Size x: " + str(len(accel_x)))
print("Size y: " + str(len(accel_y)))
print("Size z: " + str(len(accel_z)))

plt.show()