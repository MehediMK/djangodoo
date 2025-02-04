import subprocess
from django.shortcuts import render
from django.http import HttpResponse
from djangodoo.utils import utils


def get_app_list(request):
    """Display a list of installed and uninstall apps."""
    context = {}
    install_apps = utils.get_install_apps_info()
    uninstall_apps = utils.get_uninstall_apps_info()
    context["apps"] = install_apps + uninstall_apps
    return render(request, 'djangodoo/apps_list.html', context)
