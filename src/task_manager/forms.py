from django import forms
from django.forms import  Textarea
from django.core.validators import MinValueValidator,MaxValueValidator
from  django.core.exceptions import ValidationError
from task_manager.models import Tasks,Comments, Attachments

def validate_max_count_split(value):
    if len(value.split()) > 4:
        raise ValidationError("%(value)s is too long. It must be less than 4 parts",
            params={"value": value},
        )


# class TaskForm(forms.Form):
#     name = forms.CharField(
#         label="наименование задачи",
#         max_length=100,
#         validators=[
#             validate_max_count_split,
#         ]
#     )
#     priority = forms.IntegerField(
#         label="приоритет",
#         validators=[
#             MinValueValidator(1),
#             MaxValueValidator(5),
#         ]
#     )
#     description = forms.CharField(
#         required=False,
#         label="Описание",
#         widget=forms.Textarea(
#             attrs={
#
#                 "class": "special"
#             }
#         )
#     )


class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ["name","priority","description","status"]
        widgets = {
            "description": Textarea(attrs={"cols": 50, "rows": 5}),
        }

    def clean(self):
        cleaned_data = super().clean()
        priority = cleaned_data.get("priority")
        description = cleaned_data.get("description")


        if priority >= 3 and not description:
            raise forms.ValidationError(
                "Высокий приоритет требует подробного описания задачи!"
            )
        return cleaned_data



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["message","user","task"]
        labels = {
            'message': 'Ваш комментарий',
            'user': 'Имя автора',
            'task': 'К какой задаче'
        }
        widgets = {
            "message": Textarea(attrs={"cols": 50, "rows": 5}),
            #"user": forms.TextInput(attrs={'class': 'form-control custom-input'})
        }

class AttachmentsForm(forms.ModelForm):
    class Meta:
        model = Attachments
        fields = ["name","photo","task","file" ]