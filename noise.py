import PySimpleGUI as sg
import pygame
import time



# Define the layout of your GUI
layout = [
    
    [[[[sg.Button('Fast run', image_source='img/runbutton.png'), sg.Button('Applause', image_source='img/clap.png'), sg.Button('Emotional Damage!', image_source='img/dmg.png'), sg.Button('Laugh!', image_source='img/laugh.png')]]]],
    [[[[sg.Button('Donkey', image_source='img/donkey.png'), sg.Button('Fart', image_source='img/fart.png'), sg.Button('Skibidi!', image_source='img/skibidi.png'), sg.Button('Very Nice!', image_source='img/nice.png')]]]],
    [[[[sg.Button('Fart2', image_source='img/fart.png'), sg.Button('Illuminati', image_source='img/illuminati.png'), sg.Button('Robot', image_source='img/robot.png'), sg.Button('Pancake', image_source='img/pancake.png')]]]],
    [[[[sg.Button('Monkey laff', image_source='img/monkeylaf.png'), sg.Button('Terminator', image_source='img/terminator.png'), sg.Button('Punchline', image_source='img/drum.png'), sg.Button('Sus', image_source='img/sus.png')]]]],
    [[[[sg.Button('Giorgio', image_source='img/g.png'), sg.Button('No!', image_source='img/no.png'), sg.Button('Chicken', image_source='img/chiken.png'), sg.Button('Love', image_source='img/love.png')]]]],    
    [sg.Button('Exit')]
]

# Create the window
window = sg.Window('Sound Machine', layout, finalize=True)

# Event loop
while True:
    event, values = window.read()

    # Handle window close or 'Exit' button click
    if event in (sg.WIN_CLOSED, 'Exit'):
        file = 'sound/door.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        time.sleep(1.4)
        break
    elif event == 'Laugh!':

        # to play sound
        file = 'sound/laugh.mp3'
        
        for i in range(4):
            pygame.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
    elif event == 'Emotional Damage!':

        # to play sound
        file = 'sound/dmg.mp3'
        
        for i in range(4):
            pygame.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
    elif event == 'Skibidi!':

        # to play sound
        file = 'sound/skibidi.mp3'
        
        for i in range(4):
            pygame.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
    elif event == 'Very Nice!':

        # to play sound
        file = 'sound/nice.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Pancake':

        # to play sound
        file = 'sound/pancake.mp3'
        
        for i in range(4):
            pygame.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
    elif event == 'Robot':

        # to play sound
        file = 'sound/robot.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Sus':

        # to play sound
        file = 'sound/sus.mp3'
        
        for i in range(4):
            pygame.init()
            pygame.mixer.music.load(file)
            pygame.mixer.music.play()
    elif event == 'Punchline':

        # to play sound
        file = 'sound/drum.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Love':

        # to play sound
        file = 'sound/love.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Giorgio':

        # to play sound
        file = 'sound/g.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Chicken':

        # to play sound
        file = 'sound/chicken.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'No!':

        # to play sound
        file = 'sound/no.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Terminator':

        # to play sound
        file = 'sound/terminator.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Monkey laff':

        # to play sound
        file = 'sound/monke_laugh.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Illuminati':

        # to play sound
        file = 'sound/illuminati.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Fart2':

        # to play sound
        file = 'sound/fart2.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Fart':

        # to play sound
        file = 'sound/fart.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Applause':

        # to play sound
        file = 'sound/Applause_Sound_Effect.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    elif event == 'Donkey':

        # to play sound
        file = 'sound/donkey.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()

    # Handle 'Click Me' button click
    elif event == 'Fast run':

        # to play sound
        file = 'sound/fast_run_sound_effect.mp3'
        pygame.init()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
        
# Close the window
window.close()
