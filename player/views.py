import json
from ftplib import FTP
from io import BytesIO
from decouple import config

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect


def home(request):
    return render(request, 'player/index.html')


def scoreboard(request):
    return render(request, 'player/scoreboard.html')


def schedule(request):
    return render(request, 'player/schedule.html')


def playerProfile(request):
    # GET or POST
    if request.method == 'GET':
        player_id = request.GET['player_id']
        print(player_id)
        context = {'player_id': player_id}
        return render(request, 'player/player.html', context)
    return redirect('home')


def team(request):
    return render(request, 'player/team.html')


def teamStanding(request):
    return render(request, 'player/standing.html')


def readFtp(request, id):
    ftp = FTP(config('FTP_URL'))
    ftp.login(user=config('FTP_USER'), passwd=config('FTP_PASS'))
    ftp.cwd('/player')
    r = BytesIO()
    ftp.retrbinary('RETR player_'+id+'.json', r.write)
    bytes_data = r.getvalue()
    data = bytes_data.decode("utf-8")
    json_data = json.loads(data)
    ftp.quit()
    # print(json_data)
    return JsonResponse(json_data)
