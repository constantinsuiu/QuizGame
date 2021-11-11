from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator

import pytz

from .models import Game, Question, Answer, UserVote, UserPoints
from .decorators import user_has_balance, can_user_view
from .selectors import get_top_5_events, get_soon_to_expire_events, get_event_by_short_name, get_user_votes
from .services import save_user_answers, update_bank, update_user_balance

utc = pytz.UTC


# Create your views here.
class HomePage(ListView):
    template_name = 'home.html'
    context_object_name = 'data'

    def get_queryset(self):
        top_games = get_top_5_events()
        soon_to_expire = get_soon_to_expire_events()
        return {'top_games': top_games, "soon_to_expire": soon_to_expire}


class Games(ListView):
    context_object_name = 'data'
    model = Game
    template_name = 'games_list.html'

    def get_queryset(self):
        user_played_games = []
        if self.request.user.is_authenticated:
            user_played_games = [x.event.short_name for x in get_user_votes(user=self.request.user)]
        games = Game.objects.filter(question_category__category=self.kwargs["category"]).order_by("expiration_date")
        return {"games": games, "played_games": user_played_games}


class EventPage(LoginRequiredMixin, ListView):
    context_object_name = 'data'
    model = Question
    template_name = 'event.html'

    @method_decorator(user_has_balance())
    @method_decorator(can_user_view())
    def get(self, *args, **kwargs):
        data = self.get_queryset()
        return render(self.request, self.template_name, {'data': data})

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = request.user
        event = get_event_by_short_name(kwargs['short_name'])
        print('Calling Save user answers')
        save_user_answers(user, data, event)
        print('called save user answers')
        update_bank(event)
        update_user_balance(user, event)
        return HttpResponseRedirect(reverse('quiz:games-page', kwargs={"category": event.question_category}))

    def get_queryset(self):
        short_name = self.kwargs['short_name']
        category = get_event_by_short_name(short_name=short_name).question_category
        answers = Answer.objects.filter(category=category)

        return {'questions': Question.objects.filter(category=category), 'answers': answers}


class Profile(LoginRequiredMixin, ListView):
    context_object_name = 'data'
    model = UserVote
    template_name = 'profile.html'

    def get_queryset(self):
        events_voted = get_user_votes(user=self.request.user)
        points = UserPoints.objects.filter(user=self.request.user)
        return {"events": events_voted, "points": points}


class Results(ListView):
    template_name = 'results.html'
    model = UserPoints
    context_object_name = 'data'

    def get_queryset(self):
        event = self.kwargs['short_name']
        data = UserPoints.objects.filter(event__short_name__iexact=event)
        return data


class Payments(TemplateView):
    template_name = 'payments.html'

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = self.request.user
        update_user_balance(user, amount=float(data.get('add_funds')))
        return HttpResponseRedirect(reverse('quiz:profile'))
