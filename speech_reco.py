import wolframalpha as wf
import wikipedia as wiki
import pyttsx3
import speech_recognition as sr
import os
import winnavi as f1
from pywinauto.keyboard import SendKeys
from oxforddict import wordsearch
from chromemode import chmode
from calculator import calculate



r = sr.Recognizer()
client = wf.Client('APP_KEY')
en = pyttsx3.init()
en.setProperty(
    'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
en.setProperty('rate', 130)

flag = True
while(flag):
    try:
        while(1):
            """with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source,duration=3)      #listening input
                print('How can I help you!\n ')
                audio = r.listen(source)


            que = r.recognize_google(audio)
"""
            que = input('-> ')
            print(que)
            que = que.lower()
            que = que.split(' ')


            if(' '.join(que)=='go to sleep' or ' '.join(que)=='bye bye'):   #exit program
                flag = False
                en.say('bye,see you later!')
                en.runAndWait()
                break


            elif(que[0] == 'meaning' or que[0]=='mean'):                    #search meaning and open oxford api
                re = wordsearch(' '.join(que[1:]))
                en.say(' '.join(que[1:]) + 'is ' + re)
                en.runAndWait()


            elif(que[0]=='calculate'):      #calculation call
                ans = calculate(' '.join(que[1:]))


            elif(' '.join(que)=='shutdown' or ' '.join(que)=='shutdown computer'):
                print('in shutting menu')
                en.say('are you sure')
                r1 = sr.Recognizer()
                with sr.Microphone() as source:
                    r1.adjust_for_ambient_noise(source,duration=5)
                    print('How can I help you!\n ')
                    naudio = r1.listen(source)
                com = r1.recognize_google(naudio).lower()
                if(com=='yes'):
                    os.system('psshutdown')
                else:
                    en.say('as you wish')


            elif(' '.join(que)=='close' or ' '.join(que)=='close current'):
                SendKeys('%{F4}')
                continue


            elif(que[0]=='open'):
                en.say('opening'+' '.join(que[1:]))
                en.runAndWait()

                if(que[1:]=='chrome mode' or que[1]=='chrome' or que[1:]=='google chrome'):
                    print('inside chrome checck point')
                    chmode()
                else:
                    bo = True
                    bo = f1.navi(que)

                    if(bo==False):
                        print('inside cant open')
                        en.say('cannot open' + ' '.join(que[1:]))
                        en.runAndWait()
                    del(bo)


            else:

                if(' '.join(que[:2]) == 'who was' or ' '.join(que[:2]) == 'who is' or ' '.join(que[:3]) == 'tell me about' ):
                    #if(que[0]=='who'):
                    #    ans = wiki.summary(' '.join(que[1:]), sentences=2)


                    ans = wiki.summary(' '.join(que[2:]), sentences=2)

                else:
                    que = ' '.join(que)
                    try:
                        print('in wolf')
                        re = client.query(que)
                        ans = re.results

                        ans = next(re.results).text

                    except:
                        print('in second wiki')
                        ans = wiki.summary(que, sentences=2)


            print(ans)
            en.say(ans)
            en.runAndWait()


    except:
        pass
