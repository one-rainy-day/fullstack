import pytz
from datetime import datetime
from pytz import timezone


print(datetime.now(pytz.utc))

print(datetime.today())

# print(pytz.country_names['au'])
# print(pytz.country_timezones['au'])
format = "%Y-%m-%d %H:%M:%S %Z%z"
now_utc = datetime.now(timezone('UTC'))
print(now_utc.strftime(format))

ist = pytz.timezone('Australia/Sydney')
local_datetime = ist.localize(datetime.now())
print('IST Current Time =', local_datetime.strftime(format))

formatdate = "%Y-%m-%d"
print('IST Current Date =', local_datetime.strftime(formatdate))