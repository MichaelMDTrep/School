from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib import messages
import urllib

@login_required
def contact_view(request):

    def decode(raw_text):
        return urllib.parse.unquote(raw_text, encoding='utf-8', errors='replace').replace("+", " ")

    if request.method == "POST":
        data = request.body.decode().split("=")
        name = decode(data[2].split('&')[0])
        email = decode(data[3].split('&')[0])
        subject = decode(data[4].split('&')[0])
        message = decode(data[5].split('&')[0])

        contact_notification_message = render_to_string(
            'contact/emails/contact_email.txt', {
                'name': name,
                'email': email,
                'subject': subject,
                'message': message,
            }
        )

        contact_notification_message_wrapper = EmailMessage(
            f'Hey Terri! {name} is trying to contact you from Resiliency Zone',
            contact_notification_message,
            to=[settings.DEFAULT_FROM_EMAIL]
        )

        contact_notification_message_wrapper.send()
        
        messages.success(request, 'Message sent!')
        return redirect('contact')

    context = {
        'page': 'contact',
        'title': 'Contact',
    }

    return render(request, 'contact/contact.html', context)

