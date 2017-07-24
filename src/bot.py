#   Praw
#	Copyright (c) 2016, Bryce Boe
#	All rights reserved.

#	Redistribution and use in source and binary forms, with or without
#	modification, are permitted provided that the following conditions are met:

#	1. Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#	2. Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.

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

#	bot.py

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


from __future__ 					 import print_function, unicode_literals
from apscheduler.schedulers.blocking import BlockingScheduler

import praw
import os
import re
import bmemcached
import logging

from utils import *
from details import *

logging.basicConfig()
sched = BlockingScheduler()

mc = bmemcached.Client(os.environ.get('DATABASE_ENDPOINT'),
			os.environ.get('DATABASE_USERNAME'),
			os.environ.get('DATABASE_PASSWORD'))

reddit = praw.Reddit(user_agent=os.environ.get('REDDIT_UA'),
		username=os.environ.get('REDDIT_USERNAME'),
		password=os.environ.get('REDDIT_PASSWORD'),
		client_id=os.environ.get('REDDIT_CID'),
		client_secret=os.environ.get('REDDIT_CSC'))
		
subreddit = reddit.subreddit("petscop")

d = get_date_from_db(mc)

@sched.scheduled_job('interval', minutes=5)
def timed_job():
	global mc
	global reddit
	global subreddit
	
	update_block_list(reddit)
	update_date(mc, subreddit, d)
	
	print("Routine finished.")
	
sched.start()


