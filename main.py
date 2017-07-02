# Copyright 2016 Google Inc.
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

import webapp2
import datetime

# self.response is sort of a global response object
# it sets the content type header to text/plain, by default its text/html

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
now = datetime.datetime.now()

def valid_month(month):
		
		if month:
			mon = month.capitalize()
			if mon in months :
				return mon

def valid_day(day):
		if day and day.isdigit():
			date=int(day)

			if date>0 and date<=31:
				return date

def valid_year(year):
		if year and year.isdigit():
			years=int(year)
			if(years>1900 and years<=2020):
				return years	


form= """
<form method ="post">
	<h1>When is your birthday ? </h1>

	<br>
	
	<label> Month* <input type="text" name='month'></label>

	<label> Date <input type="text" name='day'></label>

	<label> Year* <input type="text" name='year'></label>
	
	<div style= "color:red"> %(error)s </div>
	<br>
	<br>
	<input type="Submit">
</form>

 """


# request is the object representing the request that came from browser
#we call "get" on it to get query parameters
#response is the object representing the response sent to back to client
#class TestHandler(webapp2.RequestHandler):
#	def post(self):
#		self.response.headers['Content-Type'] = 'text/plain'
#		self.response.out.write(self.request)
#		# self.response is python request object which is similar to HTTP request
#		#q=self.request.get("q")
#		#self.response.out.write(q)

class MainPage(webapp2.RequestHandler):
	# when we open MainPage , the browser make a GET Request by default hence we define the get method
	
	def write_form(self,error=""):
		self.response.out.write(form % {"error":error})
	
	def get(self):
	   # self.response.headers['Content-Type'] = 'text/plain'
		self.write_form()

	def post(self):
		

		user_month = valid_month(self.request.get('month'))
		user_day = valid_day(self.request.get('day'))
		user_year = valid_year(self.request.get('year'))
		

		if not (user_month and user_day and user_year):
			self.write_form("That dosen't look valid to me, friend !")
		else:
			self.response.out.write("Thanks for entering valid date")

	



			#below is URL mapping section .. # URL references to handlers , all handlers are our various website pages which are classes
# this has 1 URL ('/'   i.e. main page) and it maps to handler called MainPage
# MainPage class is defined above
# it inherits from webapp2.RequestHandler
# webapp2.RequestHandler is a generic request handler from google

app = webapp2.WSGIApplication([
	('/',MainPage),
], debug=True)


