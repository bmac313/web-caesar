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

class MainHandler(webapp2.RequestHandler):
	def get(self):
		message = ''
		page_content = """
		<!DOCTYPE html>
		<html>
			<head>
			</head>
			<body>
				<h1>Enter some text to encrypt:</h1>
				<form method="post" action="/submit">
					<textarea name="message">%s</textarea><br /> 
					<input type="submit" />
				</form>
			</body>
		</html>
		""" %(message)
		self.response.write(page_content)
		
class SubmitHandler(webapp2.RequestHandler):
	def post(self):
		if caesar.user_input_is_valid:
			MainHandler.message = caesar.encrypt(self.request.get("message"), 13)
		self.redirect('/')

app = webapp2.WSGIApplication([
	('/', MainHandler),
	('/submit', SubmitHandler)
], debug=True)
