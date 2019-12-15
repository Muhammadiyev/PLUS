from django.db import models
from users.models import User


class Lacal(models.Model):
    local_position = models.IntegerField(default=0)
    local_user = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE,related_name='local_of_user')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return "%s" % (self.user.username)

class Global(models.Model):
    global_position = models.IntegerField(default=0)
    global_user = models.ForeignKey(User,blank=True,null=True, on_delete=models.CASCADE,related_name='global_of_user')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % (self.user.username)
