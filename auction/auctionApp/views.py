from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.timezone import make_aware
from datetime import datetime
from django.http import HttpResponseBadRequest
from django.shortcuts import render

def index(request):
    return HttpResponse("LISTINGS PAGE GO HERE.")


def user_api(request):
    cur_user = request.user
    if cur_user.is_anonymous:
        return JsonResponse({
            'cur_user_data' : 'not logged in'
        })
    else:
        return JsonResponse({
            'cur_user_data' : cur_user.to_dict()
            })
        

##########################################
#Stuff By Steph
##########################################

def getQuestion(request, question_id):
    if request.method == "GET":
        questionData = Question.objects.filter(id = question_id).values()

        data = {
            'answer' : list(questionData)
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

def getUserQuestions(request, user_id):
    if request.method == "GET":
        questionData = Question.objects.filter(asker__id=user_id).values('id', 'question', 'answer')
        
        data = {}

        for i in questionData:
            data[i.get('id')] = i

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')
    
def getQuestionsAskedToUser(request, user_id):
    if request.method == "GET":
        data = {}
        if User.objects.filter(id = user_id).exists():
            _seller = User.objects.get(id = user_id)
            items = Item.objects.filter(seller = _seller).values('id')

            for i in items:
                _question = Question.objects.filter(item__id = i.get('id'))
                if (_question.exists()):
                    data[i.get('id')] = {
                        'question' : list(_question.values('id', 'question', 'answer')), 
                        'itemId' : i.get('id')
                    }

            if len(data) <= 0:
                data = {
                    'ObjectsFound' : False
                }
            else:
                data['ObjectsFound'] = True

        else:
            data['ObjectsFound'] = False
        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

def getItemQuestions(request, item_id):
    if request.method == "GET":
        _item = Item.objects.get(id = item_id)
        
        questionData = Question.object.filter(item = _item).values()
        
        data = {
            'questions' : list(questionData)
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')


def getItem(request, item_id):
    if request.method == "GET":
        item = Item.objects.filter(id = item_id)

        itemData = item.values('name', 'desc', 'start_time', 'end_time',
            'start_price', 'cur_price')

        data = {
            'item' : list(itemData),
            'seller' : list(User.objects.filter(
                id = item.values('seller')[0]['seller']
                ).values('first_name', 'last_name'))
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

@csrf_exempt
def postQuestion(request, item_id):
    if request.method == "POST":
        postData = json.loads(request.body.decode("utf-8"))
        print("posting question to database")
        _asker = User.objects.get(id = postData.get('userId', None))
        _item = Item.objects.get(id = item_id)
        _question = postData.get('question', None)

        Question.objects.create(question = _question, asker = _asker, item = _item)
        response = JsonResponse({'status' : 'question posted'})

        return response
    return HttpResponseBadRequest('Invalid request')


@csrf_exempt
def postAnswer(request, question_id):
    if request.method == "POST":
        question = Question.objects.get(id = question_id)
        postData = json.loads(request.body.decode("utf-8"))

        _answer = postData.get('answer')

        question.answer = _answer
        question.save()

        data = {
            'updated' : True
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

@csrf_exempt
def postItem(request):
    if request.method == "POST":
        _image = request.FILES.get('file')
        _name = request.POST.get('name')
        _desc = request.POST.get('desc')
        _start_time = make_aware(datetime.fromisoformat(request.POST.get('startTime')))
        _end_time = make_aware(datetime.fromisoformat(request.POST.get('endTime')))
        _start_price = request.POST.get('startPrice')


        _seller = User.objects.get(id = request.POST.get('seller'))

        Item.objects.create(name = _name, desc = _desc,
            start_time = _start_time, end_time = _end_time, 
            start_price = _start_price, cur_price = _start_price,
            image = _image, seller = _seller)

        data = {
            'status' : 'item added'
        }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

@csrf_exempt
def placeBid(request, item_id):
    if request.method == "POST":
        item = Item.objects.get(id = item_id)

        postData = json.loads(request.body.decode("utf-8"))

        _bid = postData.get('bid')

        data = {}

        if _bid > item.cur_price:
            item.newBid(_bid)
            data = {
                'status' : 'bid placed'
            }
        else:
            data = {
                'status' : 'ivalid bid'
            }

        return JsonResponse(data)
    return HttpResponseBadRequest('Invalid request')

##########################################
#End of Stuff by Steph
##########################################

def listings_api(request) -> HttpResponse:
    itemData = Item.objects.all
    return JsonResponse({
        'item': [
            item.to_dict() for item in Item.objects.all()
        ]
    })