from __future__ import unicode_literals

import datetime

from mongoengine import *
connect('taskApp')


class User(Document):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email_id = EmailField(required=True)
    date_of_birth = DateTimeField()
    gender = StringField()
    hometown = StringField()
    current_location = StringField()
    profile_link = URLField()
    fb_id = StringField()
    access_token = EmbeddedDocumentField(UserAuthToken)
    created_date = DateTimeField(editable=False)
    update_date = DateTimeField(add_now=True)

    def save(self):
        if not self.id:
            self.created_date = datetime.datetime.now()
        self.update_date = datetime.datetime.now()
        return super(User, self).save()
