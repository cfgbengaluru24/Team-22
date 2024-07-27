from django.shortcuts import render
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
cfg_db = client['cfg_22']
cost_collection = cfg_db['cost_collection']

def fetch_default(request):
    documents = list(cost_collection.find())
    sums = {
        "wage": 0,
        "hours": 0,
        "trainingCost": 0,
        "storageCost": 0,
        "units": 0,
        "usageCost": 0,
        "maintenanceCost": 0,
        "supervisors": 0,
        "supervisorWages": 0,
        "landCost": 0,
        "processingCost": 0,
        "transportCost": 0,
        "routineChecks": 0,
        "assessments": 0,
        "plantingCost": 0,
        "soilAmendments": 0,
        "adminCost": 0,
        "managementCost": 0,
        "communityIncome": 0,
        "biomassRevenue": 0,
        "totalBiomass": 0
    }
    counts = len(documents)

    for doc in documents:
        for key in sums.keys():
            sums[key] += doc.get(key, 0)

    averages = {key: (sums[key] / counts) if counts > 0 else 0 for key in sums.keys()}
    
    return render(request, 'cost_analysis/cost_analysis_form.html', averages)

