from django import forms

from django.forms import SelectMultiple, TextInput, Textarea, Widget

from courses.models import Course

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(label="Kurs Başlığı", required=True, min_length=10, max_length=50, 
#     error_messages={"required":
#                     "Kus başlığı girmelisiniz.",
#                     "max_lenght":"Başlık 10-50 karakter arasında olmalıdır.",
#                     "min_lenght":"Başlık 10-50 karakter arasında olmalıdır."}, 
#                 widget=forms.TextInput(attrs={"class":"form-control"}))
    
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}), max_length=100, min_length=10,
#     error_messages={"max_lenght":"Başlık 10-100 karakter arasında olmalıdır.",
#                     "min_lenght":"Başlık 10-100 karakter arasında olmalıdır."}
#                     )
    
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"})) 

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug')
        labels = {
            'title':'Kurs Başlığı',
            'description':'Kurs Açıklaması',   
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"})
        }
        error_messages = {
            "title": {
                "required":"Kurs başlığı girmelisiniz!",
                "max_lenght":"En fazla 50 karakter girebilirsiniz!"
            },
            "description":{
                "required":"Açıklama girmelisiniz!"
            }
        }





class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title', 'description', 'image', 'slug', 'categories', 'isActive')
        labels = {
            'title':'Kurs Başlığı',
            'description':'Kurs Açıklaması',   
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
            "categories": SelectMultiple(attrs={"class":"form-control"})
        }
        error_messages = {
            "title": {
                "required":"Kurs başlığı girmelisiniz!",
                "max_lenght":"En fazla 50 karakter girebilirsiniz!"
            },
            "description":{
                "required":"Açıklama girmelisiniz!"
            }
        }





class UploadForm(forms.Form):
    image = forms.ImageField()