
from allauth.account.views import SignupView, LoginView, PasswordResetView

# Create your views here
class MySignupView(SignupView):
    template_name = 'signup.html'


class MyLoginView(LoginView):
    template_name = 'login.html'


class MyPasswordResetView(PasswordResetView):
    template_name = 'password_reset.html'
