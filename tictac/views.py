
from django.shortcuts import redirect, render
from django.contrib import messages
from.models import *

# Create your views here.

def index(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        option= request.POST.get('room_action')
        code= request.POST.get('room_code')

        if option == '1':
            game = Game.objects.filter(room_code = code).first()


            if game is None:
                messages.success(request, "Room code not found")
                return redirect('/')
            
            if game.is_over:
                messages.success(request, "room code not found")
                return redirect('/')
            

            game.game_opponent = name
            game.save()

        else:
            game = Game(game_create = name, room_code = code)
            game.save()   
            return redirect('/play/'+code + '?name=' + name) 

    return render(request, "tictac/index.html")       



def play(request, code):
    name = request.GET.get('name')
    context ={'room_code': code, 'name': name}
    return render(request, 'tictac/play.html',context)


