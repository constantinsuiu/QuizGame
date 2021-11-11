from django.urls import path, re_path
from .views import Games, EventPage, Profile, HomePage, Results, Payments

app_name = 'quiz'

urlpatterns = [
    path('', HomePage.as_view(), name='games-home'),
    path('games/<str:category>/', Games.as_view(), name='games-page'),
    path('games/<str:category>/<str:short_name>/', EventPage.as_view(), name='event-page'),
    path('account/profile/', Profile.as_view(), name='profile'),
    path('account/profile/<str:section>', Profile.as_view(), name='profile'),
    path('results/<str:category>/<str:short_name>/', Results.as_view(), name='results'),
    path('payments/', Payments.as_view(), name='payments'),
]
