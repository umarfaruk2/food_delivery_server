from django.core.mail import EmailMessage
from decouple import config

class Util:
  @staticmethod
  def send_email(data):
    email = EmailMessage(
      subject=data['subject'],
      body=data['body'],
      from_email= config('EMAIL_FROM'),
      to=[data['to_email']]
    )
    email.send()