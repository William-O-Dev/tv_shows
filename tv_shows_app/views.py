from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Network, Show

def home(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request,'shows.html', context)

def new(request):
    return render(request,'new.html' )

def show(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id),
    }
    return render(request,'show.html', context)

def edit(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id),
    }
    return render(request,'edit.html', context)

def create(request):
    errors = Show.objects.basic_validator(request.POST, 'new')
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else: 
        new_network = Network.objects.create(name=request.POST['network'])
        Show.objects.create(
            title=request.POST['title'],
            network=new_network,
            release_date=request.POST['release_date'],
            description=request.POST['description'],
        )
        return redirect('/shows')

def delete(request, show_id):
    show_to_delete = Show.objects.get(id=show_id)
    show_to_delete.delete()
    return redirect('/shows')

def update(request, show_id):
    errors = Show.objects.basic_validator(request.POST, 'edit', show_id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else:
        all_shows=Show.objects.get(id=show_id)
        updated_show=Show.objects.get(id=show_id)
        updated_show.title=request.POST['title']
        updated_show.release_date=request.POST['release_date']
        updated_show.description=request.POST['description']
        updated_show.save()
        updated_network=Network.objects.get(id=updated_show.network.id)
        updated_network.name=request.POST['network']
        updated_network.save()
        return redirect(f'/shows/{show_id}')