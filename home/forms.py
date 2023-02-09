from django.forms import ModelForm
from .models import Contatos
from django.core.mail import EmailMessage
import requests


class FormContatos(ModelForm):
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
        nome_contato = self.cleaned_data['nome_contato']
        email_contato = self.cleaned_data['email_contato']
        telefone_contato = self.cleaned_data['telefone_contato']
        mensagem_contato =  self.cleaned_data['mensagem_contato']

        corpo = f'Nome:{nome_contato}\nTelefone:{telefone_contato}\nMensagem:{mensagem_contato}'

        mail = EmailMessage(
            subject='Escola de Música IBNA',
            from_email='mauricioaraujoguitar@gmail.com',
            to=[email_contato,],
            body=corpo,
            headers={
                'Replay-To': 'mauricioaraujoguitar@gmail.com'
            }
        )

        if len(nome_contato) < 5:
            self.add_error(
                'nome_contato',
                'Nome precisa ter mais que 5 caracteres.'
            )

        mail.send()

    class Meta:
        model = Contatos
        fields = ('nome_contato', 'email_contato', 'telefone_contato','mensagem_contato')