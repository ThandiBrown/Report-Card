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
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('main.html')
        self.response.write(template.render())

class ReportHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('report.html')
        template_variables = {
            'stdname': self.request.get("stdname"),
            'stdstr': self.request.get("stdstr"),
            'stdtown': self.request.get("stdtown"),
            'stdID': self.request.get("stdID"),
            'grade': self.request.get("grade"),
            'hometeacher': self.request.get("hometeacher"),
            'schoolname': self.request.get("schoolname"),
            'principal': self.request.get("principal"),
            'schoolstr': self.request.get("schoolstr"),
            'schooltown': self.request.get("schooltown"),
            'schoolphone': self.request.get("schoolphone"),
            'schoolyear': self.request.get("schoolyear"),
            'countyname': self.request.get("countyname"),
            'class1': self.request.get("class1"),
            'class2': self.request.get("class2"),
            'class3': self.request.get("class3"),
            'class4': self.request.get("class4"),
            'class5': self.request.get("class5"),
            'class6': self.request.get("class6"),
            'class7': self.request.get("class7"),
            't1': self.request.get("t1"),
            't2': self.request.get("t2"),
            't3': self.request.get("t3"),
            't4': self.request.get("t4"),
            't5': self.request.get("t5"),
            't6': self.request.get("t6"),
            't7': self.request.get("t7"),
            'g1': self.request.get("g1"),
            'g2': self.request.get("g2"),
            'g3': self.request.get("g3"),
            'g4': self.request.get("g4"),
            'g5': self.request.get("g5"),
            'g6': self.request.get("g6"),
            'g7': self.request.get("g7"),
            'abs1': self.request.get("abs1"),
            'abs2': self.request.get("abs2"),
            'abs3': self.request.get("abs3"),
            'abs4': self.request.get("abs4"),
            'abs5': self.request.get("abs5"),
            'abs6': self.request.get("abs6"),
            'abs7': self.request.get("abs7"),
            'tlabs': self.request.get("tlabs"),
            'tdy1': self.request.get("tdy1"),
            'tdy2': self.request.get("tdy2"),
            'tdy3': self.request.get("tdy3"),
            'tdy4': self.request.get("tdy4"),
            'tdy5': self.request.get("tdy5"),
            'tdy6': self.request.get("tdy6"),
            'tdy7': self.request.get("tdy7"),
            'tltdy': self.request.get("tltdy"),

                   }
        self.response.out.write(template.render(template_variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/report', ReportHandler),
], debug=True)
