from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Invite
from django.contrib import messages
import urllib
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings

# Create your views here.

@login_required
def invite(request):

    if request.user.is_superuser:

        def decode(raw_text):
            return urllib.parse.unquote(raw_text, encoding='utf-8', errors='replace').replace("+", " ")

        if request.method == "POST":
            data = request.body.decode().split("=")
            email = decode(data[2].split('&')[0])

            invite_same_email = Invite.objects.filter(email=email)

            if invite_same_email:
                messages.info(request, 'You already sent an invitation to this email.')
                return redirect('invite')
            else:
                invite = Invite(email=email)
                invite.save()

                invite_notification_message = render_to_string(
                    'invites/emails/invite.txt', {
                        'code': invite.code,
                    }
                )

                invite_notification_message_wrapper = EmailMessage(
                    f'Resiliency Zone Invitation - {invite.code}',
                    invite_notification_message,
                    to=[email]
                )

                invite_notification_message_wrapper.send()
                
                messages.success(request, 'Invitation sent!')
                return redirect('invite')

        context = {
            'page': 'invite',
            'title': 'Invite',
        }

        return render(request, 'invites/invite.html', context)
    
    else:
        messages.warning(request, 'You are not authorized to manage invitations.')
        return redirect('home')