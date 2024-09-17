# Spaceship
Spaceship battle themed deckbuilder

## Ideas:
- Two alternating modes of play:
    - Ship view:
        - Select path?
        - Events?
        - Assign crew members to their stations in the ship
        - Stationed crew = cards during battle
        - Crew have stats:
            - Effectiveness at various stations
            - Modifiers
            - Special effects
            - e.g. Stan is not good at weapons (-1), but great at shields (+1);
                Amy is all-rounder with the ability to handle two neibouring bridge stations at once
                Rob is a leader and improves the abilities of other crew in the room
        - Stations:
            - Bridge:
                Captain's chair
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
            - Crew quarters ?
            - Brig:
                - Convert beaten spaceships into additional crew?
            - Flight deck:
                - Fighters (Additional attacks)
            - Transporters:
                - Reassign crew?
    - Spaceship battle:
        - Turn based
        - Card selection to perform actions
- Mecahnics to consider:
    - Mana system?
    - Kinds of cards available
    - Kinds of events
    - Customisation of ship - what kinds of options should this provide?
    - Consider mechanics from Artemis (science, navigation, engineering, medical, bridge, fighters, comms, escape pods, weapons, teleporters, storage/loading bay, brig, sleeping quarters)

# TODO:
- Check that items are currently being rendered!
    - Capture boilerplate for draw, collidepoint, etc
    - How to move things in and out of current view for both events and rendering?
- Create basic ship view:
    - Ship cross-section (with clear bounds of each room)
    - Crew allocation to each area
- Create basic battle view:
    - Cards:
        - Library / discard
        - Hand
        - Card selection
    - HUD:
        - Ships
        - Mana
        - Health
        - Intention?
    - Basic effects:
        - Targeting