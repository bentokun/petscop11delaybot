#   Praw
#   Copyright (c) 2016, Bryce Boe

#   ----------------------------------------------------------------------

#	timeutils.py

#   This file is a part of the Petscop11DelayBot
#   Copyright (c) 2017 Do Trong Thu

#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.

#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.

#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>. 


from datetime                        import datetime, timedelta

def numToMonth(shortMonth):
	return{
			1 : "Jan",
			2 : "Feb",
			3 : "Mar",
			4 : "Apr",
			5 : "May",
			6 : "Jun",
			7 : "Jul",
			8 : "Aug",
			9 : "Sep", 
			10 : "Oct",
			11 : "Nov",
			12 : "Dec"
	}[shortMonth]

def add_and_get_time(d):
	d = monthdelta(d, 1)
	return d
	
def sub_and_get_time(d):
	d = monthdelta(d, -1)
	return d

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)
	
def get_date_from_db(database):
	dt_key = 'Petscop11Date'
	dt_get_str = database.get(dt_key)

	if not dt_get_str:
		d=datetime.today()
	else:
		d=datetime.strptime(dt_get_str, '%b %Y')
		
	return d