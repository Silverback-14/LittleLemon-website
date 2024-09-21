from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import LogForm
# Create your views here.


def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    response = HttpResponse()
    response.headers['Age'] = 20
    msg = f'''<br>
        <br>Path:{path}
        <br>Address:{address}
        <br>Scheme:{scheme}
        <br>Method:{method}
        <br>User agent:{user_agent}
        <br>Path info:{path_info}
        <br>
        <br>{response.headers}
        
    '''
    return HttpResponse(msg, content_type='text/html', charset='utf-8')


def menu(request, dish):
    items = {
        'pasta': 'italian dish i dont like very much',
        'dosa': 'indian dish - my fav',
        'roti': 'average north indian breakfast dish',
    }

    desc = items[dish]
    return HttpResponse(f'<h2>{dish}</h2>'+desc)


def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'home.html', context)


def about(request):
    about_content={'about':"Based in Chicago, Illinois, Little Lemon is a family owned restaurant"}
    return render(request,'about.html',about_content)
