import random

print('Hi, I am a Haiku Generator.')

# Define Haikus for different moods
haikus = {
    'LOVE': [
        "Whispers of the heart,\nA gentle touch of pure love,\nIn soft moonlight's glow.",
        "Two souls intertwined,\nLove blossoms in silent gaze,\nHearts beating as one.",
        "In your warm embrace,\nThe world fades, just you and me,\nLove's eternal flame."
    ],
    'ANGER': [
        "Storms rage deep within,\nLightning flashes in my eyes,\nFury, uncontained.",
        "Clenched fists, boiling blood,\nWords sharp as a double edge,\nAnger burns inside.",
        "Volcano erupts,\nMolten lava flows through veins,\nAnger takes its toll."
    ],
    'NATURE': [
        "Gentle breeze whispers,\nLeaves dance in the golden sun,\nNature's song of peace.",
        "Mountains kiss the sky,\nRivers carve paths through valleys,\nNature's embrace calls.",
        "Cherry blossoms bloom,\nPetals fall like soft snowflakes,\nNature's fleeting grace."
    ],
    'SORROW': [
        "Tears fall like soft rain,\nMemories linger in the mist,\nSorrow's silent song.",
        "Moonlight on still lakes,\nReflects a heart, broken wide,\nSorrow's cold embrace.",
        "Lonely willow weeps,\nBranches droop with heavy tears,\nSorrow's roots run deep."
    ],
    'LONGING': [
        "Empty room echoes,\nA distant memory calls,\nLonging fills the night.",
        "Stars whisper your name,\nAcross the vast, silent sky,\nLonging for your touch.",
        "In the quiet dusk,\nShadows stretch, longing for light,\nDreams of days gone by."
    ],
    'NOSTALGIA': [
        "Faded photographs,\nYellowed with the passage time,\nNostalgia's soft touch.",
        "Old songs on the breeze,\nMemories dance in the air,\nNostalgia's embrace.",
        "Childhood summers' glow,\nEchoes of laughter linger,\nNostalgia's warm kiss."
    ],
    'REGRET': [
        "Unspoken words drift,\nLost chances whisper in dreams,\nRegret's heavy hand.",
        "Footsteps echo faint,\nPaths not taken linger on,\nRegret's silent call.",
        "Mistakes left behind,\nTime’s river flows, unyielding,\nRegret’s quiet ache."
    ],
    'FORGIVENESS': [
        "Softly spoken words,\nBridge the chasm of old wounds,\nForgiveness heals hearts.",
        "Tears of the past fade,\nHealing begins with a word,\nForgiveness sets free.",
        "A gentle embrace,\nOld grudges dissolve like mist,\nForgiveness renews."
    ]
}

while True:
    
    feeling = input('How are you feeling? Pick between the following themes: LOVE, ANGER, NATURE, SORROW, LONGING, NOSTALGIA, REGRET, FORGIVENESS (or type "quit" to exit): ').strip().upper()

    if feeling == 'QUIT':
        print('Goodbye!')
        break
    
    haiku = random.choice(haikus.get(feeling, ["Sorry, I don't have a Haiku for that theme."]))

    print("\nHere's a Haiku for you:\n")
    print(haiku)
    print()  
