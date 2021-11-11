from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Game, UserVote


def user_has_balance():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            user = request.user
            event = Game.objects.get(short_name=kwargs["short_name"])
            if user.balance < event.price and not user.is_staff:
                return redirect('quiz:payments')
            else:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator


def can_user_view():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            is_game_active = Game.objects.get(short_name=kwargs["short_name"]).is_active
            user_voted = UserVote.objects.filter(user=request.user).filter(event__short_name=kwargs["short_name"])\
                                 .count() > 0
            results_exist = Game.objects.filter(result_available=True).filter(short_name=kwargs["short_name"])\
                                .count() > 0
            if not is_game_active:
                return redirect('quiz:games-home')
            if user_voted and not results_exist:
                return redirect('quiz:profile', section='games')
            elif user_voted and results_exist:
                return redirect('quiz:results', kwargs=kwargs)
            else:
                return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
