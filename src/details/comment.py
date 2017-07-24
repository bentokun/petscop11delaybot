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

#	comment.py

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


import praw
import re
import bmemcached

def update_date(database, subreddit, date):
	for comment in subreddit.comments(limit=None):
			if re.search("Petscop 11", comment.body, re.IGNORECASE):
				if not database.get(comment.id) and not database.get(comment.author.name):
					d2 = add_and_get_time(date)
					dt_str = numToMonth(d.month) + " " + str(d.year)
					database.set(dt_key, dt_str)
					
					reply_mess=("You have mentioned Petscop Eleven (number form). Now Petscop Eleven is estimated for release in {0} {1}! \n\n ^I'm ^a ^bot ^lol. ^This ^bot ^only ^works ^on ^Petscop ^Reddit ^and ^will ^be ^shut ^down ^on ^26/7/2017 ^or ^sooner. ^If ^you ^feel ^that ^I'm ^annoying ^in ^three ^days, ^you ^can ^block ^me ^by ^inbox ^or ^comment: ^!BLOCK. ^If ^you ^want ^to ^unblock ^me, ^send: ^!UNBLOCK. ^Seriously, ^I'm ^a ^copy ^of ^/u/SeriouslyWhenIsHL3.").format(numToMonth(d2.month), d2.year)
					
					try:
						comment.reply(reply_mess)
						print("Comment= ", comment.body, " ; CommentID= ", comment.id, "replied")
						mc.set(comment.id, "True")
					except:
						print("Error happened with comment id: ", comment.id)
						
						d2=sub_and_get_time(d)
						dt_str = numToMonth(d.month) + " " + str(d.year)
						mc.set(dt_key, dt_str)
						pass
					
					pass
				else:
					print("Comment= ", comment.body, " ; CommentID= ", comment.id, "replied")
			
		
	pass