class UserQuerySetMixin():
    user_field = 'user'
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        lookup_data = {}
        lookup_data[self.user_field] = user
        return qs.filter(**lookup_data)

# def form_valid(self, form):
#         task1 = form.save(commit=False)
#         task1.author = User.objects.get(username=self.request.user.username)
#         task1.save()
#         return HttpResponseRedirect(self.success_url())