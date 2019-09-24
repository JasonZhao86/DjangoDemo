from django import forms
from django.forms import ModelForm, ValidationError
from .models import Author2, Book2, Publisher
from django.utils.translation import gettext_lazy as _

# class PubliserForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     address = forms.CharField(max_length=50)
#     city = forms.CharField(max_length=60)
#     state_province = forms.CharField(max_length=30)
#     country = forms.CharField(max_length=20)
#     website = forms.CharField(max_length=50)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class PubliserForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ("name", "address", "city", "state_province", "country", "website")
        # fields = "__all__"
        # exclude = ("state_province", "country")
        # labels = {
        #     "name": "出版社名",
        #     "address": "地址",
        #     "city": "城市",
        #     "state_province": "省份",
        #     "country": "国家",
        #     "website": "网址",
        # }
        widgets = {
            "address": forms.Textarea(attrs={'cols': 80, 'rows': 5})
        }
        help_texts = {
            "name": _("Some useful help text.")
        }
        error_messages = {
            'name': {
                "max_length": _("This writer's name is too long."),
            }
        }

class AuthorForm(ModelForm):
    class Meta:
        model = Author2
        fields = ("name", "title", "birth_day")

    # def clean_name_field(self):
    #     cleaned_data = self.cleaned_data["name"]
    #     if len(cleaned_data) > 30:
    #         raise ValidationError("Name must less than 30")
    #     return cleaned_data

    # def clean(self):
    #     cleaned_data = super(AuthorForm, self).clean()
    #     name = cleaned_data.get("name")
    #     title = cleaned_data.get("title")
    #     if len(name) < 30 and title == "MR":
    #         raise ValidationError("xxxxxx")
    #     return cleaned_data

class BookForm(ModelForm):
    class Meta:
        model = Book2
        fields = ["name", "authors"]

# TITLE_CHOICES = (
#     ('MR', 'Mr.'),
#     ('MRS', 'Mrs.'),
#     ('MS', 'Ms.'),
# )
#
# class AuthorForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     title = forms.CharField(max_length=3, widget=forms.Select(choices=TITLE_CHOICES))
#     birth_day = forms.DateField(required=False)
#
# class BookForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     authors = forms.MultipleChoiceField(queryset=Author2.objects.all())
