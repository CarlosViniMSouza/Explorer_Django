from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

class ListaFuncionarios(ListView):
    template_name = "templates/funcionarios.html"
    model = Tabela_Funcionario
    context_object_name = "funcionarios"

def cria_funcionario(request, pk):
    # Verificamos se o método POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('lista_funcionarios'))
        # Qualquer outro método: GET, OPTION, DELETE, etc...
    else:
        return render(request, "templates/form.html", {'form': form})
        # E o fluxo de requisições termina.