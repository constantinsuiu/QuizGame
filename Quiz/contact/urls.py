from django.urls import path
from .views import ContactUsView, Faq

app_name = 'contact'

urlpatterns = [
    path('contact-us/', ContactUsView.as_view(), name='contact_us'),
    path('faq/', Faq.as_view(), name='faq')
]
