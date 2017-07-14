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
import model

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
            'name1': self.request.get("username"),
            'name2': self.request.get("school"),
            'name3': self.request.get("schooladdress"),
            'name4': self.request.get("year"),
            'name5': self.request.get("block1"),
            'name6': self.request.get("block2"),
            'name7': self.request.get("block3"),
            'name8': self.request.get("block4"),
            'name9': self.request.get("block5"),
            'name10': self.request.get("block6"),
            'name11': self.request.get("block7"),
            'name12': self.request.get("grade1"),
            'name13': self.request.get("grade2"),
            'name14': self.request.get("grade3"),
            'name15': self.request.get("grade4"),
            'name16': self.request.get("grade5"),
            'name17': self.request.get("grade6"),
            'name18': self.request.get("grade7"),
            'name19': self.request.get("useraddress"),
            'name20': self.request.get("t1"),
            'name21': self.request.get("t2"),
            'name22': self.request.get("t3"),
            'name23': self.request.get("t4"),
            'name24': self.request.get("t5"),
            'name25': self.request.get("t6"),
            'name26': self.request.get("t7")
                   }
        reportcard=model.ReportCard()
        reportcard.address=self.request.get("schooladdress")
        reportcard.useraddress= self.request.get("useraddress")
        reportcard.put()
        reportcard.firstblock=self.request.get("block1")
        reportcard.secondblock=self.request.get("block2")
        reportcard.thirdblock= self.request.get("block3")
        reportcard.fifthblock=self.request.get("block4")
        reportcard.sixthblock=self.request.get("block6")
        reportcard.seventhblock= self.request.get("grade7")
        reportcard.firstblockteacher=self.request.get("t1")
        reportcard.second_block_teacher=self.request.get("t2")
        reportcard.third_block_teacher=self.request.get("t3")
        reportcard.fourth_block_teacher= self.request.get("t4")
        reportcard.fifth_block_teacher=self.request.get("t5")
        reportcard.sixth_block_teacher=self.request.get("t6")
        reportcardseventh_block_teacher=self.request.get("t7")
        key=reportcard.put()
        self.response.out.write(template.render(template_variables))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/report', ReportHandler),
], debug=True)
