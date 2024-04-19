from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Goals, Tasks
from accounts.models import Users
from .forms import GoalRegistForm, GoalUpdateForm, TaskRegistForm, TaskUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from datetime import datetime
from django.urls import reverse_lazy
    

# 夢一覧画面作る
class GoalListView(ListView, LoginRequiredMixin):
    model = Goals
    template_name = 'goal_list.html'


# 夢作成用画面作る（フォームあり）
class GoalRegistView(CreateView, LoginRequiredMixin):
    template_name = 'goal_regist.html'
    model = Goals
    form_class = GoalRegistForm
    success_url = reverse_lazy('goallist:goal_list')
    
    def form_valid(self, form):
        form.instance.created_at = datetime.now()
        form.instance.upload_at = datetime.now()
        goal = form.save(commit=False)
        goal.users_id = self.request.user.id
        goal.save()
        return super().form_valid(form)


# 夢編集画面
class GoalEditView(UpdateView, SuccessMessageMixin, LoginRequiredMixin):
    template_name = 'goal_edit.html'
    models = Goals
    form_class = GoalUpdateForm


# 夢の個別画面つくる
class GoalDetailView(DetailView, LoginRequiredMixin):
    model = Goals, Tasks
    template_name = 'goal_detail.html'


# タスク登録画面つくる（フォームあり）
class TaskRegistView(CreateView, LoginRequiredMixin):
    template_name = 'task_regist.html'
    form_class = TaskRegistForm


# タスク編集画面
class GoalEditView(UpdateView, SuccessMessageMixin, LoginRequiredMixin):
    template_name = 'task_edit.html'
    models = Tasks
    form_class = TaskUpdateForm


# 画像生成画面つくる（フォームは夢個別画面にボタンつくっておく？）