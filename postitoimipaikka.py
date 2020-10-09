import urllib.request
import json

JSON_URL = 'https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json'


def hae_postinumerot():
    with urllib.request.urlopen(JSON_URL) as response:
        return json.loads(response.read())


def main():
    # strip() ottaa tyhjät alusta ja lopusta
    haettava = input('Kirjoita postinumero: ').strip()

    postinumerot = hae_postinumerot()

    if haettava in postinumerot:
        # title() muuttaa tekstit alkamaan isolla alkukirjaimella
        print(postinumerot[haettava].title())
    else:
        print('Postitoimipaikkaa ei löytynyt')


if __name__ == '__main__':
    main()

# terminaalissa siirry swd4tn023/00_linux_ja_python/src kansioon
# kirj. ls -l  -> listaa  mitä tiedostoja on
# kirj python3 esimerkki_postitoimipaikka.py  -> pystytään suorittamaan koodi
# kirj python3 -i esimerkki_postitoimipaikka.py  -> suoritus interaktiivisessa tilassa (suorittaa ensin koodin ja sen jälkeen voi terminaalissa hakea titeto)
# kirj esim hae_postinumerot() -> tunnistaa että tämä funktio on määritelty hakee ne tiedot jota se sisältää
