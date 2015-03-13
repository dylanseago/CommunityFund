from django import forms
from communityfund.widgets import BSDecimalInput
from communityfund.apps.home.models import Funding


class CreateCommunityForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class FundingForm(forms.ModelForm):
    amount = forms.DecimalField(widget=BSDecimalInput("Amount", prepended='$', appended='.00', hide_label=True),
                                min_value=1, decimal_places=0)

    class Meta:
        model = Funding
        fields = ('amount',)

    def __init__(self, user, project, *args, **kwargs):
        self.user = user
        self.project = project
        super(FundingForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        funding = super(FundingForm, self).save(commit=False)
        funding.user = self.user
        funding.project = self.project
        # Check if the user has previously funded this project. If so, update the previous one
        try:
            previous_funding = Funding.objects.get(user=self.user, project=self.project)
            previous_funding.amount += funding.amount
            previous_funding.save()
            return previous_funding
        except Funding.DoesNotExist:
            if commit:
                funding.save()
            return funding

