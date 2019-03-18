from django.shortcuts import render, get_object_or_404, redirect
from .models import Group, User


def index(request):
    users = User.objects.all()
    groups = Group.objects.all()
    return render(request, 'groups/index.html', {'users': users, 'groups': groups})


def edit(request, user_id):
    username = request.POST.get('username')
    group = request.POST.get('group')
    if group and username:
        user = get_object_or_404(User, id=user_id)
        user.username = username
        user.group = get_object_or_404(Group, name=group)
        user.save()
    return redirect('/groups')


def editGroup(request, group_id):
    name = request.POST.get('name')
    description = request.POST.get('description')
    if description and name:
        group = get_object_or_404(Group, id=group_id)
        group.name = name
        group.description = description
        group.save()
    return redirect('/groups')


def delete(request, user_id):
    if 'delUser' in request.POST:
        User.objects.filter(id=user_id).delete()
    elif 'delGroup' in request.POST:
        Group.objects.filter(id=user_id).delete()
    return redirect('/groups')


def add(request):
    username = request.POST.get('username')
    group = request.POST.get('group')
    if group and username:
        user = User.objects.create(username=username, group=Group.objects.get(name=group))
        user.save()
    return redirect('/groups')


def addGroup(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    if name and description:
        group = Group.objects.create(name=name, description=description)
        group.save()
    return redirect('/groups')
