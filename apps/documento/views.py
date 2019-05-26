from django.views.generic import CreateView, UpdateView
from .models import Documento


class DocumentCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class DocumentUpdate(UpdateView):
    model = Documento
    fields = ['descricao', 'arquivo']
