from driverclass import DriverClass
from config import _CLIENTID
from islive import is_live_stream
import time

stream_status = is_live_stream(_CLIENTID)
while True:
	if stream_status:
		print("Overwatch League is live")
		driver = DriverClass()
		driver.get_owl()
		break
	else:
		print("Overwatch League is not live")
	time.sleep(300)



