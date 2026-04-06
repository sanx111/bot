import mss
import pyautogui
import cv2
import numpy
import time
import multiprocessing

import map_reader

class ScreenCap:
    def __init__(self) -> None:
        self.img = None
        self.cap_process = None
        self.fps = None
        self.enable_cv = True
        self.w, self.h = pyautogui.size()
        self.monitor = {"top": 0, "left": 0, "width": self.w, "height": self.h}

        self.zone = None

    def capture_screen(self):
        t0 = time.time()
        fps_delay = 5
        frames = 1
        with mss.mss() as sct:
            while True:
                self.img = numpy.array(sct.grab(self.monitor))

                self.zone = map_reader.get_zone(self.img)
                self.zone = self.zone.lower().strip()
                
                if self.enable_cv:
                    smallimg = cv2.resize(self.img, (0, 0), fx=0.5, fy=0.5)

                    if self.fps is None:
                        fps_text = ""
                    else:
                        fps_text = f'FPS: {self.fps:.2f}'
                    
                    cv2.putText(
                        smallimg,
                        fps_text,
                        (25,50),
                        cv2.FONT_HERSHEY_DUPLEX,
                        1,
                        (5, 255, 5),
                        1,
                        cv2.LINE_AA
                    )
                    cv2.putText(
                        smallimg,
                        f"Zone: {self.zone}",
                        (25,150),
                        cv2.FONT_HERSHEY_DUPLEX,
                        1,
                        (0, 255, 255),
                        1,
                        cv2.LINE_AA
                    )
                    

                    cv2.imshow("comp vision", smallimg)  
                    cv2.waitKey(1) #espera 1 milisegundo para fazer o display corretamente

                tempo_passado = time.time() - t0
                if tempo_passado>=fps_delay:
                    self.fps = (frames/tempo_passado)
                    print (self.zone)
                    frames = 0
                    t0 = time.time()
                frames +=1

class bcolors:
    rosa = '\033[95m'
    ciano = '\033[96m'
    azul = '\033[94m'
    verde = '\033[92m'
    vermelho = '\033[91m'
    amarelo = '\033[93m'
    padrao = '\033[0m'

def print_menu():
    print(f'{bcolors.amarelo}Menu')
    print(f'\t{bcolors.verde}r - run\t\t Start Screen cap')
    print(f'\t{bcolors.vermelho}s - stop\t Stop Screen cap.{bcolors.padrao}')
    print(f'\tq - quit\t Quit program')

if __name__ == "__main__":
    #instanciando
    Screen = ScreenCap()
    #menu loop
    while True:
        print_menu()
        user_input = input().strip().lower()

        if user_input == 'quit' or user_input == 'q':
            if Screen.cap_process is not None:
                Screen.cap_process.terminate()
            break

        elif user_input == 'run' or user_input =='r':

            if Screen.cap_process is not None:
                print(f'{bcolors.amarelo} AVISO {bcolors.padrao} Screen cap ja esta rodando')
                continue
            screen_instance = ScreenCap()
            Screen.cap_process = multiprocessing.Process(
                target=screen_instance.capture_screen,
                name="screen cap"             
            )
            Screen.cap_process.start()
            #screen.cap_screen nao tem () no final pois queremos rodar o metodo em loop e não apenas apresentar seu resultado

        elif user_input == 'stop' or user_input == 's':
            if Screen.cap_process is None:
                print(f'{bcolors.amarelo} AVISO {bcolors.padrao} Screen cap não esta rodando')
                continue
            else:
                Screen.cap_process.terminate()
                Screen.cap_process = None
        else:
            print(f'{bcolors.vermelho} ERRO {bcolors.padrao} comando invalido')
    #input

    # start/stop

