from os import system
from pystyle import *
from colorama import Fore
import time
import os


def cmdconfig():
    system('title Brumail v1.0 VulnSec')
    cmd = 'mode 110,30'
    os.system(cmd)

def clear():
    system('cls')

def main():
    clear()
    print(f"""{Fore.YELLOW}____________ _   ____  ___  ___  _____ _     
{Fore.YELLOW}| ___ \ ___ \ | | |  \/  | / _ \|_   _| |    
{Fore.YELLOW}| |_/ / |_/ / | | | .  . |/ /_\ \ | | | |    
{Fore.YELLOW}| ___ \    /| | | | |\/| ||  _  | | | | |    
{Fore.YELLOW}| |_/ / |\ \| |_| | |  | || | | |_| |_| |____
{Fore.YELLOW}\____/\_| \_|\___/\_|  |_/\_| |_/\___/\_____/{Fore.WHITE}


{Fore.RED}[*]{Fore.WHITE} https://github.com/vu1nsec
{Fore.RED}[*]{Fore.WHITE} v1.0""")
    print(f"""          

{Fore.YELLOW}[1]{Fore.WHITE} Gmail
{Fore.YELLOW}[2]{Fore.WHITE} Yahoo
{Fore.YELLOW}[3]{Fore.WHITE} Outlook
{Fore.YELLOW}[4]{Fore.WHITE} Proton
{Fore.YELLOW}[5]{Fore.WHITE} iCloud
        
""")
    
#===================================================================================================================
#===================================================================================================================
    
    def gmail_gathering():
        clear()
        print(Colorate.Color(Colors.yellow, "Informations Needed : Username, Name, Lastname, Dob, Zipcode\n"))
        username = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Username : ").lower()
        if username == "":
            print("[!] Invalid Username.")
            return gmail_gathering()
        name     = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Name     : ").lower()
        lastname = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Lastname : ").lower()
        dob      = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Dob Year : ").lower()
        zipcode  = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Zipcode  : ").lower()

        brute_list = f"""
                     Brumail v1.0 - Made By VulnSec
                            
***************************************************************************
Target    : {username}
Option    : Gmail
***************************************************************************
Mail List :

{username}@gmail.com
{name}{lastname}@gmail.com
{lastname}{name}@gmail.com
{name}{lastname}{zipcode}@gmail.com
{lastname}{name}{zipcode}@gmail.com
{name}{dob}@gmail.com
{dob}{name}gmail.com
{dob}{lastname}@gmail.com
{lastname}{zipcode}@gmail.com
{username}{zipcode}@gmail.com
{username}{dob}@gmail.com
{username}{dob}{zipcode}@gmail.com
{username}{zipcode}{dob}@gmail.com
{name}{zipcode}@gmail.com

***************************************************************************
Epieos Check Links :

- Epieos: https://epieos.com/?q={username}@gmail.com&t=email
- Epieos: https://epieos.com/?q={name}{lastname}@gmail.com&t=email
- Epieos: https://epieos.com/?q={lastname}{name}@gmail.com&t=email
- Epieos: https://epieos.com/?q={name}{lastname}{zipcode}@gmail.com&t=email
- Epieos: https://epieos.com/?q={lastname}{name}{zipcode}@gmail.com&t=email
- Epieos: https://epieos.com/?q={name}{dob}@gmail.com&t=email
- Epieos: https://epieos.com/?q={dob}{name}@gmail.com&t=email
- Epieos: https://epieos.com/?q={dob}{lastname}@gmail.com&t=email
- Epieos: https://epieos.com/?q={lastname}{zipcode}@gmail.com&t=email
- Epieos: https://epieos.com/?q={username}{dob}@gmail.com&t=email
- Epieos: https://epieos.com/?q={username}{dob}@gmail.com&t=email
- Epieos: https://epieos.com/?q={username}{dob}{zipcode}@gmail.com&t=email
- Epieos: https://epieos.com/?q={username}{zipcode}{dob}@gmail.com&t=email
- Epieos: https://epieos.com/?q={name}{zipcode}@gmail.com&t=email

***************************************************************************
For any question contact vulnsec on Discord. Github https://github.com/vu1nsec
"""

        print(Colorate.Color(Colors.yellow, "\nCreating file..."))
        file_builder = open(f"{username}-Gmail-List.txt", "w+")
        file_builder.write(f"{brute_list}")
        file_builder.close()
        time.sleep(1)
        return main()

#===================================================================================================================#
#===================================================================================================================#

    def yahoo_gathering():
        clear()
        print(Colorate.Color(Colors.yellow, "Informations Needed : Username, Name, Lastname, Dob, Zipcode\n"))
        username = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Username : ").lower()
        name     = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Name     : ").lower()
        lastname = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Lastname : ").lower()
        dob      = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Dob Year : ").lower()
        zipcode  = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Zipcode  : ").lower()

        brute_list = f"""
                     Brumail v1.0 - Made By VulnSec
                            
***************************************************************************
Target    : {username}
Option    : Yahoo
***************************************************************************
Mail List :

{username}@yahoo.com
{name}{lastname}@yahoo.com
{lastname}{name}@yahoo.com
{name}{lastname}{zipcode}@yahoo.com
{lastname}{name}{zipcode}@yahoo.com       
{name}{dob}@yahoo.com
{dob}{name}@yahoo.com
{dob}{lastname}@yahoo.com
{lastname}{zipcode}@yahoo.com
{username}{zipcode}@yahoo.com
{username}{dob}@yahoo.com
{username}{dob}{zipcode}@yahoo.com
{username}{zipcode}{dob}@yahoo.com
{name}{zipcode}@yahoo.com

***************************************************************************
Epieos Check Links :

- Epieos: https://epieos.com/?q={username}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={name}{lastname}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={lastname}{name}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={name}{lastname}{zipcode}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={lastname}{name}{zipcode}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={name}{dob}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={dob}{name}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={dob}{lastname}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={lastname}{zipcode}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={username}{dob}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={username}{dob}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={username}{dob}{zipcode}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={username}{zipcode}{dob}@yahoo.com&t=email
- Epieos: https://epieos.com/?q={name}{zipcode}@yahoo.com.com&t=email

***************************************************************************
For any question contact vulnsec on Discord. Github https://github.com/vu1nsec
"""

        print(Colorate.Color(Colors.yellow, "\nCreating file..."))
        file_builder = open(f"{username}-Yahoo-List.txt", "w+")
        file_builder.write(f"{brute_list}")
        file_builder.close()
        time.sleep(1)
        return main()

#===================================================================================================================#
#===================================================================================================================#



    main_1_reponse = input(Colorate.Color(Colors.yellow, "[+] Choose : "))
    if main_1_reponse == "1":
        gmail_gathering()

    if main_1_reponse == "2":
        yahoo_gathering()

    if main_1_reponse == "3":
        print("Soon...")
        time.sleep(1)
        return main()

    if main_1_reponse == "4":
        print("Soon...")
        time.sleep(1)
        return main()

    if main_1_reponse == "5":
        print("Soon...")
        time.sleep(1)
        return main()
    
    if main_1_reponse != int:
        print("Error")
        time.sleep(1)
        return main()


if __name__ == "__main__":

    cmdconfig()
    main()

