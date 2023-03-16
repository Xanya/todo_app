from django import forms
from .models import Task


class CreateTaskForm(forms.ModelForm):
    # def __init__(self, **kwargs):
    #     self.author = kwargs.pop('author', None)
    #     super(CreateTaskForm, self).__init__(**kwargs)

    # def save(self, commit=True):
    #     obj = super(CreateTaskForm, self).save(commit=False)
    #     obj.author = self.author
    #     if commit:
    #         obj.save()
    #     return obj

    class Meta:
        model = Task
        fields = ['title']



class TaskCompleted(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['completed']