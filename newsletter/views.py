from django.contrib import messages
from django.shortcuts import render

from Blog.views import CreatePostView
from newsletter import forms
from newsletter.forms import NewsUserForm
from newsletter.models import NewsUsers
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail


def newsletter_subscribe(request):
    global instance
    if request.method == 'POST':
        form = NewsUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            if NewsUsers.objects.filter(email=instance.email).exists():
                print('Aceasta adresa de email exista deja')
                return render(request, "newsletter/subscribe.html")
            else:

                # daca e spatiu gol, nu trimite mail
                instance.save()
                print("mail adaugat")
                newUsers = NewsUsers.objects.all()
                print(newUsers)
                firstUser = newUsers[0]
                print(firstUser)
                lastUser = newUsers[len(newUsers) - 1]
                print(lastUser)
                email = lastUser.email

                send_mail(
                    subject="Test 1",
                    message="Hey, te-ai inregistrat!",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[email]
                )

        return render(request, "newsletter/subscribe.html")
    else:
        form = NewsUserForm()

    context = {'form': form}
    template = "newsletter/subscribe.html"
    return render(request, template, context)


def show_subscription(request):
    return render(request, "newsletter/subscription_done.html")

# def new_post_newsletter(request):
#      if request.method == 'POST':
#         form = NewsUserForm(request.POST)
#         if 'newsletter_sub' in request.POST:
#              newUsers = NewsUsers.objects.all()
#              print(newUsers)
#               for newUser in newUsers:
#                 email = newUser.email
#                 send_mail(
#                   subject="Test 1",
#                   message="Hey, am postat ceva nou",
#                   from_email=settings.EMAIL_HOST_USER,
#                   recipient_list=[email]
#                 )
#
#     context = {'form': form}
#     template = "newsletter/subscribe.html"
#     return render(request, template, context)
