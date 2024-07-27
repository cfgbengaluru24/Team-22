from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import random
from datetime import datetime


load_dotenv()
MONGO_URI=os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)

cfg_db = client['cfg_22']
onboarding = cfg_db['onboarding']

@csrf_exempt
@require_http_methods(["POST"])
def save_data(request):
    
    try:
        data = request.POST
        topview = request.FILES.get('top_view')
        sideview = request.FILES.get('side_view')
        range_val = data.get('range')
        place = data.get('place')
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        # print(data)

        # Save images to MongoDB
        topview_id = save_image(topview)
        sideview_id = save_image(sideview)

        current_datetime = datetime.now()

        # Create a new document in the onbaording collection
        doc = {
            'topview': topview_id,
            'sideview': sideview_id,
            'range': range_val,
            'place': place,
            'latitude': latitude,
            'longitude':longitude,
            'current_datetime':current_datetime
        }
        print(doc)
        onboarding.insert_one(doc)
        print("now redirecting")
        return render(request, 'onboarding/index.html')
    except Exception as e:
        return HttpResponse('Error saving data: ' + str(e))

def save_image(image):
    try:
        # Generate a random filename for the image
        filename = str(random.randint(1000, 9999)) + '.' + image.name.split('.')[-1]
        # Save the image to MongoDB
        image_id = cfg_db['onboarding_images'].insert_one({'image': image.read(), 'filename': filename}).inserted_id
        return image_id
    except Exception as e:
        print(e)



def index(request):
    return render(request, 'onboarding/index.html')

def identify(request):
    return render(request, 'onboarding/identify.html')