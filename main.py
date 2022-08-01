# Variables d'environnement
from dotenv import load_dotenv
load_dotenv()

# Modules tiers
import re
import os
import sys
import time
import schedule
from datetime import datetime, date, timezone, timedelta
import time
from crontab import CronTab
from apscheduler.schedulers.blocking import BlockingScheduler
from zoneinfo import ZoneInfo
from importlib.metadata import version
import asyncio
import zoneinfo
from apscheduler.schedulers.background import BackgroundScheduler
from sched import scheduler
import tzlocal

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
print("PositiveCheh démarré - " + str(followers_count) + " abonnés.")

# Définir les dates (maintenant et création)
now = datetime.now()
creation = datetime(2022, 7, 25, 17, 44)
interval = str(now - creation)

# Constante pour récupérer le nombre de jours entre la création et maintenant
s = [int(s) for s in str.split(interval) if s.isdigit()]

api.update_status("Le cheh positif a été créé il y a " + str(s)[1:-1] + " jours.\nAbonnés : " + str(followers_count) + "\n\n▶️ Krose sur Twitch twitch.tv/krose_officiel"),

print("Tweet envoyé!")






 
