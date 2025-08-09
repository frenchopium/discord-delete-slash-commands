import requests

TOKEN = "your_bot_token"
CLIENT_ID = "your_client_id"

url = f"https://discord.com/api/v10/applications/{CLIENT_ID}/commands"

headers = {
    "Authorization": f"Bot {TOKEN}",
    "Content-Type": "application/json"
}

response = requests.put(url, json=[], headers=headers)

if response.status_code == 200:
    print("✅ Toutes les commandes globales ont été supprimées.")
else:
    print(f"❌ Erreur : {response.status_code} - {response.text}")