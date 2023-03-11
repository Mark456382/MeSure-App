import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("/home/mark/Документы/GitHub/ReactNodeApp/mesure-48110-firebase-adminsdk-mz68v-72e3e719ed.json")
firebase_admin.initialize_app(cred)
firebase_admin.reference("/users_database/").set("__info__.json")