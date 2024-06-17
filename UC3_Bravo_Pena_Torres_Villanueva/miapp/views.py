from django.shortcuts import render, HttpResponse, redirect

layout ="""
<h1> Lenguaje de Programacion III - 2024) | UC3 </h1>
<hr/>
<h4>Menu:</h4>
<ul>
    <li>
        <a href="/inicio"> Inicio</a>
        </li>
        <li><a href="/primos">Numeros primos</a></li>
    </ul>
<hr/>
"""
# Create your views here.
def index(request):
    return render(request, 'index.html')


def inicio(request):
    return render(request, 'inicio.html')

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos(request, a=0, b=100):
    if a > b:
        return redirect('primos', a=b, b=a)
    
    resultado = f"""
        <h2> Números primos de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """
    
    for num in range(a, b + 1):
        if es_primo(num):
            resultado += f"<li> {num} </li>"
    
    resultado += "</ul>"
    return HttpResponse(layout + resultado)