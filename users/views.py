from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, UpdateView
from .forms import UserRegisterForm
from base.models import Task
from .models import Achievment
from django.contrib.auth.models import User

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    context = {
        'tasks':Task.objects.filter(author=request.user, completed=True)[::-1]
    }
    return render(request, 'users/profile.html', context)

class ProfileView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'users/profile.html'
    context_object_name = 'tasks'
    achievments_list = ['begginer', 'mid', 'advance']

    def get_queryset(self):
        qs = super().get_queryset()
        # if len(qs.filter(author=self.request.user, completed=True)) == 3:
        #     achievment = Achievment.objects.get(title='Beginner')
        #     achievment.users.add(self.request.user)
        #     messages.success(self.request, f'You got an achievment!')
        return qs.filter(author=self.request.user, completed=True).order_by('-date_created')

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        achievments = Achievment.objects.filter(users=self.request.user)
        context['achievments'] = achievments
        return context

class CompletedUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    template_name = 'users/completed_update.html'
    fields = ['completed']
    success_url = '/profile'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False

    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)
        qs = Task.objects.all()
        if len(qs.filter(author=self.request.user, completed=True)) == 3:
            achievment = Achievment.objects.get(title='Beginner')
            achievment.users.add(self.request.user)
            print(len(qs.filter(author=self.request.user, completed=True)))
            messages.success(self.request, f'You got an achievment!')
        return data

achievments_list = ['begginer', 'mid', 'advance']

@login_required
def achievments_view(request):
    if not request.user.id:
        tasks_len = 0
        context = {
                'achievment': achievments_list[0]
            }
    else:
        tasks_len = len(Task.objects.filter(author=request.user, completed=True))
        if tasks_len >= 10 and tasks_len < 15:
            context = {
                'achievment': achievments_list[0]
            }
    return render(request, 'users/achievments.html', context)
        