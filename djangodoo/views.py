from django.shortcuts import render
from djangodoo.utils.utils import utils


def get_app_list(request):
    context = {}
    context["apps"] = utils.apps_name_description_icon_version()
    return render(request, 'djangodoo/apps_list.html', context)
