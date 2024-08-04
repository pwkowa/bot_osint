#   ___      _       _     ____   ___ _____ 
#  / _ \ ___(_)_ __ | |_  | __ ) / _ \_   _|
# | | | / __| | '_ \| __| |  _ \| | | || |  
# | |_| \__ \ | | | | |_  | |_) | |_| || |  
#  \___/|___/_|_| |_|\__| |____/ \___/ |_|  

# Made by kowa, by <3

import json
import requests
import discord
from discord.ext import commands

with open('config.json') as config_file:
    config = json.load(config_file)
    TOKEN = config['token']
    HUNTER_API_KEY = config['hunter_api_key']

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connecté en tant que {bot.user}')

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  
    guild = ctx.guild
    member_count = guild.member_count
    response = (
        f'Pong!\n'
        f'Latence: {latency:.2f} ms\n'
        f'Serveur: {guild.name}\n'
        f'Nombre de membres: {member_count}\n'
        f'Utilisateur: {ctx.author.display_name}'
    )
    await ctx.send(response)

@bot.command()
async def numinfo(ctx, phone_number: str):
    try:
        url = f'https://api.numlookupapi.com/v1/validate/{phone_number}?apikey=num_live_KAYJ5wGhBzC92t3glm9kcjYXAYCWLsk51r0ICECM'
        response = requests.get(url)

        if response.status_code != 200:
            await ctx.send(f"Erreur lors de la récupération des informations pour le numéro: {phone_number}\nStatut de la réponse: {response.status_code}")
            return
        
        data = response.json()

        valid = "✅" if data.get('valid') else "❌"
        number = data.get('number', 'Inconnu')
        local_format = data.get('local_format', 'Inconnu')
        international_format = data.get('international_format', 'Inconnu')
        country_prefix = data.get('country_prefix', 'Inconnu')
        country_code = data.get('country_code', 'Inconnu')
        country_name = data.get('country_name', 'Inconnu')
        location = data.get('location', 'Inconnu')
        carrier = data.get('carrier', 'Inconnu')
        line_type = data.get('line_type', 'Inconnu')
        embed = discord.Embed(title=f"Informations pour le numéro: {phone_number}", color=discord.Color.green())
        embed.add_field(name="🔍 Valide", value=valid, inline=False)
        embed.add_field(name="📞 Numéro", value=number, inline=False)
        embed.add_field(name="🔢 Format local", value=local_format, inline=False)
        embed.add_field(name="🌐 Format international", value=international_format, inline=False)
        embed.add_field(name="➕ Préfixe pays", value=country_prefix, inline=False)
        embed.add_field(name="🇺🇸 Code pays", value=country_code, inline=False)
        embed.add_field(name="🌍 Nom du pays", value=country_name, inline=False)
        embed.add_field(name="📍 Localisation", value=location, inline=False)
        embed.add_field(name="📡 Opérateur", value=carrier, inline=False)
        embed.add_field(name="📱 Type de ligne", value=line_type, inline=False)
        embed.set_footer(text=f"👤 Sent by: {ctx.author.display_name}")

        await ctx.send(embed=embed)

    except requests.exceptions.RequestException as e:
        await ctx.send(f"Erreur lors de la récupération des informations pour le numéro: {phone_number}\nErreur: {e}")

