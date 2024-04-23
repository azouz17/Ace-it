from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseRedirect
import json
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib.auth import authenticate,login 
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render
from django.conf import settings



def login(request):
    try:
        POST = json.loads(request.body)
        find_user = authenticate(username=POST['username'], password=POST['password'])
        if find_user is not None:
            user = User.objects.get(username = find_user.username)
            auth.login(request,find_user)
            return JsonResponse({
                'status': 200,
                'first_name': user.first_name ,
                'last_name': user.last_name,
                'email': user.username ,
                'date_joined': user.date_joined,
                'id': user.id,
                'timeout': settings.SESSION_COOKIE_AGE
            })
        else:  
            return JsonResponse({
                'status': 404,
                'message':'no user found',
                                 })
    except(ObjectDoesNotExist):
            return JsonResponse({
                'status': 404,
                'message':'no user found',
                                 })
def logout(request):
    print('logged ot user')
    auth.logout(request)
    return JsonResponse({
         'status': 200
    })   

@csrf_exempt
def forgotPassword(request):
      return HttpResponseRedirect('http://127.0.0.1:8000/accounts/password_reset/')

def signup(request):
     try:
        POST = json.loads(request.body)
        temp = User.objects.get(username = POST['email'])
        if temp is None:
            user = User.objects.create_user(username = POST['email'], first_name = POST['first_name'], last_name = POST['last_name'], email = POST['email'])
            print(POST['password'])
            user.set_password(POST['password'])
            user.save()
            auth.login(request,user)
            return JsonResponse({
                'status': 200,
                'first_name': user.first_name ,
                'last_name': user.last_name,
                'email': user.username ,
                'date_joined': user.date_joined,
                'id': user.id,
                'timeout': settings.SESSION_COOKIE_AGE
            })
        else:  
            return JsonResponse({
                'status': 404,
                'message':'user already exixsts',
                                 })
     except(ObjectDoesNotExist):
            user = User.objects.create_user(username = POST['email'], first_name = POST['first_name'], last_name = POST['last_name'],email = POST['email'])
            print(POST['password'])
            user.set_password(POST['password'])
            user.save()
            auth.login(request,user)
            return JsonResponse({
                'status': 200,
                'first_name': user.first_name ,
                'last_name': user.last_name,
                'email': user.username ,
                'date_joined': user.date_joined,
                'id': user.id
            })
@login_required
def editProfile(request):
     try:
          status = 0
          POST = json.loads(request.body)
          user = User.objects.get(id = POST['user_id'])
          if(user.email == POST['email']):
               user.first_name = POST['first_name']
               user.last_name = POST['last_name']
               status = 200
               user.save()
          else:
               old_user = User.objects.get(username = POST['email'])
               if(User.objects.get(email = POST['email'])):
                    status = 409
                    
          return JsonResponse({
               'status': status,
               'first_name': user.first_name,
               'last_name': user.last_name,
               'email': user.email,
               'id': POST['user_id']
          })
     except(ObjectDoesNotExist):
          print('Account not found')
          user.first_name = POST['first_name']
          user.last_name = POST['last_name']
          user.email = POST['email']
          user.username = POST['email']
          status = 200
          user.save()
          return JsonResponse({
               'status': status,
               'first_name': user.first_name,
               'last_name': user.last_name,
               'email': user.email,
               'id': POST['user_id']
          })
     
@login_required
def creatTable(request):
     POST = json.loads(request.body)
     user = User.objects.get(id = POST['id'])
     table = Table.objects.create( user_id = user)
     table.save()
     return getTable(request)
def getTable(request):
     try:
           POST = json.loads(request.body)
           table = Table.objects.get( user_id = POST['id'])
           rows = Row.objects.filter(table_id = table.id)
           row_list = []
           cell_list = {}
           for item in rows:
                 row_list.append(item.to_dict())
                 cell_list[item.id] = []
                 cells = Cell.objects.filter(row_id = item.id).order_by('column_id')
                 for item in cells:
                    cell_list[item.row_id.id].append(item.to_dict())
           columns = Column.objects.filter(table_id = table.id)
           column_list = []
           for item in columns:
                 column_list.append(item.to_dict()) 
           return JsonResponse({
                 'status':200,
                 'table_id': table.id,
                 'row_count':row_list,
                 'columns': column_list,
                'rows': cell_list
           })
     except(ObjectDoesNotExist):
                     return JsonResponse({
                'status':404,
                'message': 'No table found'
           })

