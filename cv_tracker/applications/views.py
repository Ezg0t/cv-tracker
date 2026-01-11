from django.shortcuts import render, redirect, get_object_or_404
from .models import JobApplication

STATUS_SEQUENCE = ['sent', 'review', 'interview', 'offer', 'rejected']

def change_status(request, pk):
    app = get_object_or_404(JobApplication, pk=pk)
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(JobApplication.STATUS_CHOICES):
            app.status = new_status
            app.save()
    return redirect('applications:list')

def delete_application(request, pk):
    app = get_object_or_404(JobApplication, pk=pk)
    app.delete()
    return redirect('applications:list')

def application_list(request):
    apps = JobApplication.objects.select_related('user').prefetch_related('history')
    return render(request, 'applications/list.html', {'apps': apps})
