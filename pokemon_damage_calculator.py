def calculate_damage(your_type, opponent_type, attack, defense):
    types = {
        1: 'fire',
        2: 'water',
        3: 'grass',
        4: 'electric'
    }
    effectiveness = {
        'super_effective': 2,
        'neutral': 1,
        'not_very_effective': 0.5,
     } 
    if your_type == opponent_type:
         effective = effectiveness['not_very_effective']
    elif your_type == types[1] and opponent_type == types[2]:
         effective = effectiveness['not_very_effective']
    elif your_type == types[1] and opponent_type == types[3]:
         effective = effectiveness['super_effective']
    elif your_type == types[1] and opponent_type == types[4]:
         effective = effectiveness['neutral']
    elif your_type == types[2] and opponent_type == types[1]:
         effective = effectiveness['super_effective']
    elif your_type == types[2] and opponent_type == types[3]:
         effective = effectiveness['not_very_effective']
    elif your_type == types[2] and opponent_type == types[4]:
         effective = effectiveness['not_very_effective']
    elif your_type == types[3] and opponent_type == types[1]:
         effective = effectiveness['not_very_effective']
    elif your_type == types[3] and opponent_type == types[2]:
         effective = effectiveness['super_effective']
    elif your_type == types[3] and opponent_type == types[4]:
         effective = effectiveness['neutral']
    elif your_type == types[4] and opponent_type == types[1]:
         effective = effectiveness['neutral']
    elif your_type == types[4] and opponent_type == types[2]:
         effective = effectiveness['super_effective']
    elif your_type == types[4] and opponent_type == types[3]:
         effective = effectiveness['neutral']
    return 50 * (attack/defense) * effective
