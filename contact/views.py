from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
def contactView(request):
    form = ContactForm()
    if request.method == 'POST':
        first_name          = request.POST['first_name']
        last_name           = request.POST['last_name']
        email               = request.POST['email']
        message             = request.POST['message']
        phone               = request.POST['phone']
        date                = request.POST['date']

        contact = Contact(first_name=first_name, last_name=last_name, email=email, phone=phone, message=message, date=date)
        contact.save()

        send_mail('ORDER EQUIRY',
            f'There has been an enquiry from {last_name}, {first_name}. \n Message: {message} \n Delivery date: {date} \n Phone: {phone}',
                email,
                    ['neupytechng@gmail.com'],
                        fail_silently=False)

        return redirect('contact:success')
    else:
        form = ContactForm()
    context = {
        'title': 'Contact Us',
        'form': form
        }
    return render(request, "contact/contact.html", context)


def successView(request):
    context = {
        'title': 'Success!',
    }
    return render(request, 'contact/success.html', context)

