# This file is meant to parse the accelerometer data from a session
# where the event id is the same.

import csv
import sys
import operator

filename_in = "public_dataset/100669/100669_session_1/Accelerometer.csv"
filename_out = "public_dataset/100669/100669_session_1/Sorted_ID.csv"
event_id = "100669011000001"
file_in = open(filename_in, "r")
file_out = open(filename_out, "w")
csvreader = csv.reader(file_in)
csvwriter = csv.writer(file_out)

for row in csvreader:
	if row[2] == event_id:
		csvwriter.writerow(row)