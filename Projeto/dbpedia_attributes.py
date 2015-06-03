ATTRIBUTES = {
    'owl:Thing':[('label', ['rdfs:label']),
                 ('abstract', ['dbpedia-owl:abstract']),
                 ('website', ['foaf:homepage'])],

    'DBpedia:Person':[('birth name', ['dbpprop:birthName']),
                      ('birth date', ['dbpedia-owl:birthDate']),
                      ('birth place', ['dbpedia-owl:birthPlace', 'rdfs:label']),
                      ('death date', ['dbpedia-owl:deathDate']),
                      ('death place', ['dbpedia-owl:deathPlace', 'rdfs:label']),
                      ('profession', ['dbpedia-owl:profession', 'rdfs:label']),
                      ('spouse', ['dbpprop:spouse']),
                      ('children', ['dbpprop:children']),
                      ('residence', ['dbpedia-owl:residence', 'rdfs:label']), 
                      ('alma mater', ['dbpedia-owl:almaMater', 'rdfs:label']),
                      ('religion', ['dbpedia-owl:religion', 'rdfs:label'])],

    'DBpedia:MusicalArtist':[('genre', ['dbpedia-owl:genre', 'rdfs:label']),
                             ('instrument', ['dbpprop:instrument'])],

    'DBpedia:OfficeHolder':[('party', ['dbpedia-owl:party', 'rdfs:label'])],

    'DBpedia:Place':[('area total', ['dbpedia-owl:areaTotal']),
                     ('percentage of area water', ['dbpedia-owl:percentageOfAreaWater']),
                     ('time zone', ['dbpprop:timeZone', 'rdfs:label'])],

    'DBpedia:PopulatedPlace':[('capital', ['dbpedia-owl:capital', 'rdfs:label']),
                              ('largest city', ['dbpedia-owl:largestCity', 'rdfs:label']),
                              ('official language', ['dbpedia-owl:officialLanguage', 'rdfs:label']),
                              ('demonym', ['dbpedia-owl:demonym']),
                              ('government type', ['dbpprop:governmentType', 'rdfs:label']),
                              ('leader', ['dbpedia-owl:leader', 'rdfs:label']),
                              ('legislature', ['dbpprop:legislature', 'rdfs:label']),
                              ('population total', ['dbpedia-owl:populationTotal']),
                              ('population density', ['dbpedia-owl:populationDensity'])],

    'DBpedia:Country':[('gdp ppp total', ['dbpprop:gdpPpp']),
                       ('gdp ppp per capita', ['dbpprop:gdpPppPerCapita']),
                       ('gdp nominal total', ['dbpprop:gdpNominal']),
                       ('gdo nominal per capita', ['dbpprop:gdpNominalPerCapita']),
                       ('currency', ['dbpedia-owl:currency', 'rdfs:label']),
                       ('date format', ['dbpprop:dateFormat']),
                       ('drives on the', ['dbpprop:drivesOn'])],

    'DBpedia:Work':[('genre', ['dbpedia-owl:genre', 'rdfs:label'])],

    'DBpedia:TelevisionShow':[('composer', ['dbpedia-owl:composer', 'rdfs:label']),
                              ('country', ['dbpprop:country']),
                              ('creator', ['dbpedia-owl:creator', 'rdfs:label']),
                              ('language', ['dbpprop:language', 'rdfs:label']),
                              ('num episodes', ['dbpprop:numEpisodes']),
                              ('num seasons', ['dbpedia-owl:numberOfSeasons']),
                              ('open theme', ['dbpprop:opentheme']),
                              ('starring', ['dbpedia-owl:starring', 'rdfs:label'])]

}