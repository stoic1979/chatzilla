from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Room(models.Model):
    """
    model for a chat room
    """
    name = models.CharField(max_length=64)
    created_by = models.ForeignKey(User)
    active = models.BooleanField(_('Active'), default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))

    def __unicode__(self):
        return self.name


class Message(models.Model):
    """
    message model to store a chat message
    """
    content = models.TextField()
    sender = models.ForeignKey(User, related_name='sender_id')
    receiver = models.ForeignKey(User, related_name='receiver_id')
    room = models.ForeignKey(Room)
    is_read = models.BooleanField(_('Read'), default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))

    def __unicode__(self):
	return self.content[:30]
