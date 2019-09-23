from django.shortcuts import render

def index(request):
    context = {
        'nomes':[
            'eric',
            'fagner',
            'barbara',
            'fayra',
        ],
        'vazio': False,
        'teste': 'teste'
    }
    return render(request,'index.html', context)