@bot.command()
async def email(ctx, email_address: str):
    try:
        url = f'https://api.hunter.io/v2/email-verifier?email={email_address}&api_key={HUNTER_API_KEY}'
        response = requests.get(url)

        if response.status_code != 200:
            await ctx.send(f"Erreur lors de la récupération des informations pour l'e-mail: {email_address}\nStatut de la réponse: {response.status_code}")
            return
        
        data = response.json().get('data', {})

        result = data.get('result', 'Inconnu')
        score = data.get('score', 'Inconnu')
        email = data.get('email', 'Inconnu')
        domain = data.get('domain', 'Inconnu')
        disposable = data.get('disposable', 'Inconnu')
        webmail = data.get('webmail', 'Inconnu')
        mx_records = data.get('mx_records', 'Inconnu')
        smtp_server = data.get('smtp_server', 'Inconnu')
        smtp_check = data.get('smtp_check', 'Inconnu')
        accept_all = data.get('accept_all', 'Inconnu')
        block = data.get('block', 'Inconnu')
        gibberish = data.get('gibberish', 'Inconnu')
        pattern = data.get('pattern', 'Inconnu')

        embed = discord.Embed(title=f"Informations pour l'e-mail: {email_address}", color=discord.Color.blue())
        embed.add_field(name="📧 E-mail", value=email, inline=False)
        embed.add_field(name="📊 Score", value=score, inline=False)
        embed.add_field(name="🏢 Domaine", value=domain, inline=False)
        embed.add_field(name="♻️ Jetable", value=disposable, inline=False)
        embed.add_field(name="📬 Webmail", value=webmail, inline=False)
        embed.add_field(name="📦 MX Records", value=mx_records, inline=False)
        embed.add_field(name="📨 Serveur SMTP", value=smtp_server, inline=False)
        embed.add_field(name="✅ Vérification SMTP", value=smtp_check, inline=False)
        embed.add_field(name="📥 Accept All", value=accept_all, inline=False)
        embed.add_field(name="🚫 Bloqué", value=block, inline=False)
        embed.add_field(name="🗣️ Gibberish", value=gibberish, inline=False)
        embed.add_field(name="🔢 Pattern", value=pattern, inline=False)
        embed.set_footer(text=f"👤 Sent by: {ctx.author.display_name}")

        await ctx.send(embed=embed)

    except requests.exceptions.RequestException as e:
        await ctx.send(f"Erreur lors de la récupération des informations pour l'e-mail: {email_address}\nErreur: {e}")

@bot.command()
async def maclookup(ctx, mac_address: str):
    try:
        url = f'https://api.wigle.net/api/v2/network/detail?mac={mac_address}'
        headers = {
            'Authorization': f'Basic {WIGGLE_API_TOKEN}'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            mac_data = response.json()
            if mac_data.get('success'):
                net_details = mac_data.get('results', [{}])[0]
                ssid = net_details.get('ssid', 'Inconnu')
                address = net_details.get('housenumber', 'Inconnu')
                city = net_details.get('city', 'Inconnu')
                region = net_details.get('region', 'Inconnu')
                country = net_details.get('country', 'Inconnu')
                frequency = net_details.get('frequency', 'Inconnu')
                first_seen = net_details.get('firsttime', 'Inconnu')
                last_seen = net_details.get('lasttime', 'Inconnu')
                embed = discord.Embed(title=f"Informations pour l'adresse MAC: {mac_address}", color=discord.Color.blue())
                embed.add_field(name="SSID", value=ssid, inline=False)
                embed.add_field(name="Adresse", value=address, inline=False)
                embed.add_field(name="Ville", value=city, inline=False)
                embed.add_field(name="Région", value=region, inline=False)
                embed.add_field(name="Pays", value=country, inline=False)
                embed.add_field(name="Fréquence", value=frequency, inline=False)
                embed.add_field(name="Première vue", value=first_seen, inline=False)
                embed.add_field(name="Dernière vue", value=last_seen, inline=False)
                embed.set_footer(text=f"👤 Sent by: {ctx.author.display_name}")

                await ctx.send(embed=embed)
            else:
                await ctx.send(f"Aucune information trouvée pour l'adresse MAC: {mac_address}")
        else:
            await ctx.send(f"Erreur lors de la récupération des informations pour l'adresse MAC: {mac_address}\nStatut de la réponse: {response.status_code}")

    except requests.exceptions.RequestException as e:
        await ctx.send(f"Erreur lors de la récupération des informations pour l'adresse MAC: {mac_address}\nErreur: {e}")

@bot.command()
async def cdox(ctx, *, pseudo: str):
    try:
        guild = ctx.guild
        channel_name = pseudo.replace(" ", "-") 
        new_channel = await guild.create_text_channel(channel_name)
        
        embed = discord.Embed(title=f"{pseudo}", description=f"Channel pour {pseudo}", color=discord.Color.blue())
        embed.set_footer(text=f"👤 Sent by: {ctx.author.display_name}")
        
        await new_channel.send(embed=embed)
        
        await ctx.send(f'Channel créé: {new_channel.mention}')

    except discord.errors.Forbidden:
        await ctx.send("Je n'ai pas la permission de créer un canal.")
    except discord.errors.HTTPException as e:
        await ctx.send(f"Erreur lors de la création du canal: {e}")


bot.run(TOKEN)
