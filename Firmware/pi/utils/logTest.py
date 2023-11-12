
# import sys

# new_path = '../../utils'
# sys.path.append(new_path)

from Loggoer import Logger
from datetime import datetime

dbg=Logger("module 1 ")
dbg.Log("helloworld")
current_time_ms = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(current_time_ms)
