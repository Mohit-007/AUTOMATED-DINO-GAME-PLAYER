import pyautogui # automatic key action
from PIL import Image, ImageGrab # access the screen
import time # time
import speech_recognition as sr


# hit the key 
def hit(key):
    pyautogui.keyDown(key)
    return

'''
def takecommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source: 
#        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1)
        r.energy_threshold = 10
        audio = r.record(source, duration = 3) 
    try: # if it enable to listen properly then ! error
        # print("Recognizing...")
        query = r.recognize_google(audio, language="en-in") # google english india
        # print(f"you said: {query} \n ") # it will confirm the query
        if query.lower() == "down":
            hit("up")
    except Exception as e: # if it unable to listen properly then error
        print(e) # it print the error

        print("Say that again please...") # it will ask to repeat the audio
        return"None"
'''

# if the imaginery positional rectangle collide with pixel value < 100
def isCollide(data):
    for i in  range(725, 800):
        for j in range(775, 825):
            if data[i, j] < 100:
                hit("up")
                return
    '''
    for i in range(450, 875):
        for j in range(650, 700):
            if data[i, j] < 100:
                hit("down")
                return
    '''

'''
def isCollide_voice_command():
    takecommand()
    return
'''


if __name__ == "__main__":
    print('DINO GAME START IN 5 SECONDS') 
    time.sleep(1) # sleep time to switch the window

    while True: # infinite loop
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)
        #isCollide_voice_command()
        
        # for i in range(250, 300):
        #    for j in range(360, 380):
        #        data[i, j] = 171
        # image.show()
        # break
        


'''
if __name__ == "__main__":
    time.sleep(5) # sleep time to switch the window
    image =ImageGrab.grab().convert('L')
#    image = ImageGrab.grab().convert('L')
    data = image.load()
    for i in range(450, 575):
        for j in range(775, 825):
            data[i, j] = 0
    image.show()
'''    


# 

# img = Image.open("img.jpg")
# background = Image.open("background.jpg")
# background.paste(img, (0, 0), img)
# background.show()
# background.save(image.jpg)
