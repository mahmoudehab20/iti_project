from django import forms
from Admin.models import books


class booksModelForm(forms.ModelForm):
    class Meta:
        model = books
        fields= '__all__'


    def clean_title(self):
        title = self.cleaned_data['title']
        if books.objects.filter(title=title).exists():
            raise forms.ValidationError("This title already exists")

        return title
    

