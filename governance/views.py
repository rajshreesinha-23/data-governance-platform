from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import DataResource, AccessLog
from accounts.models import UserProfile

def get_role(user):
    profile = UserProfile.objects.filter(user=user).first()
    return profile.role if profile else 'user'

@login_required
def dashboard(request):
    role = get_role(request.user)
    total_resources = DataResource.objects.count()
    total_logs = AccessLog.objects.count()
    denied_count = AccessLog.objects.filter(status='denied').count()
    recent_logs = AccessLog.objects.order_by('-timestamp')[:5]
    return render(request, 'governance/dashboard.html', {
        'role': role,
        'total_resources': total_resources,
        'total_logs': total_logs,
        'denied_count': denied_count,
        'recent_logs': recent_logs,
    })

@login_required
def resources(request):
    role = get_role(request.user)
    all_resources = DataResource.objects.all()

    if request.method == 'POST':
        resource_id = request.POST.get('resource_id')
        resource = get_object_or_404(DataResource, id=resource_id)
        allowed = role in resource.get_allowed_roles()
        status = 'granted' if allowed else 'denied'
        reason = '' if allowed else f"Role '{role}' is not allowed to access this resource."
        AccessLog.objects.create(
            user=request.user,
            resource=resource,
            status=status,
            reason=reason
        )
        if allowed:
            messages.success(request, f"✅ Access GRANTED to '{resource.name}'")
        else:
            messages.error(request, f"❌ Access DENIED for '{resource.name}'. {reason}")
        return redirect('resources')

    return render(request, 'governance/resource.html', {
        'resources': all_resources,
        'role': role,
    })

@login_required
def logs(request):
    role = get_role(request.user)
    if role in ['admin', 'auditor']:
        all_logs = AccessLog.objects.order_by('-timestamp')
    else:
        all_logs = AccessLog.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'governance/logs.html', {
        'logs': all_logs,
        'role': role
    })

@login_required
def compliance(request):
    role = get_role(request.user)
    violations = AccessLog.objects.filter(status='denied').order_by('-timestamp')
    total = AccessLog.objects.count()
    denied = violations.count()
    granted = total - denied
    compliance_rate = round((granted / total) * 100, 1) if total > 0 else 100
    return render(request, 'governance/compliance.html', {
        'violations': violations,
        'compliance_rate': compliance_rate,
        'total': total,
        'denied': denied,
        'granted': granted,
        'role': role,
    })