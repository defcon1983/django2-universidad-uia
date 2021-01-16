from django.shortcuts import render
from blog.models import Blog
from calificacion.models import Materia
# Create your views here.

def dashboard(request):

    return render(request, 'core/index.html')

def calificacion(request):
    datos = Materia.objects.all().filter(user=request.user)
    context = {
        'datos': datos
        }
    return render(request, 'core/ui-tables.html', context)
 
def home(request):
    blog = Blog.objects.all()
    context = {
       'blog': blog
    }
    return render(request, 'core/pages/home.html', context)

def quienes_somos(request):
    pass

def licenciaturas(request):
    return render(request, 'core/pages/licenciaturas.html')

def maestrias(request):
    pass

def campus(request):
    pass

def reglamento(request):
    pass

def contacto(request):
    pass