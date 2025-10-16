 webhook_sender.py

import requests
import json

WEBHOOK_URL = "https://discord.com/api/webhooks/1428207789637111919/t9jmLOcAXjbE8EludIi1yCPCo5fg6IEwytyev2Snx_EPbi7u169ZWgbkqAdsn_M3gZgK"  # Substitua pelo seu webhook

def send_to_discord(email, username, password, profile_link):
    payload = {
        "username": "Steam Generator",
        "embeds": [{
            "title": " Nova Conta Steam Criada",
            "color": 0x00ff00,
            "fields": [
                {"name": "Email", "value": email, "inline": False},
                {"name": "Username", "value": username, "inline": True},
                {"name": "Password", "value": f"||{password}||", "inline": True},
                {"name": "Perfil", "value": f"[Link da Conta]({profile_link})", "inline": False}
            ]
        }]
    }
    requests.post(WEBHOOK_URL, json=payload)

# Teste (apague depois):
# send_to_discord("teste@gmail.com", "testuser", "senha123", "https://steamcommunity.com/test")
