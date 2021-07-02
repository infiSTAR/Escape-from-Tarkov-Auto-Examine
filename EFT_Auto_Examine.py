import os,random,string
os.system('title '+str(''.join(random.choice('_'+string.hexdigits) for i in range(random.randint(12,28)))))

import keyboard,sys
from loguru import logger as log
from functools import partialmethod
from pyautogui import center, click, moveTo, press, locateOnScreen, click, press, scroll, move
from time import sleep as s

#setting first time severity level, requires a number and afterwards just use None if you want to use the same severity level again
def output(level,type,color,mytext):
    log.level(type, no=level, color=color)
    log.__class__.type = partialmethod(log.__class__.log, type)
    log.remove()
    log.add(sys.stdout, format="<level>{level}</level> | <white>{time:HH:mm}</white> <level>|</level><light-white>| {message}</light-white>", level=type)
    log.type(mytext)

output(1, 'Info','<light-yellow>','If you like the code remember to star the Repository!')
output(None, 'Info','<light-yellow>','Link: https://github.com/Avnsx/Escape-from-Tarkov-Auto-Examine\n')
output(None, 'Info','<light-yellow>','Starting... make sure you are tabbed in on EFT!')
output(None, 'Info','<light-yellow>','You can press and hold Key F2 at any time to end.\n')
s(random.uniform(5,8))

runtime=0
try:
	def examine_item():
		for image in ['img_samples/blackgrey.png','img_samples/questionmark.png']:
			imagecords=locateOnScreen(image, confidence=0.9)
			if imagecords != None:
				click(imagecords, button='middle')
				move(random.uniform(180,220), random.uniform(-180,-220), random.uniform(.23,.65)) # avoids overlapping
				s(random.uniform(1,2)) # avoids examine errors & timeouts
				output(None, 'Info','<light-green>','examined item')
				return True
			else:return False

	while keyboard.is_pressed('f2') != True:
		if examine_item() == False:
			showcase=locateOnScreen('img_samples/showcase.png', confidence=0.7)
			if showcase != None:
				scroll_length=random.randint(10,11)
				for __ in range(scroll_length):
					barcoords=center(showcase)
					moveTo(barcoords[0]+random.uniform(150,190), barcoords[1]+random.uniform(30,40))
					for __ in range(7):scroll(-10)
					examine_item()
					runtime+=1
					output(None, 'Info','<light-magenta>','scroll number: '+str(runtime))
				if runtime == scroll_length:
					press('f5')
					output(None, 'Info','<light-cyan>','refreshed trader\n')
					for image in ['img_samples/1.png','img_samples/topall.png']:
						try:
							click(center(locateOnScreen(image, confidence=0.7)))
						except Exception as e:
							print(e)
							output(2, 'Error','<light-red>','\nERROR: '+image+' not found. Read the additional knowledge paragraph on the github repo.\n')
							s(15)
							exit()
						s(1)
					runtime=0
			elif showcase == None:
				output(2, 'Error','<light-red>','ERROR: showcase.png not found. Read the additional knowledge paragraph on the github repo.\n')
				s(15)
				exit()
#I'm not proud on how I parse errors here; looks like a case of it is what it is
except Exception as e:
	if 'Pillow' in str(e):
		os.system('pip install pillow --upgrade')
		output(2, 'Error','<light-red>','Dependency ERROR: Pillow was missing; attempted installing Pillow. Please re-launch!')
		s(15)
		exit()
	if 'OpenCV' in str(e):
		os.system('pip install opencv-python')
		output(2, 'Error','<light-red>','Dependency ERROR: OpenCV was missing; attempted installing OpenCV. Please re-launch!')
		s(15)
		exit()

