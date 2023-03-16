from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages
from django.views.generic import UpdateView, DeleteView, ListView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task
from .forms import CreateTaskForm, TaskCompleted

# Create your views here.

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    template_name = 'base/task_update.html'
    fields = ['title', 'description', 'active', 'completed']

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'base/task_delete.html'
    success_url = '/'

    def test_func(self):
        task = self.get_object()
        if self.request.user == task.author:
            return True
        return False


class TaskListView(CreateView):
    
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/home.html'
    form_class = CreateTaskForm
    success_url = '/'
    exclude = ['author']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Your task has been created!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        if not self.request.user.id:
            kwargs['tasks'] = Task.objects.none()
            kwargs['tasks_len'] = 0
            return super(TaskListView, self).get_context_data(**kwargs) 
        kwargs['tasks'] = Task.objects.filter(author=self.request.user, completed=False).order_by('-date_created')
        kwargs['tasks_len'] = len(Task.objects.filter(author=self.request.user, active=True, completed=False))
        return super(TaskListView, self).get_context_data(**kwargs)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     return qs.filter(author=self.request.user, completed=False).order_by('-date_created')

    """ def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['form'] = CreateTaskForm()
        return context """

# def home(request):
#     if request.method == 'POST':
#         form = CreateTaskForm(author=request.user, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Your task has been created!')
#             return redirect('todo-home')
#     else:
#         form = CreateTaskForm()

#     if request.user.id:
#         context = {
#             'tasks': Task.objects.filter(author=request.user, completed=False).order_by('-date_created'),
#             'form': form,
#             'tasks_len': len(Task.objects.filter(author=request.user, active=True))
#         }
#     else:
#         context = {

#             }
    
#     return render(request, 'base/home.html', context)