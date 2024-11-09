
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .models import UserProfile

@login_required
def admin_view(request):
    
    if request.user.userprofile.role != 'Admin':
        return HttpResponseForbidden("You are not authorized to view this page.")
    
 
    return render(request, 'admin_view.html')
