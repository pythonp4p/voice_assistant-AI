import os, webbrowser, sys, requests, subprocess, pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 180)


def speaker(text):
    engine.say(text)
    engine.runAndWait()


def browser():
    webbrowser.open('https://google.com', new=2)


def game():
    subprocess.Popen('E:/game/Сапёр v34.exe')


def offpc():
    os.system('shutdown /s')


def weather():
    '''Для работы этого кода нужно зарегистрироваться на сайте
	https://openweathermap.org'''
    try:
        params = {
            'q': 'Kyiv',
            'units': 'metric',
            'lang': 'ru',
            'appid': 'Ваш API ключ'
        }
        response = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather', params=params)
        if not response:
            raise
        w = response.json()
        speaker(
            f"На улице {w['weather'][0]['description']} {round(w['main']['temp'])} градусов"
        )

    except:
        speaker(
            'Произошла ошибка при попытке запроса к ресурсу API, проверь код')


def offBot():
    sys.exit()


def passive():
    pass
