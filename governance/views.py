from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DataResource, AccessLog

# Dashboard
@login_required
def dashboard(request):
    resources = DataResource.objects.all()
    return render(request, 'dashboard.html', {'resources': resources})


# Access resource + log it
@login_required
def access_resource(request, id):
    resource = DataResource.objects.get(id=id)

    # Log access
    AccessLog.objects.create(
        user=request.user,
        resource=resource
    )
from .models import AccessLog

def logs(request):
    logs = AccessLog.objects.all().order_by('-access_time')
    return render(request, 'logs.html', {'logs': logs})
    return render(request, 'resource.html', {'resource': resource})