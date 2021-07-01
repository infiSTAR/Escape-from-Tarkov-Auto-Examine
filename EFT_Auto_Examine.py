import keyboard
from random import uniform
from pyautogui import center, click, moveTo, press, locateOnScreen, click, press, scroll, move
from time import sleep as s

print('If you like the code remember to star the Repo! https://github.com/Avnsx/Escape-from-Tarkov-Auto-Examine')
s(1)
print('Starting... make sure you are tabbed in on EFT!\nYou can press and hold Key F2 at any time to end.')
s(4)

def examine_item():
	for image in ['img_samples/blackgrey.png','img_samples/questionmark.png']:
		try:
			imagecords=locateOnScreen(image, confidence=0.9)
		except:
			print('ERROR: '+image+' not found')
			s(10)
			exit()
		if imagecords != None:
			click(imagecords, button='middle')
			move(uniform(180,220), uniform(-180,-220), uniform(.23,.65)) # avoids overlapping
			s(uniform(1,2)) # avoids examine errors
			print('examined item')
			return True
		else:
			return False

runtime=0
while keyboard.is_pressed('f2') != True:
	if examine_item() == False:
		showcase=locateOnScreen('img_samples/showcase.png', confidence=0.7)
		if showcase != None:
			scroll_length=11 # recommended: Fence: 11 | Prapor, Skier, Peacekeeper, Mechanic, Ragman: 2
			for __ in range(scroll_length):
				barcoords=center(showcase)
				moveTo(barcoords[0]+uniform(180,220), barcoords[1]+uniform(30,40))
				for __ in range(10):scroll(-10)
				examine_item()
				runtime+=1
				print('scroll number: '+str(runtime))
			if runtime == scroll_length:
				press('f5')
				print('refreshed trader')
				for image in ['img_samples/1.png','img_samples/topall.png']:
					try:
						click(center(locateOnScreen(image, confidence=0.7)))
					except:
						print('ERROR: '+image+' not found')
						s(10)
						exit()
					s(1)
				runtime=0
		elif showcase == None:
			print('ERROR: showcase.png not found')
			s(10)
			exit()



