# views/member_view.py
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def member_view(request):
    # Check if the logged-in user has the 'Member' role
    if request.user.userprofile.role != 'Member':
        return HttpResponseForbidden("You are not authorized to view this page.")
    
    # If the user is a Member, render the member page
    return render(request, 'member_view.html')
