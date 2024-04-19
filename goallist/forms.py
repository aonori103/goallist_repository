from django import forms
from .models import Goals, Tasks, Users
from datetime import datetime
from requests import request



# 夢編集用画面とフォーム作る。
class GoalRegistForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ['goal_title', 'goal_detail']
        success_message = '登録しました'
    
    def save(self, *args, **kwargs):
        obj = super(GoalRegistForm, self).save(commit=False)
        obj.created_at = datetime.now()
        obj.upload_at = datetime.now()
        obj.save()
        return obj


class GoalUpdateForm(forms.ModelForm):
    class Meta:
        model = Goals
        fields = ['goal_title', 'goal_detail', 'goal_condition']
        success_message = '更新しました'
    
    # def get_success_url(self):
    #     return reverse_lazy('accounts:home')
    
    def save(self, *args, **kwargs):
        obj = super(GoalUpdateForm, self).save(commit=False)
        obj.update_at = datetime.now()
        obj.save()
        return obj


# タスク編集用画面とフォーム作る。
class TaskRegistForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_title', 'task_condition', 'task_priority', 'task_due']
        success_message = 'タスクを登録しました'
    
    # def get_success_url(self):
    #     return reverse_lazy('accounts:home')
    
    def save(self, *args, **kwargs):
        obj = super(TaskRegistForm, self).save(commit=False)
        obj.created_at = datetime.now()
        obj.upload_at = datetime.now()
        obj.save()
        return obj


class TaskUpdateForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['task_title', 'task_condition', 'task_priority', 'task_due']
        success_message = 'タスクを更新しました'
    
    # def get_success_url(self):
    #     return reverse_lazy('accounts:home')
    
    def save(self, *args, **kwargs):
        obj = super(TaskUpdateForm, self).save(commit=False)
        obj.update_at = datetime.now()
        obj.save()
        return obj


