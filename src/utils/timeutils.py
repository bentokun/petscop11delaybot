#   Praw
#	Copyright (c) 2016, Bryce Boe
#	All rights reserved.

#	Redistribution and use in source and binary forms, with or without
#	modification, are permitted provided that the following conditions are met:

#	1. Redistributions of source code must retain the above copyright notice, this
#	list of conditions and the following disclaimer.
#	2. Redistributions in binary form must reproduce the above copyright notice,
#	this list of conditions and the following disclaimer in the documentation
#	and/or other materials provided with the distribution.

#	THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#	ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#	WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#	DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#	FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#	DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#	SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#	CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#	OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#	OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#   ----------------------------------------------------------------------

#	timeutils.py

#	This file is a part of the Petscop11DelayBot
#	Copyright (c) 2017 Do Trong Thu

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