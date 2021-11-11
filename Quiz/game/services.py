from .models import Question, Answer, UserVote
from results.models import Finances
import math


def save_user_answers(user, data, event):
    questions = Question.objects.filter(category=event.question_category)

    for question in questions:
        print(question.question_text)
        if data.get(question.question_text):
            print(data.get(question.question_text))
            answer = Answer.objects.get(answer_text__iexact=data.get(question.question_text))
            vote, created = UserVote.objects.get_or_create(user=user, event=event, question=question, answer=answer)
            if not created:
                vote.save()


def update_user_balance(user, event=None, amount=0):
    if event:
        user.balance -= event.price
    if amount:
        user.balance += amount
    user.save()


def update_bank(event):
    commission, prize = math.modf(event.price)
    event.bank += int(prize)
    event.save()
    game, create = Finances.objects.get_or_create(event=event)
    game.profit += commission
    game.save()
