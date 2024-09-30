# Spaceship
Spaceship battle themed deckbuilder


# TODO:
- Extract repeating code for game objects into mixins:
    - draw
        - image
        - position
        - size
        - fill
        - collision
    - mouse_click
    - mouse_move
        - hold
        - move (while held)
        - unhold
    - ? include_text
        - font
        - fill
        - rel_position
        - ? title
    - event(s)
        - action(s)
- Generalise containers and game objects
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