from typing import Any
from datetime import datetime
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from .forms import RegistForm, UserLoginForm, UserEditForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Users
from django.shortcuts import render, redirect


class HomeView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time'] = datetime.now()
        return context


class RegisterUserView(CreateView):
    template_name = 'user_regist.html'
    form_class = RegistForm
    success_url = reverse_lazy('accounts:user_login')
    
    def form_valid(self, form):
        form.instance.created_at = datetime.now()
        form.instance.upload_at = datetime.now()
        return super(RegisterUserView, self).form_valid(form)


class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm
    
    def form_valid(self, form):
        remember = form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1209600) #ログイン保持状態にチェックがあれば2週間(1209600)保持する
        return super().form_valid(form)
        

class UserLogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('accounts:user_login')

# class UserLogoutView(LogoutView):
#     pass
    

class UserEditView(UpdateView, SuccessMessageMixin, LoginRequiredMixin): #ログインしないと実行できなくする
    template_name = 'user_edit.html'
    model = Users
    form_class = UserEditForm
    success_message = '更新しました'
    
    def get_success_url(self):
        return reverse_lazy('accounts:home')
    
    def get_success_message(self, cleaned_data):
        return cleaned_data.get('username') + 'を更新しました'
        
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     picture_form = forms.PictureUploadForm()
    #     pictures = Pictures.objects.filter_by_book(book=self.object)
    #     context['pictures'] = pictures
    #     context['picture_form'] = picture_form
    #     return context
    
    # def post(self, request, *args, **kwargs):
    #     # 画像をアップロードする処理を描く
    #     picture_form = forms.PictureUploadForm(request.POST or None, request.FILES or None)
    #     if picture_form.is_valid() and request.FILES:
    #         book = self.get_object() # 今更新しているbookがどのbookなのかわかる
    #         picture_form.save(book=book)
    #     return super(BookUpdateView, self).post(request, *args, **kwargs)
        
    
    def model_form_upload(request):
        user = None
        if request.method == 'POST':
            form = UserEditForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save()
        return render(request, 'home.html', context={'form': form, 'user': user})