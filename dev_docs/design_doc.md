# Spaceship

## Dev design writing tips
- Be concise
- Be specific (use numbers and diagrams)
- Describe what is known, note what is not

## Description
A spaceship themed deckbuilder.
Each crew member has their own strengths and weaknesses.
Each station within the ship has its own effect type. Mix and match crew members with ship stations to build your deck.

## Dev goal(s)
This game is purely a learning experience. I enjoy deckbuilders and thought that the idea of the player having some ability to min/max their deck building choices via crew placement seemed like a fun experience.
My initial goal is to have the crew placement and card battle mechanics playable. From there, I will see about extending the game to include events, maybe some kind of star map and then variety to all of the core elements.
The core philosophy in this process is making a game that I find fun.


## Unique selling point(s)
The interaction of placing crew at their stations gives a new take on creating a deck.

## Player experience and game POV
- Who is the player
The player is the ship captain on an amazing new ship in the fleet.
- What is the setting
Sci-fi, space exploration and battles
- What is the fantasy that the game provides the player
Making choices that matter; having agency to create the deck they want, while also having enough randomness to keep things interesting and exciting
- What should the player feel
Challenged; excited at finding synergies
- What keeps the player engaged
In genreal, the puzzle like challenge of optimising the deck and play patterns enough to win a range of different battles
- Key moments / experiences at start, middle, end of game
Start: Meeting crew and assigning starting locations
Middle: Unlocking new ship locations, discovering deck synergies, meeting interesting new crew, fighting enemies with interesting fight patterns
End: Satisfying culmination to a final extra challenging boss battle


## Visual and audio style
TODO
- What is the look and feel
- How does this support the player experience
- Concept art?


## Game world fiction
TODO
- Lore
- Story arc


## Monetisation
I am not interested in monetising or even officially releasing the game at this stage. It is a hobby project.
If things go well, I may update this in future, but do not have any current plans to do so.


## Platform, technologies, scope
- Languages, frameworks etc
As I want to build on what I already know, this is built using Python. Considering that this is going to be a computationally simple game (2D; simple state management etc), Python will be well and truly fast enough to cover my cases. Having chosen the language, I went with PyGame because it is a well-established game library with a good community.
I am experimenting with design patterns based on either what I already use/know or things that I am curious to try. I am very new to this domain, so am happy to make mistakes and learn along the way.


## Core loops
- How do game objects and player actions form loops
SHIP: List of available crew ready for assignment (only on start, or each round?); assignment of crew to locations -> creation of card into decklist
BATTLE: View from bridge out window at enemy? STS side by side view?
    Turn: Perform start of turn effects, draw cards into hand; player can then play cards (and enact card effects) until choosing to end turn. Discard rest of hand and perform end of turn effects.
    Enemry turn, with same structure (other than agency)
    Repeat until either player or all enemies are dead
- Why is this engaging
Card handling feels somewhat tangible, even in computerised form. It abstracts complex interactions into a neat package that can be optimised. Optimising and working to minimise or otherwise manage the rng is fun and engaging.
- What emergent results should be found
Certain combinations of crew and ship duties can synergise to produce more powerful (if niche) cards. Combinations of cards can create deck synergies. Potential to add events that modify the ship itself to create another layer of synergy.


## Objectives and progression
- How does the player go through the game
After making the crew selections the player is happy with, they can click the button to go to the battle screen. In battle, each card is selectable and can be activated by dragging into the central play space to use. When they have used all the cards that they intend to for the turn, they can click the button to end their turn. Winning takes the player back to the ship screen
- What are the short and long term goals
Short: To win the next battle / assign crew optimally for strategy
Long: To build synergies that allow the deck to scale to be able to beat the more difficult enemies and eventually the game
- How do these relate to the concept, style and player-fantasy
- End conditions
Beat the final boss


## Game systems
- What systems are needed
Ship management:
    Crew stats
    Ship locations
    Crew-locations (card deck)
    Persistent ship stats (health)
Enemies:
    Enemy selector
    Enemy stats (health)
    Card deck
Battle HUD:
    Energy
    Health
    Enemies
    Other stats: Shields (types), weapons, effects
Cards:
    Shuffler
    Deck
    Discard pile
    Hand
        Card selection, handling, targeting, actions
Effects:
    Card actions
    Persistent effects
    Timed effects


## Interactivity
- How are different types of interaction used
Mouse only (at least at first). Click and drag to assign crew to locations; click and drag to target/activate cards; click button to end turn; click button to start battle
- What is the player doing at any given time
The game is essentially turn based, so the player can consider their action for as long as they want before clicking and moving an item or clicking a button to go to the next phase/screen.
- What do the various screen UIs look like
SHIP: Available crew listed on left
    Ship spaces drawn onto ship floorpan (Start with rect list areas at first)
    Crew can be dragged to locations to generate cards
    Created cards populate right side
    Button bottom right to BATTLE
BATTLE:
    STS layout

## Game objects
- Stats, features, story, art etc
CREW:
    - Effectiveness at various stations
    - Modifiers
    - Special effects
    - e.g. Stan is not good at weapons (-1), but great at shields (+1);
        Amy is all-rounder with the ability to handle two neibouring bridge stations at once
        Rob is a leader and improves the abilities of other crew in the room
LOCATIONS:
    - Bridge:
        Comms
    - Weapons:
        - Scttered around ship, individually manned
    - Engineering:
        - Shields?
        - Energy system for actions?
        - Resources
    - Science:
        - Info on enemy (shield type/vuln, intent)
    - Medical:
        - Crew damage?
    - Crew quarters
        - Crew shifts?
    - Brig:
        - Convert beaten spaceships into additional crew?
        - Equivalent of curses?
    - Flight deck:
        - Fighters (Additional attacks)