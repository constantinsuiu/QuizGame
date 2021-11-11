from django.db import models
from game.models import Game


# Create your models here.
class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    slug = models.SlugField(max_length=5, unique=True)
    # uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=False)

    def __str__(self):
        return '{}'.format(self.question)


class ContactUs(models.Model):
    class Meta:
        verbose_name_plural = 'Contact Us'

    CHOICES = [
        ("Q", "Question"),
        ("C", "Complaint"),
    ]

    email = models.EmailField()
    type = models.CharField(choices=CHOICES, max_length=100)
    event = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    text = models.TextField()
    requested_at = models.DateTimeField(auto_now_add=True, editable=False)
    replied_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{} from {} user'.format(self.get_type_display(), self.email)
