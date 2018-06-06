import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# DB_PATH='%s\%s\%s' %(BASE_DIR,'db','db.txt')
DB_PATH=os.path.join(BASE_DIR,'db','db.txt')
LOG_PATH=os.path.join(BASE_DIR,'log','access.log')
