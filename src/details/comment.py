#	Praw
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

from utils import *
from random import randint

def update_date(database, subreddit, date):
	for comment in subreddit.comments(limit=None):
			if re.search("Petscop 11", comment.body, re.IGNORECASE):
				if not database.get(comment.id) and not database.get(comment.author.name):
					
					if comment.author.name == "Renaaaaaaaaaaaaaaaaa" or comment.author.name == "lonkish" or comment.author.name == "c-d-hogg":
						date = add_year_and_get_time(date)
					else:
						date = add_and_get_time(date)
					
					dt_str = numToMonth(date.month) + " " + str(date.year)
					dt_key = "Petscop11Date"
					
					database.set(dt_key, dt_str)
					
					if comment.author.name == "c-d-hogg":
						reply_mess = "Paul detected, delay 1 more year. If Paul want things to be normal again, contact /u/palaskowitz or /u/naul_is_my_lover. \n\n *** \n\n ^I'm ^a ^bot ^lol. ^This ^bot ^only ^works ^on ^Petscop ^Reddit. ^If ^you ^feel ^that ^I'm ^annoying ^, ^you ^can ^block ^me ^by ^inbox ^or ^comment: ^!BLOCK. ^If ^you ^want ^to ^unblock ^me, ^send: ^!UNBLOCK. ^If ^mods ^want ^to ^stop ^this ^bot, ^contact ^/u/palaskowitz ^or ^/u/naul_is_my_lover."
					elif comment.author.name == "Renaaaaaaaaaaaaaaaaa":
						reply_mess = ("Jake Paul detected, delay Petscop 1 year. Now Petscop Eleven is estimated for release in {0} {1}. \n\n *** \n\n ^I'm ^a ^bot ^lol. ^This ^bot ^only ^works ^on ^Petscop ^Reddit. ^If ^you ^feel ^that ^I'm ^annoying ^, ^you ^can ^block ^me ^by ^inbox ^or ^comment: ^!BLOCK. ^If ^you ^want ^to ^unblock ^me, ^send: ^!UNBLOCK. ^If ^mods ^want ^to ^stop ^this ^bot, ^contact ^/u/palaskowitz ^or ^/u/naul_is_my_lover.").format(numToMonth(date.month), date.year)
					elif comment.author.name == "lonkish":
						reply_mess = "Russian detected, afaird of Putin, delay Petscop 1 year. Now Petscop Eleven is estimated for release in {0} {1}. \n\n *** \n\n ^I'm ^a ^bot ^lol. ^This ^bot ^only ^works ^on ^Petscop ^Reddit. ^If ^you ^feel ^that ^I'm ^annoying ^, ^you ^can ^block ^me ^by ^inbox ^or ^comment: ^!BLOCK. ^If ^you ^want ^to ^unblock ^me, ^send: ^!UNBLOCK. ^If ^mods ^want ^to ^stop ^this ^bot, ^contact ^/u/palaskowitz ^or ^/u/naul_is_my_lover.".format(numToMonth(date.month), date.year)
					else:
						reply_mess=("Oh no, what have you done you ding dong? You have mentioned Petscop Eleven. Now Petscop Eleven is now estimated for release in {0} {1}! \n\n *** \n\n ^I'm ^a ^bot ^lol. ^This ^bot ^only ^works ^on ^Petscop ^Reddit. ^If ^you ^feel ^that ^I'm ^annoying ^, ^you ^can ^block ^me ^by ^inbox ^or ^comment: ^!BLOCK. ^If ^you ^want ^to ^unblock ^me, ^send: ^!UNBLOCK. ^If ^mods ^want ^to ^stop ^this ^bot, ^contact ^/u/palaskowitz ^or ^/u/naul_is_my_lover.").format(numToMonth(date.month), date.year)
					
					try:
						comment.reply(reply_mess)
						print("Comment= ", comment.body, " ; CommentID= ", comment.id, "replied")
						database.set(comment.id, "True")
					except:
						print("Error happened with comment id: ", comment.id)
						
						date=sub_and_get_time(date)
						dt_str = numToMonth(date.month) + " " + str(date.year)
						database.set(dt_key, dt_str)
						pass
					
					pass
				else:
					print("Comment= ", comment.body, " ; CommentID= ", comment.id, "replied")
				pass
			elif re.search("bad bot", comment.body, re.IGNORECASE) and comment.parent().author.name == "palaskowitz":
				print("Some one say bad bot: ")
			
				if not database.get(comment.id) and not database.get(comment.author.name):
						
					reply_mess=["I'm legit crying rn", "Kys", "Sorry, {0}".format(comment.author.name), "E N G L A N D I S M Y C I T Y", "/u/SeriouslyWhenIsHL3"]
						
					try:
						comment.reply(reply_mess[randint(0, 5)])
						print("Comment= ", comment.body, " ; CommentID= ", comment.id, "replied")
						database.set(comment.id, "True")
					except:
						print("Error happened with comment id: ", comment.id)
							
						pass
						
					pass
				else:
					print("Comment= ", comment.body, " ; CommentID= ", comment.id, "replied")
				pass
			elif re.search("c-d-hogg", comment.body, re.IGNORECASE):
				if not database.get(comment.id) and not database.get(comment.author.name):
					date = sub_and_get_time(date)
					dt_str = numToMonth(date.month) + " " + str(date.year)
					dt_key = "Petscop11Date"
					
					database.set(dt_key, dt_str)
						
					reply_mess="By mentioning Paul you have earlier the release date of Petscop Eleven by 1 month. Now Petscop Eleven is estimated for release in {0} {1}! Yayyyy! \n\n *** \n\n ^I'm ^a ^bot ^lol. ^This ^bot ^only ^works ^on ^Petscop ^Reddit. ^If ^you ^feel ^that ^I'm ^annoying ^, ^you ^can ^block ^me ^by ^inbox ^or ^comment: ^!BLOCK. ^If ^you ^want ^to ^unblock ^me, ^send: ^!UNBLOCK. ^If ^mods ^want ^to ^stop ^this ^bot, ^contact ^/u/palaskowitz ^or ^/u/naul_is_my_lover.".format(numToMonth(date.month), date.year)
						
					try:
						comment.reply(reply_mess)
						print("Comment= ", comment.body, " ; CommentID= ", comment.id, "replied")
						database.set(comment.id, "True")
					except:
						print("Error happened with comment id: ", comment.id)
							
						date=add_and_get_time(date)
						dt_str = numToMonth(date.month) + " " + str(date.year)
						database.set(dt_key, dt_str)
						pass
						
					pass
				else:
					print("Comment= ", comment.body, " ; CommentID= ", comment.id, "replied")
				pass
	
			
	return date
	
	pass