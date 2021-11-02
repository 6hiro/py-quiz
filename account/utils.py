from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

from django.core.mail import EmailMessage


class TokenGenerator(PasswordResetTokenGenerator):

    def _make_hash_value(self, user, timestamp):
        # return (user.is_active + user.pk + timestamp)
        return (text_type(user.is_active) + text_type(user.pk) + text_type(timestamp))


account_activation_token = TokenGenerator()


class EmailUtil:
    # インスタンス化せずに呼び出せる関数（第一引数にselfを受け取らない）
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'], body=data['email_body'], to=[data['to_email']])
        email.send()
