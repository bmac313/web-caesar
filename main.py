#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar

encrypted_message = ""

class MainHandler(webapp2.RequestHandler):
	def get(self):
		text_input = "<textarea name='message'></textarea>"
		#text_output = "<input type='text' value='" + encrypted_message + "' />"
		page_content = """
		<!DOCTYPE html>
		<html>
			<head>
				<title>Caesar cipher</title>
			</head>
			<body>
				<h1>Caesar Ciper</h1>
				<h2>Text to encrypt:</h2>
				<form method="post" action="/sub">
					
		""" + text_input	+ """
		<br /> 
					<input type="submit" />
				</form>
			</body>
		</html>
		"""
		self.response.write(page_content)
		
class SubmitHandler(webapp2.RequestHandler):
	def post(self):
		page_content2 = ""
		if caesar.user_input_is_valid(self.request.get("message")):
			encrypted_message = caesar.encrypt(self.request.get("message"), 13)
			page_content2 += "<p>" + encrypted_message +"</p>"
		else:
			page_content2 += "<p>Error! Please type something before submitting!"
		page_content2 += "<a href='..'><button>Go back</button></a>"
		self.response.write(page_content2)
		#self.redirect('/')
		

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/sub', SubmitHandler)
], debug=True)
