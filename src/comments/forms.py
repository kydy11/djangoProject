from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(max_length = 10000000000000000000, widget=forms.Textarea)
    name = forms.CharField(max_length =40)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")
        if "h" in name.lower():
            raise forms.ValidationError("don't use h")