import time, subprocess, threading, random
from colorama import *


class menu:
    def progressbar_run(timos, bars, type="█"):
        bars_list = []
        count = bars
        while count > 0 :
            bars_list.append(type)
            count = count - 1
        # bars_count = bars_list.count("#")
        sleep = timos / bars
        print('''
                            [ ''', end="")
        for bar in bars_list:
            print(bar + Fore.RESET, end="")
            time.sleep(sleep)
        print(" ]")

    def botos(color):
        subprocess.call("cls", shell=True)
        init()
        print(color + '''           

                                /$$$$$$$            /$$                      
                                | $$__  $$          | $$                      
                                | $$  \ $$ /$$$$$$ /$$$$$$   /$$$$$$  /$$$$$$$
                                | $$$$$$$ /$$__  $|_  $$_/  /$$__  $$/$$_____/
                                | $$__  $| $$  \ $$ | $$   | $$  \ $|  $$$$$$ 
                                | $$  \ $| $$  | $$ | $$ /$| $$  | $$\____  $$
                                | $$$$$$$|  $$$$$$/ |  $$$$|  $$$$$$//$$$$$$$/
                                |_______/ \______/   \___/  \______/|_______/ 
                                                                                                                    
        ''' + Fore.RESET)

    def test():
        while 1:
            cq = input()
            if cq == "blue":
                menu.botos(Fore.BLUE)
                menu.menu()
            elif cq == "red":
                menu.botos(Fore.RED)
                menu.menu()
            elif cq =="magenta":
                menu.botos(Fore.MAGENTA)
                menu.menu()
            elif cq == "green":
                menu.botos(Fore.GREEN)
                menu.menu()
            elif cq == "yellow":
                menu.botos(Fore.YELLOW)
                menu.menu()
            elif cq == "cyan":
                menu.botos(Fore.CYAN)
                menu.menu()
            else:
                menu.home()
                print("Commande non reconnue.")

    def menu():
        print("")
        print('''
                        =============================================================
        
        ''')
        print(f'''
                        - Couleurs disponibles : red, green, yellow, blue, magenta, cyan
                        - Pour quitter : CTRL + C

                        
        
        
        ''')

    def home():
        # subprocess.call("cls", shell=True)
        test_thread = threading.Thread(target=menu.test)
        test_thread.start()
        init()
        colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
        menu.botos(random.choice(colors))
        menu.menu()

    def startup():
        menu.botos(Fore.RED)
        time.sleep(0.4)
        menu.botos(Fore.GREEN)
        time.sleep(0.4)
        menu.botos(Fore.YELLOW)
        time.sleep(0.7)
        for i in range(1):
            menu.botos(Fore.RED)
            time.sleep(0.04)
            menu.botos(Fore.GREEN)
            time.sleep(0.04)
            menu.botos(Fore.YELLOW)
            time.sleep(0.04)
            menu.botos(Fore.BLUE)
            time.sleep(0.04)
            menu.botos(Fore.MAGENTA)
            time.sleep(0.04)
            menu.botos(Fore.CYAN)
            time.sleep(0.04)
        menu.progressbar_run(1.5, 48)
        menu.home()