from django.db import models
from django.utils import timezone

class TelegramUsers(models.Model):
    session_id = models.CharField(max_length=56, unique=True)
    tg_id = models.CharField(max_length=56, default="no-auth")
    name = models.CharField(max_length=56, default="no-auth")
    stocks_id = models.JSONField(default=dict)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.tg_id
    class Meta:
        ordering = ['-created']

class Orgs(models.Model):
    boss_tg = models.CharField(max_length=56, default="no-auth")
    name = models.CharField(max_length=56, default="no-name")
    created = models.DateTimeField(default=timezone.now)
    workers = models.ManyToManyField(TelegramUsers)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-created']

#

#// MiddleWare /organisation/<id>/
# session.tg_id in Org.Emploers(filter organisation id)
# if not => fck you page
# if yes => show navbar col

#// HTML templates
# navbar row
# navbar col

#// webpage names
#// webpage icons






