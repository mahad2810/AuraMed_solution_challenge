from pymongo import MongoClient
import random

# MongoDB Client
mongo_client = MongoClient("mongodb+srv://mahadiqbalaiml27:9Gx_qVZ-tpEaHUu@healthcaresystem.ilezc.mongodb.net/healthcaresystem?retryWrites=true&w=majority&appName=Healthcaresystem")
db = mongo_client["healthcaresystem"]
hospital_collection = db["hospitals"]

# List of phone numbers to randomly assign
HOSPITAL_PHONE_NUMBERS = ["+918582892588", "+919831455224"]

# Fetch all hospitals
hospitals = list(hospital_collection.find({}, {"_id": 1}))

# Update each hospital with a randomly assigned phone number
for hospital in hospitals:
    random_phone = random.choice(HOSPITAL_PHONE_NUMBERS)
    hospital_collection.update_one(
        {"_id": hospital["_id"]}, 
        {"$set": {"phone_number": random_phone}}
    )

print(f"✅ Updated {len(hospitals)} hospitals with shuffled phone numbers!")
