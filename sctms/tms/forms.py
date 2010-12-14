from django import forms

from tms.models import Player, Replay, Tournament


class PlayerForm(forms.ModelForm):

    class Meta:
        model = Player
        exclude = 'user',


class ResultForm(forms.Form):
    player1_score = forms.ChoiceField()
    player2_score = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        match = kwargs.pop('match')
        super(ResultForm, self).__init__(*args, **kwargs)
        bo = match.round.bo
        double = lambda x: zip(x, x)
        choices = double(range(0, bo / 2 + 2))
        p1 = self.fields['player1_score']
        p2 = self.fields['player2_score']
        p1.choices = choices
        p2.choices = choices
        p1.label = match.player1
        p2.label = match.player2


class ReplayForm(forms.ModelForm):

    class Meta:
        model = Replay
        fields = 'file',


class TournamentForm(forms.ModelForm):

    class Meta:
        model = Tournament
