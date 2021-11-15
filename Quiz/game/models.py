from datetime import datetime

import pytz
from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse

utc = pytz.UTC


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category


class Answer(models.Model):
    answer_text = models.CharField(max_length=500)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.answer_text


class Question(models.Model):
    category = models.ManyToManyField(Category)
    question_text = models.TextField()
    allow_multiple_answers = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text


class Game(BaseModel):
    event = models.CharField(max_length=200)
    expiration_date = models.DateTimeField()
    image = models.ImageField(
        upload_to="static/images", default="static/images/no-image.jpg"
    )
    result_available = models.BooleanField(default=False)
    short_name = models.CharField(max_length=100)
    question_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    price = models.FloatField(default=1.50)
    bank = models.IntegerField(default=0)

    @property
    def is_active(self):
        self.expired = True

        if self.expiration_date.replace(tzinfo=utc) < datetime.now().replace(
            tzinfo=utc
        ):
            self.expired = False

        return self.expired

    def get_absolute_url(self):
        return reverse(
            "quiz:event-page",
            kwargs={"category": self.question_category, "short_name": self.short_name},
        )

    def get_result_url(self):
        return reverse(
            "quiz:results",
            kwargs={"category": self.question_category, "short_name": self.short_name},
        )

    def __str__(self):
        return "{} event".format(self.event)


class UserVote(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    event = models.ForeignKey(Game, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    calculation_complete = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {} - {}".format(
            self.user, self.question, self.answer, self.event.short_name
        )


class UserPoints(BaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    event = models.ForeignKey(Game, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "User Points"

    def get_absolute_url(self):
        return reverse(
            "quiz:results",
            kwargs={"category": self.question_category, "short_name": self.short_name},
        )

    def __str__(self):
        return "{} - {} - {} points".format(
            self.user, self.event.short_name, self.points
        )
