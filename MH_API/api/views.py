import json
from django.shortcuts import render
from django.views import View
from .models import Monster
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class MonsterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            monsters = list(Monster.objects.filter(id=id).values())
            if len(monsters) > 0:
                monster = monsters[0]
                data = {'message': 'Success', 'monsters': monsters}
            else:
                data = {'message': 'Monster not found ...'}
            return JsonResponse(data)
        else:
            monsters = list(Monster.objects.values())
            if len(monsters) > 0:
                data = {'message': 'Success', 'monsters': monsters}
            else:
                data = {'message': 'There are not monsters here...'}
            return JsonResponse(data)

    def post(self, request):
        # print(request.body)
        j_data = json.loads(request.body)
        # print(j_data)
        Monster.objects.create(name=j_data['name'], type=j_data['type'], attribute=j_data['attribute'],
                               weakness=j_data['weakness'], rank=j_data['rank'])
        data = {'message': 'Success'}
        return JsonResponse(data)

    def put(self, request):
        pass

    def delete(self, request):
        pass
