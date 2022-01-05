Context

This dataset contains information on all 802 Pokemon from all Seven Generations of Pokemon. The information contained in this dataset include Base Stats, Performance against Other Types, Height, Weight, Classification, Egg Steps, Experience Points, Abilities, etc. The information was scraped from http://serebii.net/

Content

    abilities: A stringified list of abilities that the Pokemon is capable of having
    against_?: Eighteen features that denote the amount of damage taken against an attack of a particular type
    attack: The Base Attack of the Pokemon
    baseeggsteps: The number of steps required to hatch an egg of the Pokemon
    base_happiness: Base Happiness of the Pokemon
    capture_rate: Capture Rate of the Pokemon
    classification: The Classification of the Pokemon as described by the Sun and Moon Pokedex
    defense: The Base Defense of the Pokemon
    experience_growth: The Experience Growth of the Pokemon
    generation: The numbered generation which the Pokemon was first introduced
    height_m: Height of the Pokemon in metres
    hp: The Base HP of the Pokemon
    is_legendary: Denotes if the Pokemon is legendary.
    japanese_name: The Original Japanese name of the Pokemon
    name: The English name of the Pokemon
    percentage_male: The percentage of the species that are male. Blank if the Pokemon is genderless.
    pokedex_number: The entry number of the Pokemon in the National Pokedex
    sp_attack: The Base Special Attack of the Pokemon
    sp_defense: The Base Special Defense of the Pokemon
    speed: The Base Speed of the Pokemon
    type1: The Primary Type of the Pokemon
    type2: The Secondary Type of the Pokemon
    weight_kg: The Weight of the Pokemon in kilograms

Inspiration

Pokemon holds a very special place in my heart as it is probably the only video game I have judiciously followed for more than 10 years. With this dataset, I wanted to be able to answer the following questions:

    Is it possible to build a classifier to identify legendary Pokemon?
    How does height and weight of a Pokemon correlate with its various base stats?
    What factors influence the Experience Growth and Egg Steps? Are these quantities correlated?
    Which type is the strongest overall? Which is the weakest?
    Which type is the most likely to be a legendary Pokemon?
    Can you build a Pokemon dream team? A team of 6 Pokemon that inflicts the most damage while remaining relatively impervious to any other team of 6 Pokemon.

