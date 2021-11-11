from .models import Game, UserVote


def get_top_5_events() -> [Game]:
    popular_events = Game.objects.all().order_by('-bank')
    top_games = [x for x in popular_events if x.is_active][0:5]
    return top_games


def get_soon_to_expire_events() -> [Game]:
    return [x for x in Game.objects.all().order_by('expiration_date') if x.is_active]


def get_event_by_short_name(short_name) -> Game:
    return Game.objects.get(short_name__iexact=short_name)


def get_user_votes(user):
    return UserVote.objects.filter(user=user)
