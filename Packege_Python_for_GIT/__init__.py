#КАК ХРАНИТЬ КЛЮЧИ И ПАРОЛИ
#https://www.youtube.com/watch?v=XvLb-pRuyoU

###########################################################################
# import os
#
# with open('.env','r') as file:
#     line = file.readline()
#     os.environ[line[:line.find('=')]] = line[line.find('=') + 1:]
# API_KEY = os.environ['APY_KEY']

###########################################################################
import os
import dotenv
dotenv.load_dotenv('.env')
API_KEY = os.environ['APY_KEY']
print(API_KEY)
# gjjkl
print('rklj')