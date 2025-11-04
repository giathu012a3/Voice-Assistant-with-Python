
import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robotMouth = pyttsx3.init()
robot_brain=""

while True:
	with speech_recognition.Microphone() as mic:
		print("Robot: I,m Listening")
		audio = robot_ear.listen(mic)

	print("Robot: ...")

	try:
		you = robot_ear.recognize_google(audio)
	except:
		you=""

	print("You: "+ you)
	if you =="":
		robot_brain =" i can't hear you, try again"
	elif "hello" in you:
		robot_brain="Hello Phoenix Zadkiel"
	elif "today" in you:
		today = date.today()
		robot_brain= today.strftime("%B %d, %Y")
	elif "time" in you:
		now = datetime.now()
		robot_brain= now.strftime("%H hours %M minutes %S seconds")
	elif "bye" in you:
		robot_brain="Bye Phoenix Zadkiel"
		print("Robot: "+robot_brain)
		robotMouth.say(robot_brain)
		robotMouth.runAndWait()
		break
	else:
		robot_brain="I don't understand you."

	print("Robot: "+robot_brain)
	robotMouth.say(robot_brain)
	robotMouth.runAndWait()