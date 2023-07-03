from django.shortcuts import render
from django.http import JsonResponse
from contact.models import Message
from contact.forms import ContactForm


# Create your views here.

def contact(request):
    contact_form = ContactForm()
    context = {
        'contact_form': contact_form,
    }
    return render(request, 'contact.html', context=context)


def contact_form(request):
    if request.POST:
        contact_form = ContactForm(request.POST or None)
        if contact_form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            message = request.POST.get('message')
            subject = request.POST.get('subject')

            Message.objects.create(
                name=name,
                email=email,
                message=message,
                subject=subject
            )
            # mail to send
            contact_form.send_email()

            success = True
            message = 'Contact form sent successfully.'
        else:
            success = False
            message = 'Request method is not a valid'
    else:
        success = False
        message = 'Request method is not a valid'
    context = {
        'success': success,
        'message': message,
    }
    return JsonResponse(context)
