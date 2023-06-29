from django.shortcuts import render
from django.http import JsonResponse
from contact.models import Message


# Create your views here.

def contact(request):
    return render(request, 'contact.html')


def contact_form(request):
    if request.POST:
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

        success = True
        message = 'Contact form sent successfully.'
    else:
        success = False
        message = 'Request method is not a valid'
    context = {
        'success': success,
        'message': message,
    }
    return JsonResponse(context)
