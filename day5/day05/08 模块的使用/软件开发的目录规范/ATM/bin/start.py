# 强调：只有被导入的模块才能使用.或者..的语法

import sys
import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import src

if __name__ == '__main__':
    src.run()
