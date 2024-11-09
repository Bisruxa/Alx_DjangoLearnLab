# views/librarian_view.py
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def librarian_view(request):
    # Check if the logged-in user has the 'Librarian' role
    if request.user.userprofile.role != 'Librarian':
        return HttpResponseForbidden("You are not authorized to view this page.")
    
    # If the user is a Librarian, render the librarian page
    return render(request, 'librarian_view.html')
