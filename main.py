from driverclass import DriverClass
from config import _CLIENTID, _USERNAME, _PASSWORD
from islive import is_live_stream
import time


while True:
	stream_status = is_live_stream(_CLIENTID)
	if stream_status:
		print("Overwatch League is live")
		driver = DriverClass()
		time.sleep(5)
		driver._get_owl()
		driver._login(_USERNAME, _PASSWORD)
		break
	else:
		print("Overwatch League is not live")
	time.sleep(300)



