import subprocess
from time import sleep
from random import randint

locations = [
"Mountain",
"Piedmont",
"Ammo",
"BBQ",
"Ranch",
"Barley",
"Hops",
"Glinda",
"MIT",
"Bill",
"Earnhardt",
"Cub",
"The L",
"Wrigley",
"Brown",
"Coney Dog",
"Florida Man",
"Snow",
"Vice",
"Situation",
"Empire",
"Gotham",
"Grand Central",
"Insomnia",
"Tofu Driver",
"Cheese",
"Fresh Prince",
"Hawkins",
"uban Sandwich",
"Precedent",
"Oregon Trail",
"Casino",
"Cube",
"Dogg",
"Eazy",
"Lamar",
"Pac",
"Floatie",
"Sanitation",
"Santana",
"Inside",
"Cobain",
"Cornell",
"Hendrix",
"Radiohall",
"Crosby",
"Bagel Poutine",
"Expo 67",
"Comfort Zone",
"The 6",
"Granville",
"Stanley",
"Vansterdam",
"Mansbridge",
"Boltzmann",
"Hofburg",
"Guildhouse",
"Nevski",
"Tkalciceva",
"Blue Lagoon",
"Staromak",
"Vltava",
"LEGO",
"Lennujaam",
"Sauna",
"Tram",
"Jardin",
"Seine",
"Castle",
"Wurstchen",
"Agora",
"Odeon",
"Danube",
"Fuzzy Pony",
"Reyka",
"Dullahan",
"Grafton",
"Yam Park",
"Tayelet",
"Duomo",
"Galleria",
"Colosseum",
"Daugava",
"Saeima",
"Talksa",
"Neris",
"Chemin",
"Dendrarium",
"Bicycle",
"Canal",
"Red Light",
"Tulip",
"Vardar",
"Fjord",
"Motlawa",
"Curie",
"Vistula",
"Bairro",
"No Vampires",
"Devin Castle",
"Batllo",
"Prado",
"Djurgarden",
"Ikea",
"Syndrome",
"Alphorn",
"Altstadt",
"Lindenhof",
"Keeper Willie",
"Biscuits",
"Crumpets",
"Custard",
"United",
"The Tube",
"Besa",
"Caspian",
"Burek",
"Ghvino",
"Best Jollof",
"Mahim",
"Mutha",
"Sigiria",
"Goodbye Lenin",
"Hermitage",
"Shnur",
"Rakia",
"District",
"Lindfield",
"Mandela",
"Teleferik",
"Ataturk",
"Galata",
"Ghost",
"Lofty",
"Oval",
"Good Koala",
"Burley",
"Port Phillip",
"Yarra",
"Herdsman",
"Kings Park",
"Opera House",
"Squidney",
"Hauraki",
"Parnell",
"Botum Pagoda",
"Phooey",
"Victoria",
"Menteng",
"Old Town",
"Bosozoku",
"Drift",
"Perdana",
"Pasig",
"Garden",
"Marina Bay",
"SMRT",
"Bukhansan",
"Han River",
"Hangang",
"Datong",
"Hangover",
"Khalifa",
"Red River",
"Kaiju",
"Tango",
"Mercadao",
"Pinacoteca",
"Cueca",
"Rololandia",
"Cuy",
"Crudo",
"Cojones",
"Papers",
"Amaru",
"Station",
]

while True:
    i = randint(0,174)
    location = locations[i]
    subprocess.run([f'windscribe connect "{location}"'], shell=True)
    # wait_time = randint(1,78)
    # print(f"Pausing for {wait_time} seconds...")
    # sleep(wait_time)
    subprocess.run(["curl 'https://tools.gardenandgunmag.com/vote.php?id=11271&s=9&v1=tEj5D2NH1m&v2=585d73374a0d4393abce8ec0b5983ff9&cv=y&_=1662816971048' \
  -H 'Accept: application/json, text/javascript, */*; q=0.01' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'DNT: 1' \
  -H 'Origin: https://gardenandgun.com' \
  -H 'Referer: https://gardenandgun.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: cross-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
  --compressed"], shell=True)
    print("\n")