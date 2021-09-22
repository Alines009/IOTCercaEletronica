from django.http import JsonResponse
from django.shortcuts import render, redirect
import json


def index(request):
    return render(request, 'index.html')


def rastrear(request):

    if request.POST:
        lista = request.POST
        lista = lista.getlist("data[]")
        print(lista)
        aux = "{ \n \"checkpoints\": \n ["+','.join(lista)+"] \n}"
        with open("../checkpoints.json", "w") as outfile:
            outfile.write(aux)

        print("depois de salvar arquivo")
        return JsonResponse({'response': 'ok'})

    try:
        f = open("../alert.txt", "r")
        sensor_data = f.read().split("#")
        print(sensor_data)
        f.close()

        if len(sensor_data) == 2:

            status_cerca = eval(sensor_data[0])
            coordenadas = tuple(map(float, sensor_data[1][1:-1].split(', ')))

            print(status_cerca)

            return render(request, 'rastrear.html', {'msg': True, 'status_cerca': status_cerca, 'latitude': coordenadas[0], 'longitude': coordenadas[1]})
        else:
            return render(request, 'rastrear.html')

    except IOError:
        return render(request, 'rastrear.html')
