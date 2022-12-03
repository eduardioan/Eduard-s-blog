
from django.shortcuts import render

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
      else:
        instance.save()
        print("mail adaugat")
    return render(request, "newsletter/subscription_done.html")
  else:
    form = NewsUserForm()

  # ---- start send email ----
  # newUsers = NewsUsers.objects.all()
  # for newUser in newUsers:
  #   email = newUser.email
  #   send_mail(
  #     subject="Test 1",
  #     message="Hey, a aparut un post nou!",
  #     from_email=settings.EMAIL_HOST_USER,
  #     recipient_list=[email]
  #   )
  # ---------------------------

  context = {'form': form}
  template = "newsletter/subscribe.html"
  return render(request, template, context)

def show_subscription(request):
  return render(request, "newsletter/subscription_done.html")

# for user in NewsUsers.objects.all():
#     send_mail(subject, message, from_email,
#         user.Email)

# subject = 'Bun venit la blogul meu'
# message = f'Salut {NewsUsers.name}, v-ati inregistrat cu succes.'
# email_from = settings.EMAIL_HOST_USER
# recipient_list = [NewsUsers.email, ]
# send_mail( subject, message, email_from, recipient_list )
