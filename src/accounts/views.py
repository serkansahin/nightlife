from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.forms import UserRegistrationForm
from accounts.models import CustomUser

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class SignUpView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
class UserDetailView(DetailView):
    model = CustomUser
    template_name = "registration/user_details.html"
    context_object_name = "user"

@method_decorator(login_required, name="dispatch")
class UserUpdate(UpdateView):
    model = CustomUser
    template_name = "registration/user_update.html"
    fields = ['username', 'town', 'thumbnail',]