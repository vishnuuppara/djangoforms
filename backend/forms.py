from django import forms

class Feedback(forms.Form):
    Tittle=forms.CharField(label= 'Tittle', max_length=50,widget= forms.TextInput(attrs={'class':'form-control'}))
    subject=forms.CharField(label= 'subject discription', max_length=200,widget= forms.Textarea(attrs={'class':'form-control'}))
    email=forms.CharField(label= 'email', min_length=1,widget= forms.TextInput(attrs={'class':'form-control'}))