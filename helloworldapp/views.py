from django.shortcuts import render
from django.http import HttpResponse

from helloworldapp.models import Person


# Create your views here.


def foo(request):
    name = "Bogo"
    html = "<html><body>Hello World ! from {name} </body></html>".format(name=name)
    return HttpResponse(html)


def foo2(request):
    return render(request, "helloworld.html", {"name": "Bogo"})


def foo3(request, name):  # helloworld2 /Bogo
    return render(request, "helloworld.html",
                  {"name": name})


def foo4(request, name):
    return render(request, "helloworld3.html",
                  {"name": name})


#####################################


def foo5(request, ):
    return render(request, "helloworld4.html",
                  {"persons": Person.objects.all()})


def foo6(request):  # read css
    return render(request, "helloworld5.html", {"name": "Bogo"})


def foo7(request):  # load image from static
    return render(request, "helloworld6.html")


def foo8(request):  # datatable
    return render(request, "helloworld7.html")


from django.shortcuts import redirect
from .forms import FormPerson


def formsearch(request):
    if request.method == "POST":
        form = FormPerson(request.POST)
        if form.is_valid():
            formperson = form.save(commit=False)
            return redirect('/formresult/{}/'.format(formperson.name))
    else:
        form = FormPerson()
    return render(request, 'form_model.html', {'form': form})


def formresult(request, name):
    html = """<html><h1>Search result</h1><body>
    This is the name that was searched: {}</body></html>""".format(name)
    return HttpResponse(html)