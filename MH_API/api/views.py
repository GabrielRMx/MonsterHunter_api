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

    # GET REQUEST
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
                data = {'message': 'Monster not found ...'}
            return JsonResponse(data)

    # POST REQUEST
    def post(self, request):
        # print(request.body)
        j_data = json.loads(request.body)
        # print(j_data)
        Monster.objects.create(name=j_data['name'], type=j_data['type'], attribute=j_data['attribute'],
                               weakness=j_data['weakness'], rank=j_data['rank'])
        data = {'message': 'Success'}
        return JsonResponse(data)

    # PUT REQUEST
    def put(self, request, id):
        j_data = json.loads(request.body)
        monsters = list(Monster.objects.filter(id=id).values())
        if len(monsters) > 0:
            monster = Monster.objects.get(id=id)
            monster.name = j_data['name']
            monster.type = j_data['type']
            monster.attribute = j_data['attribute']
            monster.weakness = j_data['weakness']
            monster.rank = j_data['rank']
            monster.save()
            data = {'message': 'Monster successfully updated!'}
        else:
            data = {'message': 'Monster not found ...'}

        return JsonResponse(data)

    # DELETE REQUEST
    def delete(self, request, id):
        monsters = list(Monster.objects.filter(id=id).values())
        if len(monsters) > 0:
            Monster.objects.filter(id=id).delete()
            data = {'message': 'Monster successfully erased ...'}
        else:
            data = {'message': 'Monster not found ...'}
        return JsonResponse(data)
