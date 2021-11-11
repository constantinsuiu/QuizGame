from django.db import models
from game.models import Game, Question, Answer


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Results(BaseModel):
    event = models.ForeignKey(Game, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct_answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Results'

    def __str__(self):
        return '{} - {} - {}'.format(self.event.short_name.capitalize(), self.question, self.correct_answer)


class Finances(BaseModel):
    event = models.ForeignKey(Game, on_delete=models.CASCADE)
    profit = models.FloatField(default=0.00)

    class Meta:
        verbose_name_plural = "Finances"

    def __str__(self):
        return self.event.short_name
