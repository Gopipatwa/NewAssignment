from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from geopy.geocoders import Nominatim
import pandas as pd 



# Create your views here.



class FileView(View):
    geolocator = Nominatim(user_agent="Djsngo_App")
    def get(self, request):
        return render(request,'index.html')
        ...  # code to process a GET request

    def post(self, request):
        print(request)
        data = pd.read_excel(request.FILES['file'])
        
        # location = self.geolocator.geocode("175 5th Avenue NYC")
        data['Latitude'] = data.apply(lambda row: self.geolocator.geocode(str(row.Address)).latitude,axis=1)
        data['Longitude'] = data.apply(lambda row: self.geolocator.geocode(str(row.Address)).longitude,axis=1)
        
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="response.xls"'
        data.to_excel(response,index=False)
        # print(request.FILES['file'])
        return response

        ...  # code to process a POST request

