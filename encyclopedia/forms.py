from django import forms

# Class for edit form

class EditForm(forms.Form):
    form_title = forms.CharField()
    form_content = forms.CharField(widget=forms.Textarea)
