from django.db import models
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime
from accounts.models import Users



class BaseMeta(models.Model):
    created_at = models.DateTimeField(default=datetime.now())
    upload_at = models.DateTimeField(default=datetime.now())
    
    class Meta:
        abstract = True


class Goals(BaseMeta):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    goal_title = models.CharField(max_length=100)
    goal_detail = models.CharField(max_length=200)
    goal_condition = models.IntegerField(blank=True, default=0)
    
    class Meta:
        db_table = 'goals'
    
    def get_absolute_url(self):
        return reverse_lazy('goallist:goal_detail', kwargs={'pk': self.pk})
    


class Tasks(BaseMeta):
    goals = models.ForeignKey('Goals', on_delete=models.CASCADE)
    
    task_title = models.CharField(max_length=100)
    task_condition = models.IntegerField(default='0', blank=False, null=False,)
    task_priority = models.IntegerField(default='0', blank=False, null=False)
    task_due = models.DateField(default=timezone.now)
    