@login_required    
def modifyrow(request):
      counter = 0
      try:
        POST = json.loads(request.body)
        table = Table.objects.get( user_id = POST['user_id'])
        row = Row.objects.filter(table_id = table.id)
        row = row.get(id = POST['row_id'])
        for col in POST['columns']:
              cell = Cell.objects.get(row_id = row, column_id = Column.objects.get(id = col['column_id']))
              cell.text = POST['new_row'][counter]
              cell.save()
              counter+=1
        print(POST['columns'])
        return JsonResponse({
                'status':200,
                'message': 'No ay  found'
           })
      except(ObjectDoesNotExist):
            row = Row.objects.create(table_id = table)
            for col in POST['columns']:
                Cell.objects.create(row_id = row, column_id = Column.objects.get(id = col['column_id']), text = POST['new_row'][counter])
                counter+=1
            return JsonResponse({
                'status':200,
                'message': 'No table found'
           })
      

@login_required      
def deleteRow(request):
     try:    
        POST = json.loads(request.body)
        row = Row.objects.get(id = POST['row_id'])
        row.delete()
        return JsonResponse({
             'status': 200,
             'message': 'row deleted succefuly'
        })
     except(ObjectDoesNotExist):
        return JsonResponse({
                'status':404,
                'message': 'No Row found'
           })
     
@login_required     
def addColumn(request):
     try:    
        POST = json.loads(request.body)
        table = Table.objects.get( id = POST['table_id'])
        column = Column.objects.create(name = POST['column'] ,table_id = table)
        rows = Row.objects.filter(table_id = POST['table_id'])
        for row in rows:
             Cell.objects.create(row_id = row , column_id = column, text='')
        return JsonResponse({
             'status': 200,
             'message': 'column added succefuly'
        })
     except(ObjectDoesNotExist):
        return JsonResponse({
                'status':404,
                'message': 'Something went wrong'
           })
     
@login_required     
def deleteColumn(request):
     try:    
        POST = json.loads(request.body)
        column = Column.objects.get(id = POST['column_id'])
        column.delete()
        return JsonResponse({
             'status': 200,
             'message': 'column deleted succefuly'
        })
     except(ObjectDoesNotExist):
        return JsonResponse({
                'status':404,
                'message': 'Something went wrong'
           })
     
@login_required     
def EditColumn(request):
     try:    
        POST = json.loads(request.body)
        column = Column.objects.get(id = POST['column_id'])
        column.name = POST['text']
        column.save()
        return JsonResponse({
             'status': 200,
             'message': 'column edited succefuly'
        })
     except(ObjectDoesNotExist):
        return JsonResponse({
                'status':404,
                'message': 'Something went wrong'
           })
     
@login_required     
def getExperts(request):
     experts = Expert.objects.filter(approved = True)
     expert_list = []
     for expert in experts:
          expert_list.append(expert.to_dict())
     fields = Field.objects.all()
     field_list = []
     for field in fields:
          field_list.append(field.to_dict())
     return JsonResponse({
          'status':200,
        'experts': expert_list,
        'fields': field_list
    })

@login_required
def sendemail(request):
     POST  = json.loads(request.body)
     try:
          send_mail(
               POST['subject'],
               POST['message'],
               'ace.it.notify@gmail.com',
               ['mostafa.azouz@gmail.com'],
               fail_silently=False,
          )
          return JsonResponse({
          'status':200,
          })
     except Exception as e:
          print(e)
          return JsonResponse({
          'status':400,
          })
     
     

@login_required     
def createExpert(request):
     try:
        POST  = json.loads(request.body)
        Expert.objects.get(id = POST['user_id'])
        return JsonResponse({
               'status': 404
          })
     except(ObjectDoesNotExist):
        field = Field.objects.get(id = POST['field'])
        expert =  Expert.objects.create(id = POST['user_id'],name = POST['name'],rate = POST['rate'],experience = POST['experience'],email = POST['email'],field = field ,about_me = POST['about_me'],linkedIn = POST['url'], profile_picture = POST['profile_picture'], approved = False , rating = 0)
        expert.save()
        return JsonResponse({
               'status': 200
          })
     
@login_required   
def getFields(request):
     try:
          fields = Field.objects.all()
          field_list = []
          for field in fields:
               field_list.append(field.to_dict())
          print(field_list)
          return JsonResponse({
               'status': 200,
               'fields': field_list
          })
     except(ObjectDoesNotExist):
          return JsonResponse({
               'status': 404
          })     

     