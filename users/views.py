# DEFINE IMPORTS
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User


# START OF FILE: [users]: 'views.py'

# [GET] > userLogin
def login_view(request):
    # Extract the message(if any)
    message = request.GET.get('message', '')
    # Check if user is authenticated
    if request.user.is_authenticated:
        # Redirect to profile using 'reverse'
        return HttpResponseRedirect(reverse('users:profile_view'))
    # Else function will returned login webpage(render)
    return render(request, 'userLogin.html', {'message': message})

# [POST] < userLogin
def login_user(request):
    username = request.POST['username']
    password = request.POST['password']    
    # Authorize user
    user = authenticate(username=username, password=password)
    # User is NOT Authenticated
    if user is None:
        # Update result parameter to pass to view
        error_message = "Invalid Username or Password!"
        # Construct reverse URL for Http Response Redirect
        return render(request, 'userLogin.html', {'error_message': error_message})
    else:
        # Login user 
        login(request, user)
        return HttpResponseRedirect(reverse('users:profile_view'))

# [GET] > userRegister 
def register_view(request):
    # Check if user is authenticated
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('users:logout_view') + '?error_message=You must be logged out in to register a new user.')
    return render(request, 'userRegister.html')

# [POST] > userRegister 
def register_user(request):
    raiseFlag = False

    while raiseFlag == False:
        if request.method == 'POST':
            # Fetch data from form
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
        
        # Check if both password match
        if password != confirm_password:
            return HttpResponseRedirect(reverse('users:register_view') + f'?error_message=Make sure your password match!')
                
        try:
            # Create a New User instance and Set Attributes
            new_user = User.objects.create_user(username=username, password=password)
            # Set Firstname
            new_user.email = email
            # Set Is? - Staff
            new_user.is_staff = False
            # Set Is? - Superuser
            new_user.is_superuser = False
            # Save User to Database
            new_user.save()
            print("Successfully Added New User to Database")
            print(f"USERNAME - {username}\nPassword(op-sec) - {password}\nEmail - {email}")
            # Redirect User to Profile
            return HttpResponseRedirect(reverse('users:login_view'))   
        # Catch the exception
        except Exception as ex:            
            # Get the Error Message
            error_message = str(ex)
            # Redirect back to register with the error message
            return HttpResponseRedirect(reverse('users:register_view') + f'?error_message={error_message}')
        
# [GET] > userProfile
def profile_view(request):
    return render(request, 'userProfile.html')

# [GET] > userLogout & [POST] < userLogout
def logout_view(request):
#    if request.method == 'POST':
#        return HttpResponseRedirect(reverse('users:logout_user'))
#     # Extract the message from the query parameter
#    error_message = request.GET.get('error_message', '')    
#    # Pass the message to the template
    logout(request)
    return redirect(reverse('users:login_view'))
 

'''CODE IMPLEMENTED & CONTRIBUTED BY: BRANDEN VAN STADEN'''
