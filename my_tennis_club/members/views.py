from django.http import HttpResponse #this is used to send a response back to the users browsers
from django.template import loader #loader is used to load HTML templates in this case (all_members.html)
from .models import Member #this refers to a model representing a db table where data about members is stores

def members(request): #this is a view function that handles a request when someone visits a specific URL
    mymembers = Member.objects.all().values() #fetches all the rows from the Members table in the database
    template = loader.get_template('all_members.html') #this line loads an html file called all_members.html from the templates folder
    context = { #the context is a dictionary that stores variables you want to pass to the template.
        'mymembers' : mymembers, # here the key 'mymembers' holds all the member data
    }
    return HttpResponse(template.render(context, request)) #this line takes the context renders it into the html template and sends result ans an HTTP response to the user's browser


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember':mymember,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def testing(request):
    template = loader.get_template('template.html')
    context = {
        'firstname': 'Patrick',
    }
    return HttpResponse(template.render(context, request))



