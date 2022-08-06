from django import forms

class SearchForm(forms.Form):
	search = forms.CharField(required=False,widget= forms.TextInput(attrs={'value':'Search encyclopedia'}))


class CreatePage(forms.Form):
	
	title = forms.CharField(widget=forms.TextInput(attrs={}))
	article = forms.CharField(widget=forms.Textarea(attrs={'rows':'34'}))
	
class EditPage(forms.Form):
	
	pageEdit = forms.CharField(widget=forms.Textarea(attrs = {'rows':'30'}))
