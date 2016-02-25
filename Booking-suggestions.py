#!/usr/bin/env python
import webbrowser
import os
import csv
import time

print "Hello"
with open('test.csv', 'rb') as f:
	reader = csv.reader(f)
	i=0
	for row in reader:
		i=i+1
		mylist = (','.join(row))
		print mylist
		text = mylist
		text= text.replace(" ","%s")
		print "Next input is: "+text
		text= "adb shell input text "+text
#		print text
#		print len(text)
		count = len(text)/2
		while (count):
			os.system("adb shell input keyevent 67")
			count=count -1
		os.system(text)
		time.sleep(5)
		os.system("adb shell screencap -p /sdcard/screen{0}.png".format(i+1))
		os.system("adb pull /sdcard/screen{0}.png".format(i+1))




