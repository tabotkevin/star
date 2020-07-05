
people = [
    {
        "name": "Luke Skywalker",
        "height": "172",
        "mass": "77",
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": "19BBY",
        "gender": "male",
        "created": "2014-12-09T13:50:51.644000Z",
        "edited": "2014-12-20T21:17:56.891000Z",
    },
    {
        "name": "C-3PO",
        "height": "167",
        "mass": "75",
        "hair_color": "n/a",
        "skin_color": "gold",
        "eye_color": "yellow",
        "birth_year": "112BBY",
        "gender": "n/a",
        "created": "2014-12-10T15:10:51.357000Z",
        "edited": "2014-12-20T21:17:50.309000Z",
    }
]

people_many = [
    {
        "films": [
            1,
            2
        ],
        "species": [
            1,
        ],
        "starships": [
            1,
            2
        ],
        "vehicles": [
            1,
            2
        ]
    },

    {
        "films": [
            1
        ],
        "species": [
            2
        ],
        "starships": [
            1
        ],
        "vehicles": [
            1,
            2
        ]
    }
]

planets = [
    {
        "name": "Tatooine",
        "rotation_period": "23",
        "orbital_period": "304",
        "diameter": "10465",
        "climate": "arid",
        "gravity": "1 standard",
        "terrain": "desert",
        "surface_water": "1",
        "population": "200000",
        "created": "2014-12-09T13:50:49.641000Z",
        "edited": "2014-12-20T20:58:18.411000Z",
    },
    {
        "name": "Alderaan",
        "rotation_period": "24",
        "orbital_period": "364",
        "diameter": "12500",
        "climate": "temperate",
        "gravity": "1 standard",
        "terrain": "grasslands, mountains",
        "surface_water": "40",
        "population": "2000000000",
        "created": "2014-12-10T11:35:48.479000Z",
        "edited": "2014-12-20T20:58:18.420000Z",
    }
]

planets_many = [
    {
        "residents": [
            1,
            2
        ],
        "films": [
            1
        ]
    },

    {
        "residents": [
            2
        ],
        "films": [
            1,
            2
        ]
    }
]

starships = [
    {
        "name": "CR90 corvette",
        "model": "CR90 corvette",
        "manufacturer": "Corellian Engineering Corporation",
        "cost_in_credits": "3500000",
        "length": "150",
        "max_atmosphering_speed": "950",
        "crew": "30-165",
        "passengers": "600",
        "cargo_capacity": "3000000",
        "consumables": "1 year",
        "hyperdrive_rating": "2.0",
        "MGLT": "60",
        "starship_class": "corvette",
        "created": "2014-12-10T14:20:33.369000Z",
        "edited": "2014-12-20T21:23:49.867000Z",
    },
    {
        "name": "Star Destroyer",
        "model": "Imperial I-class Star Destroyer",
        "manufacturer": "Kuat Drive Yards",
        "cost_in_credits": "150000000",
        "length": "1,600",
        "max_atmosphering_speed": "975",
        "crew": "47,060",
        "passengers": "n/a",
        "cargo_capacity": "36000000",
        "consumables": "2 years",
        "hyperdrive_rating": "2.0",
        "MGLT": "60",
        "starship_class": "Star Destroyer",
        "created": "2014-12-10T15:08:19.848000Z",
        "edited": "2014-12-20T21:23:49.870000Z",
    }
]

starships_many = [
    {
        "pilots": [
            2
        ],
        "films": [
            1,
            2
        ]
    },

    {
        "pilots": [
            1,
            2
        ],
        "films": [
            1
        ]
    }
]

