# from django.shortcuts import render
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import random

client = MongoClient('connection_string')
db = client['db_name']

load_dotenv()
MONGO_URI=os.getenv("MONGO_URI")

cfg_db = client['cfg_22']
cost_collection = cfg_db['cost_collection']



def generate_dummy_data():
    return {
        "wage": round(random.uniform(15, 50), 2),
        "hours": round(random.uniform(5, 40), 2),
        "trainingCost": round(random.uniform(100, 1000), 2),
        "storageCost": round(random.uniform(20, 100), 2),
        "units": round(random.uniform(1, 10), 2),
        "usageCost": round(random.uniform(100, 1000), 2),
        "maintenanceCost": round(random.uniform(50, 500), 2),
        "supervisors": round(random.uniform(1, 5), 2),
        "supervisorWages": round(random.uniform(20, 100), 2),
        "landCost": round(random.uniform(100, 1000), 2),
        "processingCost": round(random.uniform(50, 500), 2),
        "transportCost": round(random.uniform(20, 200), 2),
        "routineChecks": round(random.uniform(10, 100), 2),
        "assessments": round(random.uniform(50, 300), 2),
        "plantingCost": round(random.uniform(100, 1000), 2),
        "soilAmendments": round(random.uniform(50, 300), 2),
        "adminCost": round(random.uniform(100, 500), 2),
        "managementCost": round(random.uniform(100, 500), 2),
        "communityIncome": round(random.uniform(50, 500), 2),
        "biomassRevenue": round(random.uniform(100, 1000), 2),
        "totalBiomass": round(random.uniform(1000, 10000), 2)
    }

# Insert multiple dummy documents
dummy_documents = [generate_dummy_data() for _ in range(20)]
# print(dummy_documents)
cost_collection.insert_many(dummy_documents)

print("Dummy data inserted successfully!")
