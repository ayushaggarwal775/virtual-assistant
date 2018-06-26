from pyautogui import press,keyUp,keyDown


def setting(x):
    x = x.split()
    y = ' '.join(x[:2])
    print(x)
    if(y=='increase volume'):
        keyDown('fn')
        for i in range(int(x[3])):
            press('volumeup')
        keyUp('fn')


    elif(y=='increase brightness'):
        keyDown('fn')
        for i in range(int(x[3])):
            press('volumeup')
        keyUp('fn')

    elif(y=='decrease volume'):
        keyDown('fn')
