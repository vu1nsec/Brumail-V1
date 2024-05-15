from os import system
from pystyle import *
from colorama import Fore
import time
import os

# def install_requirements():
#    system('pip install pystyle')
#    system('pip install colorama')

def cmdconfig():
    system('title Brumail v1.0 VulnSec')
    cmd = 'mode 110,30'
    os.system(cmd)

def clear():
    system('cls')

def main():
    clear()
    print(f""" 
                               {Fore.YELLOW}____________ _   ____  ___  ___  _____ _     
                               {Fore.YELLOW}| ___ \ ___ \ | | |  \/  | / _ \|_   _| |    
                               {Fore.YELLOW}| |_/ / |_/ / | | | .  . |/ /_\ \ | | | |    
                               {Fore.YELLOW}| ___ \    /| | | | |\/| ||  _  | | | | |    
                               {Fore.YELLOW}| |_/ / |\ \| |_| | |  | || | | |_| |_| |____
                               {Fore.YELLOW}\____/\_| \_|\___/\_|  |_/\_| |_/\___/\_____/{Fore.WHITE}
                                
                                    {Fore.RED}[|]{Fore.WHITE} https://github.com/vu1nsec {Fore.RED}[|]{Fore.WHITE}
                                    {Fore.RED}[|]{Fore.WHITE}           v1.0 {Fore.RED}            [|]{Fore.WHITE}""")

    print(f"""          

                                              {Fore.YELLOW}[1]{Fore.WHITE} GMAIL
                                              {Fore.YELLOW}[2]{Fore.WHITE} YAHOO
                                              {Fore.YELLOW}[3]{Fore.WHITE} OUTLOOK
                                              {Fore.YELLOW}[4]{Fore.WHITE} PROTON
                                              {Fore.YELLOW}[5]{Fore.WHITE} ICLOUD
        
""")
    
#===================================================================================================================
#===================================================================================================================

    def back_to_main():
        print(f"{Fore.GREEN}[+]{Fore.WHITE} Going back to Main...")
        time.sleep(1)
        return main()

    def gmail_gathering():
        clear()
        print(Colorate.Color(Colors.yellow, "Informations Needed : Username, Name, Lastname, Dob, Zipcode\n"))
        username = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Username : ").lower()
        if username == "":
            print(f"{Fore.RED}[!]{Fore.WHITE} Invalid Username")
            time.sleep(1)
            return gmail_gathering()
        name     = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Name     : ").lower()
        if name == "":
            print(f"{Fore.RED}[!]{Fore.WHITE} Invalid Name")
            time.sleep(1)
            return gmail_gathering()
        lastname = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Lastname : ").lower()
        if lastname == "":
            print(f"{Fore.RED}[!]{Fore.WHITE} Invalid Lastname")
            time.sleep(1)
            return gmail_gathering()
        dob      = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Dob Year : ").lower()
        if dob == "":
            print(f"{Fore.RED}[!]{Fore.WHITE} Invalid Dob Year")
            time.sleep(1)
            return gmail_gathering()
        zipcode  = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Zipcode  : ").lower()
        if zipcode == "":
            print(f"{Fore.RED}[!]{Fore.WHITE} Invalid Zipcode")
            time.sleep(1)
            return gmail_gathering()
        
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
        print(f"{Fore.GREEN}[+]{Fore.WHITE} File Created !")
        back_to_main()

#===================================================================================================================#
#===================================================================================================================#

    def yahoo_gathering():
        clear()
        print(Colorate.Color(Colors.yellow, "Informations Needed : Username, Name, Lastname, Dob, Zipcode\n"))
        username = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Username : ").lower()
        if username == "":
            print(f"{Fore.RED}[!]{Fore.WHITE} Invalid Username")
            time.sleep(1)
            return yahoo_gathering()
        name     = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Name     : ").lower()
        if name == "":
            print(f"{Fore.RED}[!]{Fore.WHITE} Invalid Name")
            time.sleep(1)
            return yahoo_gathering()
        lastname = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Lastname : ").lower()
        if lastname == "":
            print(f"{Fore.RED}[!]{Fore.WHITE} Invalid Lastname")
            time.sleep(1)
            return yahoo_gathering()
        dob      = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Dob Year : ").lower()
        if dob == "":
            print(f"{Fore.RED}[!]{Fore.WHITE} Invalid Dob Year")
            time.sleep(1)
            return yahoo_gathering()
        zipcode  = input(f"{Fore.YELLOW}[+]{Fore.WHITE} Zipcode  : ").lower()
        if zipcode == "":
            print(f"{Fore.RED}[!]{Fore.WHITE} Invalid Zipcode")
            time.sleep(1)
            return yahoo_gathering()

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
        print(f"{Fore.GREEN}[+]{Fore.WHITE} File Created !")
        back_to_main()

#===================================================================================================================#
#===================================================================================================================#

    main_1_reponse = input(Colorate.Color(Colors.yellow, "                                              [+] Choose : "))
    if main_1_reponse == "1":
        gmail_gathering()

    elif main_1_reponse == "2":
        yahoo_gathering()

    elif main_1_reponse == "3":
        print("Soon...")
        time.sleep(1)
        return main()

    elif main_1_reponse == "4":
        print("Soon...")
        time.sleep(1)
        return main()

    elif main_1_reponse == "5":
        print("Soon...")
        time.sleep(1)
        return main()
    
    else:
        print(f"{Fore.RED}                                              [-]{Fore.WHITE} Error !")
        time.sleep(1)
        return main()

if __name__ == "__main__":

    # install_requirements()
    cmdconfig()
    main()

