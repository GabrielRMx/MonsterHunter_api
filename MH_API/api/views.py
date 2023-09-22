import json
from django.shortcuts import render
from django.views import View
from .models import Monster
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Aqui definimos la clase MonsterView que contiene los metodos necesarios para las peticiones.
class MonsterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # METODO GET
    def get(self, request, id=0):

        # Se verifica si el id es mayor a 0 para hacer el filtrado.
        if id > 0:

            # Se almacena la lista con el elemento que corresponde al id, a traves del metodo filter.
            monsters_list = list(Monster.objects.filter(id=id).values())

            # Se almacena el diccionario con el mensaje y los datos del monstro.
            if len(monsters_list) > 0:
                data = {'message': 'Success', 'monsters': monsters_list}

            # En caso de que el id no exista.
            else:
                data = {'message': 'Monster not found ...'}

            # Por ultimo se devuelve la respuesta JSON con los datos que corresponden.
            return JsonResponse(data)

        # En caso de que no se especifique el id, se almacena la lista completa de los monstruos.
        else:
            monsters = list(Monster.objects.values())

            # Se verifica que hayan elementos en la lista.
            if len(monsters) > 0:
                data = {'message': 'Success', 'monsters': monsters}

            # En caso de que el id no exista.
            else:
                data = {'message': 'Monster not found ...'}

            # Se devuelve la respuesta JSON con los datos que corresponden.
            return JsonResponse(data)

    # # METODO POST
    def post(self, request):

        # Se almacena la estructura del JSON como diccionario usando el metodo loads.
        j_data = json.loads(request.body)

        # Se le aplica al modelo el metodo objects para manipular los objetos.
        # Con el metodo create, creamos un nuevo objeto, en este caso un nuevo monstruo.
        Monster.objects.create(name=j_data['name'], type=j_data['type'], attribute=j_data['attribute'],
                               weakness=j_data['weakness'], rank=j_data['rank'])

        # Se devuelve el mensaje de que ha sido exitoso.
        data = {'message': 'Success'}

        # Se devuelve la respuesta cuando el monstruo fue creado con exito.
        return JsonResponse(data)

    # # METODO PUT
    def put(self, request, id):

        # Se almacena la estructura del JSON como diccionario usando el metodo loads.
        j_data = json.loads(request.body)

        # Se almacena la lista con el elemento que corresponde al id, a traves del metodo filter.
        monsters = list(Monster.objects.filter(id=id).values())

        # Se verifica si se encuentra un elemento con ese id almacenado en la lista.
        if len(monsters) > 0:

            # Se le asignan los valores a cada clave / dato del monstruo.
            monster = Monster.objects.get(id=id)
            monster.name = j_data['name']
            monster.type = j_data['type']
            monster.attribute = j_data['attribute']
            monster.weakness = j_data['weakness']
            monster.rank = j_data['rank']
            monster.save()
            data = {'message': 'Monster successfully updated!'}

        # En caso de que el id no exista.
        else:
            data = {'message': 'Monster not found ...'}

        # Se devuelve la respuesta JSON con los datos correspondientes.
        return JsonResponse(data)

    # METODO DELETE
    def delete(self, request, id):

        # Se almacena la lista con el elemento que corresponde al id, a traves del metodo filter.
        monsters = list(Monster.objects.filter(id=id).values())

        # Se verifica si se encuentra un elemento con ese id almacenado en la lista.
        if len(monsters) > 0:
            Monster.objects.filter(id=id).delete()
            data = {'message': 'Monster successfully erased ...'}

        # En caso de que el id no exista.
        else:
            data = {'message': 'Monster not found ...'}

        # Se devuelve la respuesta JSON con los datos correspondientes.
        return JsonResponse(data)
