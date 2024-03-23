from django.shortcuts import render, HttpResponse, redirect
from .models import dates,KissMessage,NudeImage
from datetime import datetime, timezone
import time
from django.contrib.auth import logout
from .forms import DatesForm,UpdateBothDatesForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def base(request):

    return render(request, "myapp/base.html", {"name" : "name"})

def home(request):
    date_obj = dates.objects.all()[0]
    datetime_obj = datetime.fromisoformat(str(date_obj))

    return render(request, "myapp/home.html",{"datetime" : str(datetime_obj)})


def kisses(request):

    return render(request, "myapp/kisses.html", {"name" : "name"})

def nudes(request):

    return render(request, "myapp/nudes.html", {"name" : "name"})

def date(request):
    date_obj = dates.objects.all()[1]
    datetime_obj = datetime.fromisoformat(str(date_obj))

    return render(request, "myapp/date.html", {"datetime" : str(datetime_obj)})

def custom_logout(request):
    logout(request)
    # Redirect to your desired page after logout
    return redirect('home')  # Replace 'home' with the name of the URL you want to redirect to

def updatedate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DatesForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success_page')  # Redirect as appropriate
        else:
            form = DatesForm()
        return render(request, 'myapp/updatedate.html', {'form': form})
    else:
        return redirect('login')  # Redirect to login

def update_last_date(request):
    if request.method == 'POST':
        form = DatesForm(request.POST)  # Instantiate form with POST data
        if form.is_valid():
            new_date = form.cleaned_data['date']  # Extract the validated date from the form
            first_date_obj = dates.objects.first()  # Get the first dates object

            if first_date_obj:
                first_date_obj.date = new_date  # Update the date field
                first_date_obj.save()  # Save the changes
            else:
                # If there are no date objects, create a new one
                dates.objects.create(date=new_date)

            return redirect('/')  # Redirect to a new URL
    else:
        form = DatesForm()  # An unbound form

    return render(request, 'your_template.html', {'form': form})
def update_next_date(request):
    if request.method == 'POST':
        form = DatesForm(request.POST)  # Instantiate form with POST data
        if form.is_valid():
            new_date = form.cleaned_data['date']  # Extract the validated date from the form
            second_date_obj = dates.objects.all().order_by('id')[1:2].first()  # This will get the second object or None if it doesn't exist


            if second_date_obj:
                second_date_obj.date = new_date  # Update the date field
                second_date_obj.save()  # Save the changes
            else:
                # If there are no date objects, create a new one
                dates.objects.create(date=new_date)

            return redirect('/')  # Redirect to a new URL
    else:
        form = DatesForm()  # An unbound form

def update_both(request):
    if request.method == 'POST':
        form = UpdateBothDatesForm(request.POST)
        if form.is_valid():
            first_new_date = form.cleaned_data['first_date']
            second_new_date = form.cleaned_data['second_date']

            # Update the first date object
            first_date_obj = dates.objects.all().order_by('id').first()
            if first_date_obj:
                first_date_obj.date = first_new_date
                first_date_obj.save()
            else:
                dates.objects.create(date=first_new_date)

            # Update the second date object
            second_date_obj = dates.objects.all().order_by('id')[1:2].first()
            if second_date_obj:
                second_date_obj.date = second_new_date
                second_date_obj.save()
            else:
                dates.objects.create(date=second_new_date)

            return redirect('/')  # Redirect to home or a confirmation page
    else:
        form = UpdateBothDatesForm()  # Instantiate an empty form for GET requests

    return render(request, '/', {'form': form})

def update_dates(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DatesForm(request.POST)
            if form.is_valid():
                new_date = form.cleaned_data['date']
                
                action = request.POST.get('action')
                
                if action == 'update_next':
                    # Update the second date object
                    second_date_obj = dates.objects.all().order_by('id')[1:2].first()
                    if second_date_obj:
                        second_date_obj.date = new_date
                        second_date_obj.save()
                    else:
                        dates.objects.create(date=new_date)
                        
                elif action == 'update_last':
                    # Update the first date object
                    first_date_obj = dates.objects.first()
                    if first_date_obj:
                        first_date_obj.date = new_date
                        first_date_obj.save()
                    else:
                        dates.objects.create(date=new_date)
                
                elif action == 'update_both':
                    # Update both dates, starting with the first
                    first_date_obj = dates.objects.first()
                    if first_date_obj:
                        first_date_obj.date = new_date
                        first_date_obj.save()
                    else:
                        dates.objects.create(date=new_date)
                    
                    # Now update the second, ensuring it's a different object
                    second_date_obj = dates.objects.all().order_by('id')[1:2].first()
                    if second_date_obj and second_date_obj != first_date_obj:
                        second_date_obj.date = new_date
                        second_date_obj.save()
                    elif not second_date_obj:
                        dates.objects.create(date=new_date)

                return redirect('/')  # Redirect to a new URL or success page
        else:
            form = DatesForm()  # An unbound form for GET requests
        return render(request, 'myapp/updatedate.html', {'form': form})
    else:
        return redirect('login')  # Redirect to login
    
def send_kiss(request):
    if request.method == 'POST':
        message_content = request.POST.get('message', '').strip()
        if message_content:
            # Save the kiss message to the database
            KissMessage.objects.create(user=request.user, message=message_content)
            # Optionally, you can use Django's messaging framework to provide feedback to the user
            # from django.contrib import messages
            # messages.success(request, 'Your kiss was sent successfully!')

        return redirect('kiss_send')  # Redirect to the home page or any other page you prefer
    else:
        # Redirect to home if the method is not POST or the form is not valid
        return redirect('home')
    
def kiss_send(request):
    return render(request, "myapp/kiss_send.html", {"name" : "name"})

def send_nude(request):
    if request.method == 'POST' and request.FILES.get('nude_image'):
        nude_image = request.FILES['nude_image']
        # Save the image to your model
        NudeImage.objects.create(user=request.user, image=nude_image)
        # Redirect to a new URL or a success page
        return redirect('nude_sent')
    return redirect('home')

def nude_sent(request):
    return render(request, "myapp/nude_sent.html", {"name" : "name"})

def is_admin(user):
    return user.is_authenticated and user.is_staff

@login_required
@user_passes_test(is_admin)
def view_kiss_images(request):
    images = NudeImage.objects.all()
    return render(request, 'myapp/view_nudes.html', {'images': images})

@login_required
@user_passes_test(is_admin)
def view_kiss_messages(request):
    messages = KissMessage.objects.all()
    return render(request, 'myapp/view_kiss_messages.html', {'messages': messages})