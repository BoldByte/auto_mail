from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Investor
from .forms import InvestorForm
from django.http import JsonResponse, HttpResponseRedirect
from mail import EmailSender  # Import your mail.py script functions
from ai_form import create_mail
from .forms import EmailForm
import re

def change(text, name= 'investor'):
    # Regular expression pattern
    pattern = r'dear\s+[^,]+,'

    # Replace matched patterns using re.sub()
    modified_text = re.sub(pattern, f'dear {name},', text, flags=re.IGNORECASE)

    return modified_text

def investor_list(request):
    investors = Investor.objects.all()
    return render(request, 'investor.html', {'investors': investors})

def mail(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            recipient_list = [email.strip() for email in to_email.split(',')]
            subject = form.cleaned_data['subject']
            new_sub = [subject] * len(recipient_list)
            message = form.cleaned_data['message']
            new_mess = [change(message) for i in range(len(recipient_list))]
            # print(new_mess)
            attachment = request.FILES.getlist('attachment')
            if not attachment: attachment = ''

            # Use your mail.py script to send the email
            EmailSender().send_email(recipient_list, new_sub, new_mess, attachment)

            return redirect('investor_list')
        else:
            selected_investors_ids = request.POST.getlist('selected_investors')
            selected_investors = Investor.objects.filter(id__in=selected_investors_ids)
            mail = create_mail('make a resevation with an email')
            form = EmailForm()
            return render(request, 'mail.html', {'selected_investors': selected_investors, 'form': form, 'mail': mail})
    else:
        return redirect('investor_list')

def home(request):
    return render(request, 'index.html')

def add_investor(request):
    if request.method == 'POST':
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investor_list')
    else:
        form = InvestorForm()
    
    return render(request, 'add_investor.html', {'form': form})
