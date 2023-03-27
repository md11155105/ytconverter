#I DON'T KNOW SHELL COMMANDS SO I AM USING #PYTHON TO CONNECT WITH SHELL, JUST RUN THE #BELOW COMMAND TO UPDATE 'YT Converter' TOOL. #AFTER UPDATING IF ANY ERROR OCCURS TAKE A #SCREENSHOT AND EMAIL ME WITH ATTACHING THE #SCREENSHOT.

#COMMAND :
# $ 'python update.py'

import os
os.chdir('/data/data/com.termux/files/home')
os.system('mv ytconverter bytconverter')
os.system('git clone https://github.com/kaifcodec/ytconverter.git')
os.system('rm -f $HOME/bytconverter ')

print("\n RESTART YOUR TERMUX APPLICATION AND 'YT Converter' tool.")
