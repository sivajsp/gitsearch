from django import forms
class get_city(forms.Form):
    city = forms.CharField(max_length = 20,
    widget = forms.TextInput(attrs={"placeholder":"Enter the city..."}))
