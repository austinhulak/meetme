import datetime

days = ['Mon.', 'Tues.', 'Wed.', 'Thurs', 'Fri.', 'Sat.', 'Sun.']

def get_available_times():
	now = datetime.datetime.today()
	day = now.weekday()
	time_rng = get_time_range(now)

	available = ['{} {}'.format(days[day], time_rng)]	
	for i in range(2):
		[next, next_day, next_rng] = get_next_time_range(day, time_rng)
		day = next_day
		time_rng = next_rng
		available.append(next)
	
	return available

def get_time_range(time):
	hr = time.hour
	rng = None

	if (hr < 13):
		rng = 'morning'
	elif (hr < 17):
		rng = 'afternoon'
	else:
		rng = 'evening'

	return rng


def get_next_time_range(day, time_rng):
	next = None
	tomorrow = (day + 1) % 7

	if (time_rng == 'morning'):
		next_day = day
		next_rng = 'afternoon'
	elif (time_rng == 'afternoon'):
		next_day = day
		next_rng = 'evening'
	else:
		next_day = tomorrow
		next_rng = 'morning'

	next = '{} {}'.format(days[next_day], next_rng)	
	return [next, next_day, next_rng]


if (__name__ == '__main__'):
	avail = get_available_times()
	for a in avail:
		print(a)
