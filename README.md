# Network Toolbox

Network Toolbox er en kalkulator for å regne ut nettverks adresser i subnet.

For å bruke kalkulatoren fyller man inn en IP adresse og hvilke CIRD den har.
Man får da servert:
- IP Address
- Network Address
- Subnet Mask
- Broadcast Address
- First Usable Host
- Last Usable Host
- Usable Hosts
- CIDR
- IP Type
- Binary IP

Appen er skrevet av KI i sin helhet.


# Prosjektstruktur

- app.py
- Dockerfile
- requirements.txt
- docker-compose.yml
- README.md
- templates/
   - index.html

# Oppbygging

Appen består av to tjenester:

- *web*: webapplikasjonen
- *db*: en database som autentiseres mot. Databasen har ett volume "dbdata", akkurat som i Nordly appen tidligere.
