from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from Instagram.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.core.files.storage import FileSystemStorage
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
    curr_user =request.user
    mi_usuario = MiUsuario.objects.get(pk = request.user.pk)
    post_user = post.objects.filter(user_id = curr_user.id)
    context = {'usuario_actual' : mi_usuario,'post_user': post_user }
    return render (request, 'avicii.html',context)

@login_required
def galeria (request):
    if request.method == 'GET':
        return render (request, 'galeria.html')
    else:
        photo = request.FILES['photo']
        fs = FileSystemStorage()
        curr_user = request.user;
        cantidad_post = post.objects.filter(user_id=curr_user.id).count();
        name = curr_user.username + '-'+  str (cantidad_post);
        filename = fs.save (name, photo)
        path = fs.url(filename)
        description = request.POST['descripcion'];
        mi_curr_user = MiUsuario (pk = curr_user.pk)
        newPost = post (photo= path, descripcion= description, user_id = mi_curr_user)
        newPost.save()


        return redirect('avicii')
