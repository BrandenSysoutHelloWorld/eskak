# DEFINE IMPORTS
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Entry

# START OF FILE: [eskak]: 'views.py'

# LANDING VIEW
def landing_view(request):
    return render(request, 'landing.html')

# ENTRY CREATE VIEW
def new_entry_view(request):
    return render(request, 'newEntry.html')

# ENTRY CREATE FUNCTION
def new_entry_create(request):
    # Fetch Entry Details
    date = request.POST['entryDate']
    time = request.POST['entryTime']
    units = request.POST['entryUnits']

    try:
        new_entry = Entry(date=date, time=time, units=units, username=request.user.username)  

        new_entry.save()

        message = 'SUCCESSFULLY ADDED NEW ENTRY TO DATABASE!'

        print(message)

        return HttpResponseRedirect(reverse('eskak:previous_entry_view') + f'?message=SUCCESSFULLY ADDED NEW ENTRY TO DATABASE')
    
    except Exception as ex:            
        # Get the Error Message
        error_message = str(ex)
        # Redirect back to new_entry_view with the error message
        return HttpResponseRedirect(reverse('eskak:new_entry_view') + f'?error_message={error_message}')

# PREVIOUS ENTRIES VIEW
def previous_entry_view(request):
    message = request.GET.get('message', '')
    entries = Entry.objects.all()  # Retrieve all Entry objects

    show_entries = []

    for entry in entries:
        if entry.username == request.user.username:
            show_entries.append(entry)    
    return render(request, 'previousEntry.html', {'entries': show_entries, 'message': message})

# DELETE A ENTRY
def delete_entry(request, entry_id):
    entries = Entry.objects.all()  # Retrieve all Entry objects

    for entry in entries:
        if entry_id == entry.id:
            entry.delete()

    return HttpResponseRedirect(reverse('eskak:previous_entry_view') + f'?message=SUCCESSFULLY REMOVED NEW ENTRY TO DATABASE')     

'''
Made with ❤️
------------
BRANDEN VAN STADEN -
    All rights reserved | September 2023
-------------------------------------
'''