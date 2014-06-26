from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from main.models import Tenant


@login_required
def tenants(request):
    tenant_list = Tenant.objects.all().order_by('name')
    context = {'tenant_list': tenant_list}
    return render(request, 'main/tenants.html', context)


@login_required
def tenant_cashflows(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    context = {'cashflows': tenant.cashflows()}
    return render(request, 'main/cashflows.html', context)

@login_required
def tenant_reminders(request, tenant_id):
    tenant = get_object_or_404(Tenant, pk=tenant_id)
    context = {'reminders': []}
    return render(request, 'main/reminders.html', context)
