from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import  reverse_lazy
from django.views.generic import ListView, FormView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .forms import ContactForm
from .models import ContactUs, FAQ


# Create your views here.
class ContactUsView(SuccessMessageMixin, FormView):
    form_class = ContactForm
    template_name = 'contact_us.html'
    success_url = reverse_lazy('quiz:profile')
    success_message = 'We have received your message and try to reply as soon as possible.'

    def get(self, request, *args, **kwargs):
        form = ContactForm(request, request.GET or None)
        return render(self.request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactForm(request, request.POST)
        if form.is_valid():
            messages.success(self.request, 'Test message')
            self.form_actions(form)
        return render(self.request, self.template_name, {'form': form})

    def form_actions(self, form):
        email = form.cleaned_data["email"]
        message_type = form.cleaned_data["type"]
        event = form.cleaned_data["event"]
        text = form.cleaned_data["text"]
        message = ContactUs(email=email, type=message_type, event=event, text=text)
        message.save()
        send_mail(
            subject="You got a new {}".format(message_type),
            message="The user {} sent the following text: <br> {}".format(email, text),
            from_email=email,
            recipient_list=["constantin.suiu@me.com"],
            fail_silently=False
        )


class Faq(ListView):
    context_object_name = 'data'
    model = FAQ
    template_name = 'faq.html'
