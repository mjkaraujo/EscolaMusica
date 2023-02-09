from django.forms import ModelForm
from .models import ContatoCurso
from django.core.mail import EmailMessage
import requests


class FormCursos(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')
        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': '6LeSuY4hAAAAAE0DDl1JodoJub5sJeTSBsYIgVzq',
                'response': recaptcha_response
            }
        )

        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('success'):
            self.add_error(   
            'contatos',
            'Desculpe, ocorreu um erro!'
            )
    def send_mail(self):
        nome_curso = self.cleaned_data['nome_curso']
        email_curso = self.cleaned_data['email_curso']
        telefone_curso = self.cleaned_data['telefone_curso']
        mensagem_curso =  self.cleaned_data['mensagem_curso']

        corpo = f'Nome:{nome_curso}\nTelefone:{telefone_curso}\nMensagem:{mensagem_curso}'

        mail = EmailMessage(
            subject='Escola de Música IBNA',
            from_email='mauricioaraujoguitar@gmail.com',
            to=[email_curso,],
            body=corpo,
            headers={
                'Replay-To': 'mauricioaraujoguitar@gmail.com'
            }
        )

        if len(nome_curso) < 5:
            self.add_error(
                'nome_curso',
                'Nome precisa ter mais que 5 caracteres.'
            )

        mail.send()

    class Meta:
        model = ContatoCurso
        fields = ('nome_curso', 'email_curso', 'telefone_curso','mensagem_curso')