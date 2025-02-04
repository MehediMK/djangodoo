from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command
from django.core.management.base import CommandError
from djangodoo.utils import utils


def get_app_list(request):
    """Display a list of installed and uninstall apps."""
    context = {}
    install_apps = utils.get_install_apps_info()
    uninstall_apps = utils.get_uninstall_apps_info()
    context["apps"] = install_apps + uninstall_apps
    return render(request, 'djangodoo/apps_list.html', context)


def create_app(request):
    app_name = request.GET.get("app_name")
    # Validate app_name to prevent security issues
    if not app_name:
        return HttpResponse("Invalid app name.", status=400)
    try:
        # Run Django's startapp command to create the app
        call_command('startapp', app_name)
        return HttpResponse(f"App '{app_name}' created successfully!")
    except CommandError as e:
        return HttpResponse("Error creating app.", status=500)
