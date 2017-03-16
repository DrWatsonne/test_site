
from django.db import models
from django.core.mail import mail_admins


class Message(models.Model):
    u"""
    A model that stores the status of sent messages
    """
    email = models.EmailField()
    status = models.CharField(max_length=10, default='')

    def __unicode__(self):
        return u'[%s] From: %s' % (self.status, self.email)

    def send(self, text, email):
        self.email = email
        sended_msg = mail_admins(self.email, text, False)
        if sended_msg > 0:
            self.status = u'Sended'
        else:
            self.status = u'Not sended'
        self.save()
        return self.status
