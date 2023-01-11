import speech_recognition as sr
import pyttsx3
import random
import os

rec = sr.Recognizer()
maquina = pyttsx3.init()

def executa_comando():

    try:
        with sr.Microphone(1) as mic:
            rec.adjust_for_ambient_noise(mic)
            print('ouvindo...')
            voz = rec.listen(mic)
            comando = rec.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'karen' in comando:
                comando = comando.replace('karen', '')
                maquina.runAndWait()
    except:
        print('por favor, cheque seu microfone')
    return comando

def random_number():
 num_aleatorio = random.randint(0,1000)

def comando_voz_usuario():

    comando = executa_comando()
    if 'bom dia' in comando:
        maquina.say('bom dia, senhor')
        maquina.runAndWait()
        executa_comando() 
    if 'boa tarde' in comando:
        maquina.say('boa tarde, senhor')

    if 'boa noite' in comando:
        maquina.say('boa noite, senhor')

    if 'qual o seu nome' in comando:
        maquina.say('meu nome é karen')

    if 'quem é seu criador' in comando:
        maquina.say('meu criador se chama alysson rrendryk')

    if 'data da sua criação' in comando:
        maquina.say('de acordo com meu criador, fui criada no dia 25 de outubro de 2022')

    if 'abra o navegador' in comando:
        os.system("start Chrome.exe")
        
    if 'abra o youtube' in comando:
        os.system("start www.youtube.com")
    if 'mix' in comando:
        os.system("start www.youtube.com/watch?v=YPhD7rvVnDo&list=RDGMEMFDHdtbQF5jLxlUZMleBN_w&start_radio=1&rv=5u5ZXEsaZ60")

comando_voz_usuario()