from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Restaurant, User
import json
# Create your views here.
JWT_TOKEN = '63aa3e92-c3fe-4010-bd5e-bc3e38e91d5e'

class RestauranteView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id > 0:
            restaurants = list(Restaurant.objects.filter(id=id).values())
            if len(restaurants) > 0:
                restaurant = restaurants[0]
                datos = {'message': 'Success','restaurants': restaurant}
            else:
                datos = { 'message': 'Restaurant not found ...'}
            return JsonResponse(datos)
        else:
            restaurants = list(Restaurant.objects.values())
            if len(restaurants)>0:
                datos = {'message': 'Success','restaurants': restaurants}
            else:
                datos = { 'message': 'Restaurants not found ...'}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        Restaurant.objects.create(name = jd['name'], type_res = jd['type_res'], address = jd['address'], telephone = jd['telephone'])
        datos = {'message':'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        restaurants = list(Restaurant.objects.filter(id=id).values())
        if len(restaurants) > 0:
            restaurant = Restaurant.objects.get(id=id)
            restaurant.name = jd['name']
            restaurant.type_res = jd['type_res']
            restaurant.address = jd['address']
            restaurant.telephone = jd['telephone']
            restaurant.save()
            datos = {'message':'Success'}
        else:
            datos = { 'message': 'Update Failed'}
        return JsonResponse(datos)

    def delete(self, request, id):
        restaurants = list(Restaurant.objects.filter(id=id).values())
        if len(restaurants) > 0:
            Restaurant.objects.filter(id=id).delete()
            datos = {'message':'Success'}
        else:
            datos = { 'message': 'Delete Failed'}
        return JsonResponse(datos)

class UserView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body)
        print(jd)
        if len(jd) == 2:
            user = list(User.objects.filter(email=jd["email"]).values())
            
            use = User.objects.get(email=jd["email"])
            print(use.password)
            if len(user) > 0 and use.password == jd["password"]:
                datos = {'message':'Success','token':JWT_TOKEN}
            else:
                datos = { 'message': 'Auth failed'}
            return JsonResponse(datos)
        
        if len(jd) == 3:
            user = list(User.objects.filter(email=jd["email"]).values())
            if len(user) > 0:
                datos = { 'message': 'Register failed'}
            else:
                User.objects.create(name = jd['name'], email = jd['email'], password = jd['password'])
                datos = {'message':'Success'}
            return JsonResponse(datos)
            
            return JsonResponse(datos)
