from django.shortcuts import render
#from django.http import HttpResponse

gravestonestest = [
    {
        'adventurer_name': 'Kaine',
        'race': 'Human',
        'class': 'Wizard',
        'enscript': 'Here lies Kaine, who bravely opposed the evils of Ravenloft',
        'date_posted': 'September 19, 2020',
        'player': 'Adam'
    },
    {
        'adventurer_name': 'Rondall',
        'race': 'Half-Elf',
        'class': 'Bard',
        'enscript': 'This stone remembers Rondall, whose body still lies under the windmill by which he was crushed.',
        'date_posted': 'September 23, 2020',
        'player': 'Benjamin'
    }
]

# Create your views here.
def home(request):
    return render(request, 'grave/home.html')

def explore(request):
    context = {
        'gravestones': gravestonestest
    }
    return render(request, 'grave/explore.html', context)

def newgrave(request):
    return render(request, 'grave/newgrave.html')


def about(request):
    return render(request, 'grave/about.html', {'title': 'About'})
