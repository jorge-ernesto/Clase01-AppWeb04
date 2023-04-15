from django import forms

# Se puede usar tuplas o listas
LISTA_CURSOS = (
    ("Python", "Python"),
    ("Django", "Django"),
    ("PHP", "PHP"),
    ("SqlServer", "SqlServer"),
    ("Oracle", "Oracle"),
    ("JavaScript", "JavaScript"),
)

class Alumno(forms.Form):
    # Definir los datos de la clase (inputs del formulario)
    # Si no se especifica lo contrario, todos los inputs seran required=TRUE por defecto
    codigo = forms.CharField()
    nombre = forms.CharField()
    curso = forms.ChoiceField(choices=LISTA_CURSOS)
    parcial = forms.IntegerField()
    final = forms.IntegerField()
    practica = forms.IntegerField()
