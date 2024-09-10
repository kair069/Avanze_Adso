from django.shortcuts import render

# Create your views here.
def hub(request):
    return render(request, 'hub.html')


def example_view(request):
    return render(request, 'nombre_de_la_app/example.html')