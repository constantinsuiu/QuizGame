from game.models import Game, UserPoints


def draw_prize(event):
    max_points = UserPoints.objects.filter(event=event).order_by('-points').first()
    winners = UserPoints.objects.filter(points=max_points.points)
    game = Game.objects.get(event=event)
    prize = (game.bank * 0.9) / winners.count()
    for winner in winners:
        winner.user.balance += prize
