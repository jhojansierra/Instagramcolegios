from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from Instagram.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    if request.user.is_authenticated:
            return redirect('electro')
    if request.method == 'GET':
        return render (request, 'index.html')
    else:
        name = request.POST['nombre_completo']
        username = request.POST['usuario']
        email = request.POST['correo']
        password = request.POST['password']


        usuarioDjango = User.objects.create_user(username = username, password = password , email = email, first_name = name)
        miusuario= MiUsuario(usuario_django = usuarioDjango )
        usuarioDjango.save()
        miusuario.save()
        return redirect ('login')


@login_required
def electro(request):
    return render (request, 'electro.html')

@login_required
def avicii(request):
    mi_usuario = MiUsuario.objects.get(pk = request.user.pk)

    context = {'usuario_actual' : mi_usuario }
    return render (request, 'avicii.html',context)
