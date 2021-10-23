import praw

reddit = praw.Reddit(
    client_id="CUlMAgLt1nnsCb9-5wEQww",
    client_secret="d6Q0qATAETX5tmzGM96m9GGdcBq1DA",
    password="Magha@702",
    user_agent="testscript by u/RagingBox08",
    username="RagingBox08",
)


def getNewPost(rslash):
    # rslash = input("enter the name of the subreddit: ")
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    for submission in subreddit.new(limit=5):
        print(submission.url)
        return submission.url, subreddit.title


def getHotPost(rslash):
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    c = 0
    for submission in subreddit.hot(limit=6):
        if c == 0:
            c += 1
            continue
        print(submission.url)
        return submission.url, subreddit.title


def getTopPost(rslash):
    subreddit = reddit.subreddit(rslash)
    print(subreddit.title)
    for submission in subreddit.top(limit=10):
        print(submission.title)
        print(submission.url)
        return submission.url, subreddit.title


subreddit = reddit.subreddit('ImaginaryNetwork')
desc = subreddit.description
print(desc)
print(type(desc))


def get_categories():
    categorires = ['Characters', 'Races', 'Lands', 'Architecture',
                   'Monsters', 'Technology', 'Fandoms', 'Misc', 'Friends']
    return categorires


def get_sub_reddit():
    all_subreddit = {
        'characters': ['r/ImaginaryArchers',
                       'r/ImaginaryAssassins',
                       'r/ImaginaryAstronauts',
                       'r/ImaginaryBoners',
                       'r/ImaginaryKnights',
                       'r/ImaginaryLovers',
                       'r/ImaginaryMythology',
                       'r/ImaginaryNobles',
                       'r/ImaginaryScholars',
                       'r/ImaginarySoldiers',
                       'r/ImaginaryWarriors',
                       'r/ImaginaryWitches',
                       'r/ImaginaryWizards', ],
        'races': ['r/ImaginaryAngels',
                  'r/ImaginaryDwarves',
                  'r/ImaginaryElves',
                  'r/ImaginaryFaeries',
                  'r/ImaginaryHumans',
                  'r/ImaginaryImmortals',
                  'r/ImaginaryMerfolk',
                  'r/ImaginaryOrcs',
                  ],
        'Lands': ['r/ImaginaryBattlefields',
                  'r/ImaginaryCityscapes',
                  'r/ImaginaryHellscapes',
                  'r/ImaginaryMindscapes',
                  'r/ImaginaryPathways',
                  'r/ImaginarySeascapes',
                  'r/ImaginarySkyscapes',
                  'r/ImaginaryStarscapes',
                  'r/ImaginaryWastelands',
                  'r/ImaginaryWeather',
                  'r/ImaginaryWildlands',
                  'r/ImaginaryWorlds', ],
        'Architecture': ['r/ImaginaryArchitecture',
                         'r/ImaginaryCastles',
                         'r/ImaginaryDwellings',
                         'r/ImaginaryInteriors',
                         'r/ImaginaryLibraries', ],
        'Monsters': ['r/ImaginaryBeasts',
                     'r/ImaginaryBehemoths',
                     'r/ImaginaryCarnage',
                     'r/ImaginaryDemons',
                     'r/ImaginaryDragons',
                     'r/ImaginaryElementals',
                     'r/ImaginaryHorrors',
                     'r/ImaginaryHybrids',
                     'r/ImaginaryLeviathans',
                     'r/ImaginaryMonsterGirls',
                     'r/ImaginaryUndead',
                     'r/ImaginaryWorldEaters', ],
        'Technology': ['r/ImaginaryArmor',
                       'r/ImaginaryCybernetics',
                       'r/ImaginaryCyberpunk',
                       'r/ImaginaryFutureWar',
                       'r/ImaginaryFuturism',
                       'r/ImaginaryMechs',
                       'r/ImaginaryPortals',
                       'r/ImaginaryRobotics',
                       'r/ImaginaryStarships',
                       'r/ImaginarySteampunk',
                       'r/ImaginaryVehicles',
                       'r/ImaginaryWarships',
                       'r/ImaginaryWeaponry', ],
        'Fandoms': ['r/ImaginaryAzeroth',
                    'r/ImaginaryDarkSouls',
                    'r/ImaginaryFallout',
                    'r/ImaginaryJedi',
                    'r/ImaginaryKanto',
                    'r/ImaginaryMarvel',
                    'r/ImaginaryMiddleEarth',
                    'r/ImaginaryNecronomicon',
                    'r/ImaginaryOverwatch',
                    'r/ImaginaryTamriel',
                    'r/ImaginaryWarhammer',
                    'r/ImaginaryWesteros',
                    'r/ImaginaryWitcher', ],
        'Misc': ['r/ImaginaryNetwork',
                 'r/ImaginaryBestOf',
                 'r/ImaginaryAww',
                 'r/ImaginaryColorscapes',
                 'r/ImaginaryFeels',
                 'r/ImaginaryMaps',
                 'r/ImaginaryUnofficial',
                 'r/ImaginaryPets',
                 'r/ImaginarySliceOfLife',
                 'r/ImaginaryTurtleWorlds',
                 'r/ImaginaryWTF', ],
        'Friends': ['r/AdorableDragons',
                    'r/AlternativeArt',
                    'r/ApocalypsePorn',
                    'r/ArmoredWomen',
                    'r/ArtPorn',
                    'r/BadAssDragons',
                    'r/ImpracticalArmour',
                    'r/INEGentlemanBoners',
                    'r/Isometric',
                    'r/Moescape',
                    'r/mtgporn',
                    'r/PopArtNouveau',
                    'r/Pulp',
                    'r/Raining',
                    'r/ReasonableFantasy',
                    'r/SpecArt',
                    'r/StarshipPorn',
                    'r/SuperStructures',
                    'r/SympatheticMonsters',
                    'r/UnusualArt',
                    'r/Wallpapers',
                    'r/ZodiacArt', ],
    }

# print(reddit.user.me())
