# Variables d'environnement
from dotenv import load_dotenv
load_dotenv()

# Modules tiers
import re
import os
import sys
import time
from datetime import date, datetime 
import schedule

# Importer le module de l'API Twitter
import tweepy

# Identifiants de connexion
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Autorisation des clés
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Définir l'accès au bot par les tokens
auth.set_access_token(access_token, access_token_secret)

# Appel à l'API
api = tweepy.API(auth)

# L'identifiant de l'utilisateur
id = 24971740

# Récupération de l'utilisateur
user = api.get_user(screen_name='PositiveCheh')

# Récupération du nombre d'abonnés
followers_count = user.followers_count

# Bot exécuté
print("Bot exécuté - " + str(followers_count) + " abonnés.")

# Définir les dates (maintenant et création)
now = datetime.now()
creation = datetime(2022, 7, 25, 17, 44)
interval = str(now - creation)

# Constante pour récupérer le nombre de jours entre la création et maintenant
s = [int(s) for s in str.split(interval) if s.isdigit()]

def job():
# Tweet et annonce
    api.update_status("Le cheh positif a été créé il y a " + str(s)[1:-1] + " jours.\nAbonnés : " + str(followers_count) + "\n\n▶️ Krose sur Twitch twitch.tv/krose_officiel")
    print("Script lancé.\nTweet envoyé : \nLe cheh positif a été créé il y a " + str(s)[1:-1] + " jours.\nAbonnés : " + str(followers_count) + "\n\n▶️ Krose sur Twitch twitch.tv/krose_officiel")

# Planification de tâches
schedule.every().day.at("17:44").do(job)








 
