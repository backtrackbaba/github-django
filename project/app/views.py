from django.shortcuts import render, HttpResponse
import requests
import json

# Create your views here.

# views.py


def index(request):
    return HttpResponse('Hello World!')


def test(request):
    return HttpResponse('My second view!')


def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
            userData['name'] = data['name']
            userData['blog'] = data['blog']
            userData['email'] = data['email']
            userData['public_gists'] = data['public_gists']
            userData['public_repos'] = data['public_repos']
            userData['avatar_url'] = data['avatar_url']
            userData['followers'] = data['followers']
            userData['following'] = data['following']
        parsedData.append(userData)
    return render(request, 'app/profile.html', {'data': parsedData})


def repos_list(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username + '/repos')
        jsonList = []
        jsonList.append(json.loads(req.content))
        userData = {}
        for data in jsonList:
            userData['repository_name'] = data['name']
            userData['repository_description'] = data['description']
            userData['repo_stars'] = data['emastargazers_countil']
            userData['repo_watchers'] = data['watchers_count']
            userData['repo_forks'] = data['forks_count']
            userData['repo_main_language'] = data['language']
            userData['repo_license'] = data['license']['name']
            userData['repo_license'] = data['updated_at']
        parsedData.append(userData)
    return render(request, 'app/listing.html', {'data': parsedData})
