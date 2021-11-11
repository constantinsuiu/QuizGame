from django import forms
from game.models import Game

CHOICES = (("Q", "Question"),
           ("C", "Complaint"),
           ("R", "New Request"))


class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'email@example.com'}))
    type = forms.ChoiceField(label ='Please choose a request type', choices=CHOICES)
    event = forms.ModelChoiceField(queryset=Game.objects.all().order_by('expiration_date'), required=False)
    text = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, request, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        if not request.user.is_anonymous:
            self.fields["email"].initial = request.user.email
        print(kwargs)
