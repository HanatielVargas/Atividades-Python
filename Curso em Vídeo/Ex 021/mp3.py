try:
    from pygame import mixer

    mixer.init()
    mixer.music.load('Ex 021/musica.mp3')
    mixer.music.play()
except:
    print('\033[1;31mOcorreu um erro!\033[m')
else:
    try:
        a = input('Digite enter para sair ')
    except:
        print('\033[1;31mOcorreu um erro!\033[m')
