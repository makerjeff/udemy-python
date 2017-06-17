import datetime # used to calculate dates and times.
import time     # useful for delaying.

print 'Now: {}'.format(datetime.datetime.now())

#calculate time deltas with datetime:
# NOTE: these are all date-time objects. Need to be converted to strings.
yesterday = datetime.datetime(2017, 6, 16, 0, 0)
now = datetime.datetime.now()
delta = now-yesterday

print 'Previous date: {}'.format(yesterday)
print 'Difference: {}'.format(delta)  #returns timedelta object
print 'Days: {}'.format(delta.days)
print 'Total seconds: {}'.format(delta.total_seconds())

print str(now)

# formating time strings
print now.strftime('%Y-%m%B-%d-%H-%M-%f')

# can do datetime calculations for future

after = now + datetime.timedelta(days=1, seconds=2000)
print after


# demonstrating time delays.
demo_list = []

for i in range(5):
    demo_list.append(datetime.datetime.now())
    print 'saving...'
    time.sleep(1)

for item in demo_list:
    print item.strftime('%Y-%m%B-%d-%M-%s-%f')

