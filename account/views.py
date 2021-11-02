from django.shortcuts import render, redirect
from django.views import View
import json
from django.http import JsonResponse
# from validate_email import validate_email
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
# from .utils import account_activation_token
from django.urls import reverse
from django.contrib.auth import authenticate, get_user_model, login, logout
from .utils import EmailUtil, account_activation_token


def registration(request):
    return render(request, 'account/registration.html')


class RegistrationView(View):
    def get(self, request):
        return render(request, 'account/registration.html')

    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        print(email)
        print(password)

        context = {
            'email': email
        }

        if not get_user_model().objects.filter(email=email).exists():
            if len(password) < 7:
                messages.error(request, 'パスワードを７字以上にしてください')
                return render(request,  'account/registration.html', context)
            user = get_user_model().objects.create_user(email=email, password=password)
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            link = reverse('account:activate', kwargs={
                'uidb64': uid,
                'token': token
            })

            activate_url = 'http://' + current_site.domain + link
            email_body = user.email + \
                'さん、ご登録ありがとうございます。\nメールアドレスに間違いがなければ、以下のリンクからログインしてください。 \n' + activate_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'ユーザー登録を完了してください'}
            EmailUtil.send_email(data)
            messages.success(request, '確認メールを送信しました')
            return render(request, 'account/registration.html')
        print('############')
        messages.error(request, '既にアカウントが存在します')
        return render(request, 'account/registration.html', context)


class VerificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=id)

            if not account_activation_token.check_token(user, token):
                redirect('/login')

            if user.is_verified:
                return redirect('/login')

            user.is_verified = True
            user.save()

            messages.success(request, 'アカウント作成が完了しました')
            return redirect('/login')
        except Exception as e:
            print(e)

        print("AAAAAAAAAAA")
        return redirect('/login')


class LoginView(View):
    def get(self, request):
        return render(request, 'account/login.html')

    def post(self, request):
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        context = {
            'email': request.POST.get('email', None)
        }

        if password:
            user = authenticate(email=email, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    # messages.success(request, 'Welcome!!')
                    return redirect('/quizes')
                messages.error(request, 'ユーザー登録が完了していません\nメールを確認してください')
                return render(request, 'account/login.html')

            messages.error(request, 'メールアドレスもしくは、パスワードが間違っています')
            return render(request, 'account/login.html', context)
        messages.error(request, 'すべての項目を入力してください')
        return render(request, 'account/login.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'ログアウトが完了しました')
        return redirect('/login')
