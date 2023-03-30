from django import forms

LISTA_CURSOS=(
    ("Python","Python"),
    ("Django","Django"),
    ("PHP","PHP"),
    ("SqlServer","SqlServer"),
    ("Oracle","Oracle"),
    ("JavaScript","JavaScript"),
)

# clase para definir datos del alumno
class Alumno(forms.Form):
    #definir los datos del alumno
    codigo=forms.CharField()
    nombre=forms.CharField()
    curso=forms.ChoiceField(choices=LISTA_CURSOS)
    parcial=forms.IntegerField()
    final=forms.IntegerField()
    practica=forms.IntegerField()
    
    