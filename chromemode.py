from selenium import webdriver as wb
from pywinauto.keyboard import SendKeys as sk
import pyttsx3
import speech_recognition as sr


#temp = 'open new tab'
#temp =temp.split()

def chmode():

    engine = pyttsx3.init()
    re = sr.Recognizer()
    print('what can i  search')

    #driver.maximize_window()
    i=0
    driver = wb.Chrome()
    while True:

        print('what can i search')
        try:
            with sr.Microphone() as source:
                re.adjust_for_ambient_noise(source,duration=2)
                engine.say('what can i serach')
                engine.runAndWait()

                audio = re.listen(source)
                x = re.recognize_google(audio)
        except:
                print('cannot understand')


        print(x)
        if(x=='exit' or x=='close'):
            break
        else:

            if(i!=0):
                sk('^t')
            windows = driver.window_handles
            driver.switch_to_window(windows[i])
            i+=1
            driver.get('http://www.google.com')
            driver.find_element_by_name('q').send_keys(x)
            sk('^{ENTER}')
