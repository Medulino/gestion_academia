from django.shortcuts import redirect
from django.contrib import messages

def profesor_required(view_func):
    def wrapper(
        request,
        *args,
        **kwargs
    ):
        if not request.user.is_authenticated:
            return redirect(
                'login'
            )
        if request.user.tipo != 'profesor':
            messages.error(
                request,
                'Acceso denegado.'
            )
            return redirect(
                'inicio'
            )
        return view_func(
            request,
            *args,
            **kwargs
        )
    return wrapper