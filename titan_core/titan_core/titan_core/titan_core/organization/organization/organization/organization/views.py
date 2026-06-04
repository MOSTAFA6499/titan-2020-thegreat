from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import User, Team, Class, ClassRegistration

@login_required
def dashboard(request):
    context = {
        'user': request.user,
        'upcoming_classes': Class.objects.filter(
            participants__student=request.user, 
            start_time__gt=timezone.now()
        )[:5],
        'team_members': request.user.team.members.all() if request.user.team else [],
    }
    return render(request, 'organization/dashboard.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.phone = request.POST.get('phone', '')
        user.save()
        messages.success(request, 'اطلاعات شما به‌روزرسانی شد!')
        return redirect('profile')
    return render(request, 'organization/profile.html', {'user': request.user})

@login_required
def courses(request):
    return render(request, 'organization/courses.html', {'courses': []})
