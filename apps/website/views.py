from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apps.funcionario.models import Funcionario


@login_required
def home(request):
    data = {}
    data['usuario'] = request.user
    return render(request, 'website/index.html', data)
