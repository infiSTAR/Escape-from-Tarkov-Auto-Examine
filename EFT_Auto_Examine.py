import os,random,string
randtitle=str(''.join(random.choice('_'+string.hexdigits) for i in range(random.randint(12,28))))
os.system('title '+randtitle)

import keyboard,sys,threading
from loguru import logger as log
from functools import partialmethod
from pyautogui import center, click, moveTo, press, locateOnScreen, click, press, scroll, move
from tinyWinToast.tinyWinToast import Toast, Button
from time import sleep as s

def output(level,type,color,mytext):
    log.level(type, no=level, color=color)
    log.__class__.type = partialmethod(log.__class__.log, type)
    log.remove()
    log.add(sys.stdout, format="<level>{level}</level> | <white>{time:HH:mm}</white> <level>|</level><light-white>| {message}</light-white>", level=type)
    log.type(mytext)

output(1, 'Info','<light-yellow>','Developed by Avnsx on GitHub: https://github.com/Avnsx/Escape-from-Tarkov-Auto-Examine\n')
output(None, 'Info','<light-yellow>','Starting... make sure a EFT Traders showcase is visible on your screen!')
output(None, 'Info','<light-yellow>','You can press and hold Key F2 at any time to end.\n')
s(random.uniform(3,5))

def error_exit(reason):
	output(2, 'Error','<light-red>', reason)
	s(15)
	os._exit(0)

def threaded():
	threading.Timer(1, threaded).start()
	if keyboard.is_pressed('f2') == True:
		toast = Toast()
		toast.setAppID(randtitle)
		toast.addButton(Button(content='Visit on GitHub', activationType='protocol', arguments='https://github.com/Avnsx/Escape-from-Tarkov-Auto-Examine', pendingUpdate=False))
		toast.setIcon(src=os.path.dirname(os.path.abspath(__file__))+'\\img_samples\\icon.ico', crop='round') #filepath fix
		toast.setDuration('short')
		toast.setTitle('Please leave Feedback!')
		toast.setMessage('Liked it? Have suggestions for improvements? Or maybe would like to support by giving a Star?')
		toast.show()
		os._exit(0)
	else:return False

loopn=0
runtime=0
try:
	def examine_item():
		for image in ['img_samples/blackgrey.png','img_samples/questionmark.png']:
			imagecords=locateOnScreen(image, confidence=0.9) # edit here; if issues with image detection 1
			if imagecords != None:
				click(imagecords, button='middle')
				move(random.uniform(180,220), random.uniform(-180,-220), random.uniform(.23,.65)) # avoids overlapping
				s(random.uniform(1,2)) # avoids examine errors & timeouts
				output(None, 'Info','<light-green>','examined item')
				return True
			else:return False

	while True:
		if loopn == 0:
			threaded()
			loopn+=1
		if examine_item() == False:
			showcase=locateOnScreen('img_samples/showcase.png', confidence=0.7) # edit here; if issues with image detection 2
			if showcase != None:
				scroll_length=random.randint(10,11) # edit here; if too much or too less scrolling
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
							click(center(locateOnScreen(image, confidence=0.7))) # edit here; if issues with image detection 3
							s(random.uniform(2,3)) # tabs load up time
						except Exception as e:
							print(e)
							error_exit('ERROR: '+image+' not found. Read the additional knowledge paragraph on the GitHub repo.\n')
					runtime=0
			elif showcase == None:error_exit('ERROR: showcase.png not found. Read the additional knowledge paragraph on the GitHub repo.\n')
except Exception as e: #not proud on exception handling
	if 'Pillow' in str(e):
		os.system('pip install pillow --upgrade')
		error_exit('Dependency ERROR: Pillow was missing; attempted installing Pillow. Please re-launch!')
	if 'OpenCV' in str(e):
		os.system('pip install opencv-python')
		error_exit('Dependency ERROR: OpenCV was missing; attempted installing OpenCV. Please re-launch!')
	else:
		print(e)
		error_exit('Unexpected ERROR: If you do not know what this was caused by open an Issue ticket in the GitHub repository.')
