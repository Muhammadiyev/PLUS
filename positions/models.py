from django.db import models
from users.models import User

class Local(models.Model):
    local_position = models.IntegerField(default=0,blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    local_user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.local_user)

class Global(models.Model):
    global_position = models.IntegerField(default=0,blank=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    global_user = models.ForeignKey(User,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.global_user)

