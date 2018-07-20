

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import Notes

from django.contrib.auth import authenticate, login


from datetime import datetime
from .decorators import active_user_required

from django.contrib.auth.models import User



def authenticate(request):
    username = request.POST.get("username")
    if not username:
        return None
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        print('authentication failed!!')
    return user


def mylogin(request):
    template = loader.get_template('zpxnotes/login.html')
    if request.method == 'GET':
        context = {}
        response = HttpResponse(template.render(context, request))
        return response

    if request.method == 'POST':
        print('hello')
        user = authenticate(request)
        print(user)
        if user is not None:
            if user.is_active:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                # request.session.set_expiry(86400)
                print(login(request, user))




# Create your views here.
@active_user_required
def index(request):


    template = loader.get_template('zpxnotes/index.html')

    if request.method == 'GET':

        notes = Notes.objects.filter(author=request.user)
        context = {'notes': notes}

        response = HttpResponse(template.render(context, request))
        return response
    if request.method == 'POST':
        user = request.user
        note = request.POST.get('note')
        note_obj = Notes(data = note, author = user, created_at=datetime.now(), updated_at=datetime.now())
        note_obj.save()
        return HttpResponseRedirect('index')




@active_user_required
def edit(request):

    template = loader.get_template('zpxnotes/edit.html')

    if request.method == 'GET':
        id = request.GET.get('id')

        notes = Notes.objects.get(id=int(id))
        context = {'notes': notes}

        response = HttpResponse(template.render(context, request))
        return response
    if request.method == 'POST':
        note = request.POST.get('note')
        id = request.POST.get('id')
        note_obj = Notes.objects.get(id=int(id))

        if int(note_obj.author.id) != int(request.user.id):
            return HttpResponseRedirect('index')

        note_obj.data = note
        note_obj.save()
        return HttpResponseRedirect('index')


@active_user_required
def delete(request):

    if request.method == 'GET':
        id = request.GET.get('id')

        note_obj = Notes.objects.get(id=int(id))
        if int(note_obj.author.id) != int(request.user.id):
            return HttpResponseRedirect('index')
        note_obj.delete()


        return HttpResponseRedirect('index')





