from django import forms
from .models import Curso, Aluno

# Formulário para Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso  # Aqui vamos dizer que o formulário vai usar o modelo Curso
        # Aqui vamos dizer quais campos do modelo Curso queremos usar no formulário
        fields = ['nome']

# Formulário para Aluno


class AlunoForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Aluno  # Aqui vamos dizer qual modelo esse formulário vai usar
        fields = ['nome', 'data_nascimento', 'cpf', 'genero',
                  'estado_civil', 'escolaridade', 'curso']
        # Aqui vamos dizer quais campos do modelo aluno queremos usar no formulário
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'maxlength': '14','class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'estado_civil': forms.Select(attrs={'class': 'form-control'}),
            'escolaridade': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
        }
