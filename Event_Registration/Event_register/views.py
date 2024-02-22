import uuid
from django.shortcuts import render, redirect
from .models import Registration



def registration_form(request):
    return render(request, 'registration_form.html')

def register(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone']
        event_sessions = ', '.join(request.POST.getlist('event_sessions'))

        # Generate a UUID for registration ID
        registration_id = uuid.uuid4()

        # Save registration details
        registration = Registration.objects.create(full_name=full_name, email=email, 
                                                    phone_number=phone_number, 
                                                    event_sessions=event_sessions, 
                                                    registration_id=registration_id)
        # Optionally, send confirmation email here

        return render(request, 'confirmation.html', {'registration': registration})
    else:
        return redirect('registration_form')
