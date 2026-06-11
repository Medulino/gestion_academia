from django.shortcuts import render
from django.shortcuts import redirect
from .forms import RegistroAlumnoForm
def registro(request):
    if request.method == 'POST':
        form = RegistroAlumnoForm(
            request.POST
        )
        if form.is_valid():
            form.save()
            return redirect(
                'login'
            )
    else:
        form = RegistroAlumnoForm()
    return render(
        request,
        'usuarios/registro.html',
        {
            'form': form
        }
    )