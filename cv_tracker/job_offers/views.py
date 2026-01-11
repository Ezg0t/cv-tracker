from django.shortcuts import get_object_or_404, redirect, render
from .models import JobOffer
from applications.models import JobApplication

def job_offer_list(request):
    offers = JobOffer.objects.all().order_by('-created_at')
    return render(request, 'job_offers/list.html', {'offers': offers})

def change_status(request, pk):
    offer = get_object_or_404(JobOffer, pk=pk)
    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(JobOffer.STATUS_CHOICES):
            offer.status = new_status
            offer.save()
    return redirect('job_offers:list')

def add_application(request, pk):
    offer = get_object_or_404(JobOffer, pk=pk)
    if request.method == "POST":
        JobApplication.objects.create(
            company=offer.company_name,
            position=offer.title,
            status='sent'
        )
        offer.status = 'SENT'
        offer.save()
    return redirect('applications:list')