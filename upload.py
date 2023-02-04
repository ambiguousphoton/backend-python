import firebase_admin
from firebase_admin import credentials
import json
cred = credentials.Certificate("projectkey.json")
firebase_admin.initialize_app(cred ,{
    "databaseURL" : "https://hariom-c0713-default-rtdb.firebaseio.com/"
})

from firebase_admin import db
ref = db.reference('/')
with open("bookinfo.json","r") as f:
    file_contents = json.load(f)
ref.set(file_contents)