films = [
    {
        "title": "A New Hope",
        "episode_id": 4,
        "opening_crawl": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....",
        "director": "George Lucas",
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": "1977-05-25",
        "created": "2014-12-10T14:23:31.880000Z",
        "edited": "2014-12-20T19:49:45.256000Z",
    },
    {
        "title": "The Empire Strikes Back",
        "episode_id": 5,
        "opening_crawl": "It is a dark time for the\r\nRebellion. Although the Death\r\nStar has been destroyed,\r\nImperial troops have driven the\r\nRebel forces from their hidden\r\nbase and pursued them across\r\nthe galaxy.\r\n\r\nEvading the dreaded Imperial\r\nStarfleet, a group of freedom\r\nfighters led by Luke Skywalker\r\nhas established a new secret\r\nbase on the remote ice world\r\nof Hoth.\r\n\r\nThe evil lord Darth Vader,\r\nobsessed with finding young\r\nSkywalker, has dispatched\r\nthousands of remote probes into\r\nthe far reaches of space....",
        "director": "Irvin Kershner",
        "producer": "Gary Kurtz, Rick McCallum",
        "release_date": "1980-05-17",
        "created": "2014-12-12T11:26:24.656000Z",
        "edited": "2014-12-15T13:07:53.386000Z",
    }
]

films_many = [
    {
        "species": [
            1,
            2
        ],
        "starships": [
            2
        ],
        "vehicles": [
            1
        ],
        "characters": [
            1
        ],
        "planets": [
            1,
            2
        ]
    },
    {
        "species": [
            1,
            2
        ],
        "starships": [
            1
        ],
        "vehicles": [
            1,
            2
        ],
        "characters": [
            1,
            2
        ],
        "planets": [
            2
        ]
    }
]

species = [
    {
        "name": "Human",
        "classification": "mammal",
        "designation": "sentient",
        "average_height": "180",
        "skin_colors": "caucasian, black, asian, hispanic",
        "hair_colors": "blonde, brown, black, red",
        "eye_colors": "brown, blue, green, hazel, grey, amber",
        "average_lifespan": "120",
        "homeworld": "9/",
        "language": "Galactic Basic",
        "created": "2014-12-10T13:52:11.567000Z",
        "edited": "2014-12-20T21:36:42.136000Z",
    },
    {
        "name": "Droid",
        "classification": "artificial",
        "designation": "sentient",
        "average_height": "n/a",
        "skin_colors": "n/a",
        "hair_colors": "n/a",
        "eye_colors": "n/a",
        "average_lifespan": "indefinite",
        "homeworld": "",
        "language": "n/a",
        "created": "2014-12-10T15:16:16.259000Z",
        "edited": "2014-12-20T21:36:42.139000Z",
    }
]

species_many = [
    {
        "people": [
            1
        ],
        "films": [
            2
        ]
    },
    {
        "people": [
            1,
            2
        ],
        "films": [
            1
        ]
    }
]

vehicles = [
    {
        "name": "Sand Crawler",
        "model": "Digger Crawler",
        "manufacturer": "Corellia Mining Corporation",
        "cost_in_credits": "150000",
        "length": "36.8 ",
        "max_atmosphering_speed": "30",
        "crew": "46",
        "passengers": "30",
        "cargo_capacity": "50000",
        "consumables": "2 months",
        "vehicle_class": "wheeled",
        "created": "2014-12-10T15:36:25.724000Z",
        "edited": "2014-12-20T21:30:21.661000Z",
    },
    {
        "name": "T-16 skyhopper",
        "model": "T-16 skyhopper",
        "manufacturer": "Incom Corporation",
        "cost_in_credits": "14500",
        "length": "10.4 ",
        "max_atmosphering_speed": "1200",
        "crew": "1",
        "passengers": "1",
        "cargo_capacity": "50",
        "consumables": "0",
        "vehicle_class": "repulsorcraft",
        "created": "2014-12-10T16:01:52.434000Z",
        "edited": "2014-12-20T21:30:21.665000Z",
    }
]


vehicles_many = [
    {
        "pilots": [
            1,
            2
        ],
        "films": [
            2
        ]
    },
    {
        "pilots": [
            1
        ],
        "films": [
            1,
            2,
        ]
    }
]
