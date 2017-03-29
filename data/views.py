# coding: utf-8
from django.shortcuts import render
import yaml, git, os
from exegetetool import settings
from forms import ReferenceForm
from django.http import HttpResponse
from datetime import datetime, date
from django.contrib import messages

data_file = os.path.join(settings.BASE_DIR, 'exegetesDoc/data/references.yaml')

def load_yaml(position=False):
    """

    """
    with open(data_file, 'r') as file:
        try:
            datas = yaml.load(file)
            if position:
                position = 0
                for data in datas['references']:
                    data['position'] = position
                    data['title_short'] = data.get('title-short')
                    try:
                        data['date'] = "%s/%s/%s" % (int(data['issued']['month']), int(data['issued']['day']), int(data['issued']['year']))
                    except:
                        data['date'] = None
                    position += 1
        except yaml.YAMLError as e:
            print(e)
    return datas['references']

def update_yaml(request, position_id, data):
    """

    """
    datas = load_yaml()
    datas[position_id]['type'] = data['type']
    datas[position_id]['id'] = data['id']
    datas[position_id]['authority'] = data['authority']
    datas[position_id]['section'] = data['section']
    if data['date']:
        datas[position_id]['issued'] = {}
        datas[position_id]['issued']['year'] = int(data['date'][6:10])
        datas[position_id]['issued']['month'] = int(data['date'][0:2])
        datas[position_id]['issued']['day'] = int(data['date'][3:5])
    datas[position_id]['title'] = data['title']
    datas[position_id]['title-short'] = data['title_short']
    datas[position_id]['number'] = data['number']
    datas[position_id]['ECLI'] = data['ECLI']
    datas[position_id]['URL'] = data['URL']
    with open(data_file, 'w') as file:
        try:
            file.write(yaml.safe_dump({'references' : datas }, default_flow_style=False))
            messages.success(request, "The YAML file have been successfull updated")
        except yaml.YAMLError as e:
            print(e)
    return

def add_yaml(data):
    """

    """
    datas = load_yaml()
    new_entry = {
        'type': data['type'],
        'id': data['id'],
        'authority': data['authority'],
        'section': data['section'],
        'title': data['title'],
        'issued': {
            'year': int(data['date'][6:10]),
            'month': int(data['date'][0:2]),
            'day': int(data['date'][3:5]),
        },
        'title-short': data['title_short'],
        'number': data['number'],
        'ECLI': data['ECLI'],
        'URL': data['URL']
    }
    datas.append(new_entry)
    with open(data_file, 'w') as file:
        try:
            file.write(yaml.safe_dump({'references' : datas }, default_flow_style=False))
        except yaml.YAMLError as e:
            print(e)
    return

def index(request):
    """
	   Liste les entrées depuis le fichier YAML
    """
    datas = load_yaml(True)
    context = {
        'datas': datas,
    }
    return render(request, 'data/references.html', context)

def display(request, position_id):
    """

    """
    position_id = int(position_id)
    data = load_yaml(True)
    context = {
        'data' : data[position_id],
        'position_id': position_id
    }
    return render(request, 'data/display_references.html', context)

def add(request):
    """
    """
    f = ReferenceForm()

    if request.POST:
        add_yaml(request.POST)
        f = ReferenceForm(request.POST)
    context = {
        'form': f.as_p(),
    }
    return render(request, 'data/references_form.html', context)

def update(request, position_id):
    """
        Update a case
    """
    position_id = int(position_id)
    datas = load_yaml(True)[position_id]
    f = ReferenceForm(datas)
    if request.POST:
        datas = request.POST
        update_yaml(request, position_id, datas)
        f = ReferenceForm(datas)
    context = {
        'form': f.as_p(),
    }
    return render(request, 'data/references_form.html', context)

def pull(request):
    """
	   Synchronise les datas depuis le repo Github
    """
    g = git.cmd.Git('../exegetesDoc')
    g.pull()
    return

def push(request):
    """
	   Commit les modifications et les envois sur le serveur Git
    """

    return

def search(request, champs):
    """
	   Effectuer une recherche dans le fichier YAML
    """

    return

def display_yaml(request):
    """

    """
    with open(data_file, 'r') as file:
        return HttpResponse(file.read(), content_type='text/plain')
