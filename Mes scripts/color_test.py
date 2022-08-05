#Colorama test :
#import colorama
#from colorama import Fore
#from colorama import Style

#colorama.init()
#print(Fore.BLUE + Style.BRIGHT + "This is the color of the sky" + Style.RESET_ALL)
#print(Fore.GREEN + "This is the color of grass" + Style.RESET_ALL)
#print(Fore.BLUE + Style.DIM + "This is a dimmer version of the sky" + Style.RESET_ALL)
#print(Fore.YELLOW + "This is the color of the sun" + Style.RESET_ALL)

class bcolors:
    VERT = '\033[92m' #GREEN
    JAUNE = '\033[93m' #YELLOW
    ROUGE = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

#print(f"{bcolors.VERT}Vert!{bcolors.RESET}")
print("\u001b[31mTest")