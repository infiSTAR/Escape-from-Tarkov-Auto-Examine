# Escape-from-Tarkov-Auto-Examine ![Stars](https://img.shields.io/github/stars/Avnsx/Escape-from-Tarkov-Auto-Examine?style=plastic&logo=appveyor) ![Downloads](https://img.shields.io/github/downloads/Avnsx/Escape-from-Tarkov-Auto-Examine/total?label=.exe%20downloads&style=plastic)
## Description
New Account? EFT just wiped? Not a problem anymore! This one click code continously auto examines all items on a pre-selected Trader. Giving you free EXP & taking away the pain of having to examine items in raid. Not really detectable, you're safe to use this without being scared of getting banned.*

## Dependencies
If you don't want to use the .exe version from the releases tab on the right; you'll have to install python and run below in cmd:

	pip install pyautogui
	pip install keyboard
	pip install pillow --upgrade
	pip install opencv-python

## How To
1. Install python & repo dependencies
2. If you don't use the .exe version download & unzip the github repo
3. Open Escape from Tarkov
4. Go to settings; you have to be on screen resolution 1920x1080 (16:9) (if it still doesn't work, it's recommended that you copy my settings from the screenshot below)
5. Go on any Traders showcase (works most efficiently on Fence with scroll length 11, other traders 2)
6. Click on EFT_Auto_Examine.py
7. Leave it running as long as you wish to (the longer it runs the more items you'll have examined)
8. Enjoy your day, while all items continously get auto examined for you

## Additional Knowledge
You can stop the bot any time by pressing and holding F2 for a couple seconds, or just closing its window. If the bot scrolls too much for you or if you're not trying to use this bot on Fence, go to line 30 (``scroll_length = 11``) in the code and edit the length to whatever works best for you & save it. Recommended Settings: Fence: 11 | Prapor, Skier, Peacekeeper, Mechanic, Ragman: 2

This bot uses picture recognition, so if it errors out saying it can't find a picture you're unlucky. Your easiest way to get past this is by lowering the confidence(``confidence=0.9``) level of whatever picture wasn't found. If that didn't help and you're a tryhard and really want to use this, even though it can't find the pictures; you can go to the ``img_samples`` folder and check out each of those pictures and take your own versions of them(them all, or just the picture the code says it couldn't find), simply by screenshotting your client and cropping the required pictures just as I did. Then overwriting the orginal files in that folder, with your newly cropped versions. The images have to be .pngs. I've used https://www.iloveimg.com/crop-image to crop my images, it's a great tool to cut them so small.

Intentionally refused to use the API, to lower ban risk to a minimum.

![Picture 1](https://i.imgur.com/ooRNtK6.png)
![Picture 2](https://i.imgur.com/Vssjixm.png)

Written with python 3.9.5 on Windows 10 Build 19043, Resolution 1920x1080 (16:9), 17.3" (43.9 cm) screen.

Dependant on how many people show me that they're liking the code by giving ⭐'s on this repo, I'll expand functionality & push more quality of life updates.🎉

*Does not mean I take any responsibility if you get banned. All I'm saying is that it's insanely unlikely that you'll get banned for the usage of this. Since it's literally just using pictures to interact with the client and each movement and wait it does is randomised; meaning it's already avoiding fingerprinting. On top of that they would never ever care enough to ban a external picture recognition based bot lmao
