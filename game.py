from time import sleep
from random import choice

#make sure phase escalations are indicated by host talk

def main():
    basement_found = False
    exit_found = False
    dead = False
    picture_found = False
    perfume_gone = False
    safe_open = False
    phase = 0
    stage = 1
    inventory = ['phone']
    visited_rooms = ['entrance hall']
    locations1 = ['laundry room', 'hallway', 'kitchen', 'bathroom', 'reading room']
    locations2 = ['living room', 'dining room', 'bedroom']
    current_location = 'the entrance hall'
    get_character()
    print_narrator('...')
    input('>>> Press enter to continue.')
    print_narrator('Your eyes slowly adjust. You\'re in an entrance hall.\nBehind you is a redwood door. It\'s locked.\nIt\'s too dark to see any further down the hall.\nYou take out your phone. You have no service here, but the flashlight still works.\nYou turn it on and shine it down the hall. You can make out a few doors.')
    while exit_found == False:
        if dead == True:
            print_narrator('It\'s getting colder.\nYou feel your heart slowing.\nIt\'s..dark...again.\nSweet darkness. I\'m home.\n...\n...')
            input('>>> ')
            print_host('At last, we can be together forever, my love.')
            input('>>> ')
            print_narrator('The end?')
            break
        if locations1 == []:
            stage = 2
        choice = standard_options(phase)
        if choice == '1':
            print_narrator('...')
            current_location = move(current_location, visited_rooms)
            if current_location == 'bedroom':
                inventory, picture_found = return_bedroom(inventory, picture_found)
            elif current_location == 'living room':
                inventory = return_living(inventory)
            elif current_location == 'dining room':
                return_dining()
            elif current_location == 'laundry room':
                inventory, safe_open = return_laundry(inventory, safe_open)
            elif current_location == 'bathroom':
                inventory, phase, perfume_gone, dead = return_bathroom(inventory, phase, perfume_gone, dead)
            elif current_location == 'kitchen':
                inventory, phase = return_kitchen(inventory, phase)
            elif current_location == 'reading room':
                inventory, visited_rooms, phase, basement_found, exit_found = return_reading(inventory, visited_rooms, phase, basement_found, exit_found)
            elif current_location == 'basement':
                inventory, phase, exit_found = return_basement(inventory, phase, exit_found)
            elif current_location == 'entrance hall':
                inventory = return_entrance(inventory)
            else:
                pass
        elif choice == '2':
            print_narrator('...')
            if stage == 1:
                locations1, current_location, phase, inventory, basement_found, picture_found, perfume_gone, dead = explore1(locations1, phase, inventory, basement_found, picture_found, perfume_gone, dead)
                visited_rooms.append(current_location)
            elif stage == 2:
                locations2, current_location, phase, inventory, basement_found, picture_found, perfume_gone, dead = explore2(locations2, phase, inventory, basement_found, picture_found, perfume_gone, dead)
                visited_rooms.append(current_location)
        elif choice == '3':
            print_narrator('...')
            check_inventory(inventory)
        elif choice == '4':
            talk(phase)
        else:
            print_narrator('Choose a valid option.')
            pass
    if exit_found == True:
        print_narrator('Do you want to leave? Y/N')
        choice = input('>>> ')
        if choice.strip() == 'Y':
            print_host('Leavlng aGa!n/////?\n......................\n.........................\ng............bye.\n\n\n\n\n\n\n\n\nEnd.')
        elif choice.strip() == 'N':
            standard_options()
        else:
            print_narrator('Do you want to leave? Y/N')
            choice = input('>>> ')

#Prints text slowly in red.
def print_host(text):
    for x in text:
        print("\033[31m", x, end='', sep='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.04)
    print() # go to new line

#Prints text slowly in white.
def print_narrator(text):
    for x in text:
        print("\033[37m", x, end='', sep='', flush=True)  # print one character, no new line, flush buffer
        sleep(0.04)
    print()

#Starts game. Gets character name.
def get_character():
    intro = f'You open your eyes.\nYou\'re laying in the fetal position on what feels like hardwood.\nIt\'s cold and dark. You can feel a draft.\nWhere am I?\nWho am I?\n...'
    print_narrator(intro)
    character = input('Enter your name:\n>>> ')
    print_host(f'...\nHello, {character}. Welcome home.\nThe place never felt the same without you.\nPlease don\'t leave me again.')
    return character

#The action options given throughout the game.
def standard_options(phase):
    if phase <= 1:
        print_narrator('...\nSelect an option:\n1 - Move to an already explored room.\n2 - Explore a new room.\n3 - Check inventory.\n4 - Talk.')
        choice = input('>>> ')
    elif phase == 2:
        print_narrator('...\nSeLect an option.\n1 - Move to an aiready explored room.\n2 - explore a new rooM.\n3 - che<k inventory.\n4 - talk.')
        choice = input('>>> ')
    else:
        print_narrator('...\n.e...t a- -p..on.\n.......................')
        print_host('?\n........\n1 - die\n2 - die\n3 - die\n4 - die')
        choice = input('>>> ')
    return choice

#Code run when standard options 1 is chosen.
def move(loc, visited):
    print_narrator(f'You are in the {loc}.')
    if len(visited) > 1:
        visited_str = ", ".join(visited[:-1]) + ' and ' + ''.join(visited[-1])
        print_narrator(f'You have visited the {visited_str}.')
    elif len(visited) == 1:
        visited_str = ''.join(visited)
        print_narrator(f'You have visited the {visited_str}.')
    move_to = input(f'Where do you want to move?\n>>> ')
    if move_to in visited:
        loc = move_to
        print_narrator(f'You go back to the {loc}.')
        return loc
    else:
        print_narrator(f'You are in the {loc}.')
        return loc

#code run when standard options 2 is chosen. This happens in game stage 1
def explore1(locations, phase, inventory, basement_found, picture_found, perfume_gone, dead):
    end_location = choice(locations)
    if end_location == 'laundry room':
        print_narrator('You enter the laundry room. Everything is covered in dust.\nThere is a washing machine, a dryer and a card table with nothing on it.\nThere are some cabinets on the wall.')
        input('>>> ')
        print_narrator('You open the cabinets.\nThey\'re all empty except for one. It has a metal safe.\nYou try to open it, but it\'s locked and you don\'t see a key nearby.')
        locations.remove('laundry room')
        input('>>> ')
    elif end_location == 'hallway':
        print_narrator('You look around the hallway.\nThere are nails in the wall where pictures used to hang, but there are no pictures.\nThe walls are bare.')
        locations.remove('hallway')
        input('>>> ')
    elif end_location == 'kitchen':
        print_narrator('You enter the small kitchen.\nThere are a few empty cupboards, dusty countertops and a stove with four burners.\nOddly, the stove top seem to be covered in ash.')
        search_kitchen = input('Search? Y/N\n>>> ')
        if search_kitchen == 'Y':
            if phase <= 1:
                print_host('There\'s nothing here. Go somewhere else.')
                print_narrator('...')
                keep_searching = input('Keep searching? Y/N\n>>> ')
                if keep_searching == 'Y':
                    print_narrator('You look around, investigating the cupboards, dusting off surfaces,\neven sifting through the ash. You don\'t find anything.')
                    print_host('I told you to stop!')
                    phase +=1
                else:
                    pass
            elif phase == 2:
                print_host('theRe*s n0thing herE. go SomewHere e1se.')
                print_narrator('...')
                keep_searching = input('Keep searching? Y/N\n>>> ')
                if keep_searching == 'Y':
                    print_narrator('You look around, investigating the cupboards, dusting off surfaces,\neven sifting through the ash. You don\'t find anything.')
                    print_host('i s@id st0p!')
                    phase +=1
                else:
                    pass
            elif phase == 3:
                print_host('n0...ng h.*e. -- $om.--re e.*e.')
                print_narrator('...')
                keep_searching = input('Keep searching? Y/N\>>> ')
                if keep_searching == 'Y':
                    print_narrator('You look around, investigating the cupboards, dusting off surfaces,\neven sifting through the ash. You don\'t find anything.')
                    print_host('..di.')
                    phase +=1
                else:
                    pass
        else:
            pass
        locations.remove('kitchen')
        print_narrator('...')
        input('>>> ')
    elif end_location == 'bathroom':
        print_narrator('You enter the bathroom.\nThe shower curtain rod has fallen sideways into the empty tub.\nAbove the sink is a cracked mirror and beside it is a small cabinet.\n')
        look = input('Look into the mirror? Y/N\n>>> ')
        if look == 'Y':
            print_narrator('You look into the mirror and see your fractured reflection.')
            print_host('Just as beautiful as I remember you.')
        else: 
            print_narrator('You avoid looking in the mirror as you explore the room.')
        print_narrator('...')
        search = input('Search cabinet? Y/N\n>>> ')
        if search == 'Y':
            print_narrator('You open the cabinet and find a small rectangular glass bottle full of clear liquid.\nSelect an option:\n1-put it in your bag\n2-open it and sniff\n3-pour it down the drain\n4-drink it')
            bottle = input('>>> ')
            if bottle == '1':
                print_narrator('It looks like perfume. You put the bottle in your bag.')
                inventory.append('perfume')
            elif bottle == '2':
                print_narrator('You open the bottle and sniff it.\nIt\'s a sweet smelling perfume. It smells good.\nYou lean against the sink and breathe it in deeply.\nYou feel yourself sliding to the floor.')
                input('>>> ')
                print_narrator('You feel a warm, safe presence.\nYour eyes are closed, but that\'s okay.\nYou trust this person completely.\nYou always have.')
                print_host('Are you ready to be with me forever? Y/N')
                forever = input('>>> ')
                if forever == 'Y':
                    dead = True
                elif forever == 'N':
                    print_narrator('It takes so much effort, but you manage to shake your head and open your eyes.\nYou are on the floor of the bathroom. The bottle of perfume is gone.')
                    perfume_gone = True
                else:
                    print_narrator('You ignore the voice and open your eyes.\nYou are on the floor of the bathroom. The bottle of perfume is in your hand.\nYou put it in your bag.')
                    inventory.append('perfume')
            elif bottle == '3':
                print_narrator('You open the bottle and tip the contents into the sink.')
                if phase <= 1:
                    print_host('What are you doing? Stop!')
                elif phase == 2:
                    print_host('whAt @re you d0ing? STO-!')
                elif phase >= 3:
                    print_host('.h.t @-e y*u do1.g? S---!')
                phase +=1
                print_narrator('The bottle is empty. You leave it on the counter.')
                perfume_gone = True
            elif bottle == '4':
                print_narrator('You open the bottle and bring it to your lips.\nThere is an overwhelmingly strong sweet smell as you down it in one go.\nThe world starts to turn black.')
                dead = True
        else:
            pass
        locations.remove('bathroom')
        input('>>> ')
    elif end_location == 'reading room':
        print_narrator('You enter the reading room. The walls are lined with empty shelves.\nThere is an armchair and a small table near a frosted glass window.\nA dark grey rug covers the floor.')
        input('>>> ')
        print_narrator('You look around the room.\nAs you walk around, you notice that your footsteps feel hollow near the center of the room.\nYou pull back the rug and find a trapdoor with a small, narrow hole in the center.\nYou try to open the door, but you can\'t get a grasp on the edges and\n you don\'t have enough leverage if you try to pull using the hole.')
        basement_found = True
        locations.remove('reading room')
        input('>>> ')
    return (locations, end_location, phase, inventory, basement_found, picture_found, perfume_gone, dead)

#Code run when standard options 2 is chosen. This happens in game stage 2
def explore2(locations, phase, inventory, basement_found, picture_found, perfume_gone, dead):
    if locations == []:
        print_narrator('There are no more new rooms to explore.')
        input('>>> ')
        return locations, end_location, phase, inventory, basement_found, picture_found, perfume_gone, dead
    end_location = choice(locations)
    if end_location == 'living room':
        print_narrator('You enter the living room.\nThere\'s a shattered glass coffee table, an upright piano that is no longer upright,\nand a couch with slashed cushions and stuffing pouring out.\nEverything is covered in a thick layer of dust.')
        search = input('Search? Y/N\n>>> ')
        if search == 'Y':
            print_narrator('Gingerly avoiding the broken glass, you move towards the couch.\nAs your footsteps clear the dust, you notice a spot of carpet that is dark, matted brown.\nYou walk around that spot, reach into the stuffing of the couch and find a key.\nYou put it in your bag.')
            inventory.append('key')
        locations.remove('living room')
        input('>>> ')
    elif end_location == 'dining room':
        print_narrator('You enter the dining room.\nThere is a blinding flash and everything goes dark.\nYou fall to the floor.')
        input('...\n>>> ')
        print_host('Wake up.')
        print_narrator('You open your eyes and see red.')
        input('...\n>>> ')
        if phase <= 1:
            print_host('Leave this room.')
        elif phase == 2:
            print_host('GeT 0ut!')
        elif phase == 3:
            print_host('... ...t!')
        input('>>> ')
        print_narrator('...\nYou wipe the blood out of your eyes and look around.\nEverything remaining in the diningroom is charred and blackened,\nbut you notice a torn piece of paper buried in the ashes.')
        print_host('DON\'T LOOK AT THAT!')
        print_narrator('Read?')
        read = input('Y/N\n>>> ')
        if read == 'Y':
            print_narrator('...\nThe paper bursts into flames in your hand, but before it burns away,\nyour eye catches three words: \"...of both parties:\"\n...')
            print_host('N0|-|')
            phase +=1
        else:
            print_narrator('...\nThe paper bursts into flames in your hand and burns away.\n...')
        locations.remove('dining room')
        print_narrator('...')
        input('>>> ')
    elif end_location == 'bedroom': 
        print_narrator('You enter the bedroom.\nThere is a neatly made king sized bed with a silver and black duvet.\nA mahogany dresser stands along one wall next to a full-body mirror.\nNear a boarded up window is a writing desk.\n...')
        search_bed = input('Search bed? Y/N\n>>> ')
        if search_bed == 'Y':
            print_narrator('You run your hand under the pillows and over the duvet. You don\'t find anything.')
        else:
            pass
        search_dresser = input('Search dresser? Y/N\n>>> ')
        if search_dresser == 'Y':
            print_narrator('You open each drawer of the dresser.\nThey\'re filled with clothes.\nIn the bottom drawer, you find an old photo.\nIt\'s almost completely faded away but you think it\'s a photo of two pairs of footprints beside each other in sand.\nYou put it in your bag.')
            inventory.append('picture')
            picture_found == True
        else:
            pass
        search_desk = input('Search desk? Y/N\n>>> ')
        if search_desk == 'Y':
            print_narrator('You open each drawer of the desk.\nThey are all empty, but upon closer inspection, you see some odd pencil scratches in the top one.\nAt first they seem like random scribblings, but you stare at them, trying to figure them-')
            if phase <= 1:
                print_host('Behind you!')
                print_narrator('...')
                turn = input('Turn around? Y/N\n>>> ')
                if turn == 'Y':
                    print_narrator('You turn around.\nThere\'s a decomposing body laying on the bed.\nShe\'s wearing a moth-eaten bathrobe and her ragged hair falls around her face in greasy, dirt-covered locks.\nShe raises her head and turns to look at you.\nYou back up against the desk and feel something fall by your feet.\nYou glance down briefly to see a pocketknife.\nYou look up quickly, but the body is gone. The room is just as it was before.\nTrying to keep one eye on the bed, you reach down and pick up the pocketknife.\nIt\'s silver and has an ornately embossed \'K\' on it.\nYou put it in your bag.')
                    inventory.append('pocketknife')
                    picture_found = True
                    phase +=1
                else:
                    print_narrator('You ignore your host. You\'ve almost got it.\nJust as you notice the name hidden in the marks, you feel someone\'s breath on the back of your neck.\nYou turn and she embraces you.\nHer hands are gentle as they caress your hair and draw you close.\n\'Shh...Come with me.\' She says.')
                    fight = input('Fight? Y/N\n>>> ')
                    if fight == 'Y':
                        print_narrator('You push her off of you and that\'s when you notice the moth-eaten bathrobe she\'s wearing,\nher ragged, dirt-covered hair, and the flesh falling from her bones.\nShe stumbles away from you and tilts her head to the side, lips widening slowly into a smile.\nAnd then she disintegrates into dust.\n')
                        input('...\n>>> ')
                        phase +=1
                    else:
                        print_narrator('You close your eyes.\n...')
                        dead = True
                        input('...\n>>> ')
            elif phase == 2:
                print_host('Behlnd y0u!')
                print_narrator('...')
                turn = input('Turn around? Y/N\n>>> ')
                if turn == 'Y':
                    print_narrator('You turn around.\nThere\'s a decomposing body laying on the bed.\nShe\'s wearing a moth-eaten bathrobe and her ragged hair falls around her face in greasy, dirt-covered locks.\nShe raises her head and turns to look at you.\nYou back up against the desk and feel something fall by your feet.\nYou glance down briefly to see a pocketknife.\nYou look up quickly, but the body is gone. The room is just as it was before.\nTrying to keep one eye on the bed, you reach down and pick up the pocketknife.\nIt\'s silver and has an ornately embossed \'K\' on it.\nYou put it in your bag.')
                    inventory.append('pocketknife')
                    input('...\n>>> ')
                    phase +=1
                else:
                    print_narrator('You ignore your host. You\'ve almost got it.\nJust as you notice the name hidden in the marks, you feel someone\'s breath on the back of your neck.\nYou turn and she embraces you.\nHer hands are gentle as they caress your hair and draw you close.\n\'Shh...Come with me.\' She says.\nYou close your eyes.\n...')
                    dead = True
                    input('...\n>>> ')
            else:
                print_host('...')
                turn = input('Turn around? Y/N\n>>> ')
                if turn == 'Y':
                    print_narrator('You turn around.\nThere\'s a decomposing body laying on the bed.\nShe\'s wearing a moth-eaten bathrobe and her ragged hair falls around her face in greasy, dirt-covered locks.\nShe raises her head and turns to look at you.\nYou back up against the desk and feel something fall by your feet.\nYou glance down briefly to see a pocketknife.\nYou look up quickly, but the body is gone. The room is just as it was before.\nTrying to keep one eye on the bed, you reach down and pick up the pocketknife.\nIt\'s silver and has an ornately embossed \'K\' on it.\nYou put it in your bag.')
                    inventory.append('pocketknife')
                    print_host('...')
                else:
                    print_narrator(' You\'ve almost got it.\nJust as you notice the name hidden in the marks, you feel someone\'s breath on the back of your neck.\nYou turn and she embraces you.\nHer hands are gentle as they caress your hair and draw you close.\n\'Shh...Come with me.\' She says.\nYou close your eyes.\n...')
                    dead = True
                    input('...\n>>> ')
        locations.remove('bedroom')
    return (locations, end_location, phase, inventory, basement_found, picture_found, perfume_gone, dead)

#Code run when standard options 3 is chosen.
def check_inventory(bag):
    inventory = [x for x in bag]
    print_narrator(f'Inventory: {", ".join(inventory)}')

#Code run when standard options 4 is chosen.
def talk(phase):
    if phase <= 1:
        print_host('Doesn\'t this place remind you of better times? Y/N')
        better_times = input('>>> ')
        if better_times == 'Y':
            print_host('Me, too.')
        elif better_times == 'N':
            print_host('... Well have a look around and it will.')
        else:
            print_host('...')
    elif phase == 2:
        print_host('This place f.els like a hoMe again wlth you here. don\'T you th1nk? Y/N')
        home_again = input('>>> ')
        if home_again == 'Y':
            print_host('I kn0w. We11 be togeTher forever soOn.')
        elif home_again == 'N':
            print_host('whY is th@t?')
        else:
            print_host('...')
    elif phase == 3:
        phase3_dialogues = ['What .re you d--ng to m?', '- tho.Ght --u 1*v-- ^e', '...']
        print_host(choice(phase3_dialogues))
    else:
        phase4_dialogues = ['.-..', '0000000000.000', '------', 'die']
        print_host(choice(phase4_dialogues))

def return_entrance(inventory):
    if 'key' in inventory:
        print_narrator('You have a key in your inventory. Do you want to try to unlock the door? Y/N')
        open = input('>>> ')
        if open == 'Y':
            print_narrator('You try the key in the door, but it doesn\'t fit here.')
        else:
            pass
    else:
        print_narrator('The front door is locked.')
    input('>>> ')
    return inventory

def return_laundry(inventory, safe_open):
    if safe_open == False:
        if 'key' in inventory:
            print_narrator('You have a key in your inventory. Do you want to open the safe? Y/N')
            open = input('>>> ')
            if open == 'Y':
                print_narrator('You open the safe.\nInside is an envelope full of cash and a crowbar.\nYou put them in your bag.')
                inventory.append('envelope of cash')
                inventory.append('crowbar')
                safe_open = True
            else:
                pass
        else:
            print_narrator('There is a locked safe in this room, but you don\'t have a key for it.')
    elif safe_open == True:
        print_narrator('The room is as you left it.\nThe safe is empty.')
    return inventory, safe_open

def return_kitchen(inventory, phase):
    if 'picture' in inventory:
        print_narrator('The kitchen is as you left it and the burners are off.\nYou have a picture in your bag. Do you want to burn it? Y/N')
        burn = input('>>> ')
        if burn == 'Y':
            print_narrator('You take the picture out of your bag and turn on a burner.')
            input('>>> ')
            if phase <= 1:
                print_host('Stop that.')
            elif phase == 2:
                print_host('St0p!')
            else:
                print_host('S.0p!--!')
            print_narrator('You ignore your host and you watch the picture burn away.')
            inventory.remove('picture')
            phase +=1
        else:
            pass
    else:
        print_narrator('The kitchen is as you left it and the burners are off.\nThere is nothing for you to do here.')
    return inventory, phase

def return_hallway():
    print_narrator('The hallway hasn\'t changed.')

def return_reading(inventory, visited_rooms, phase, basement_found, exit_found):
    if basement_found == True:
        if 'crowbar' in inventory:
            print_narrator('The reading room is as you left it.\nYou have a crowbar in your bag.\nUse the crowbar to open the basement door? Y/N')
            open_door = input('>>> ')
            if open_door == 'Y':
                print_narrator('You open the door to the basement and see a set of stairs going down.\nYou feel a slight draft coming from below.')
                if phase <= 1:
                    print_host('Don\'t.')
                elif phase == 2:
                    print_host('D0n*t.')
                else:
                    print_host('.!')
                print_narrator('You ignore your host and enter the basement.\nIt\'s empty, but you see basement bulkhead doors at the other end.\nYou run to them. They are tied shut with zip-ties.')
                if 'pocketknife' in inventory:
                    print_narrator('Use the pocketknife to cut them? Y/N')
                    cut = input('>>> ')
                    if cut == 'Y':
                        exit_found = True
                        return inventory, visited_rooms, phase, basement_found, exit_found
                    else:
                        if phase <= 1:
                            print_host('Yes. Stay with me.')
                        elif phase == 2:
                            print_host('yes. sT@y w1th me.')
                        else:
                            print_host('-.die.')
                        pass
                if 'pocketknife' not in inventory:
                    print_narrator('They\'re tied tight. Better find a way to cut them.')
                    if phase <= 1:
                        print_host('Yes. Stay with me.')
                    elif phase == 2:
                        print_host('yes. sT@y w1th me.')
                    else:
                        print_host('-.die.')
                print_narrator('You leave the basement.')
                input('>>> ')
                visited_rooms.append('basement')
        else:
            print_narrator('The reading room is as you left it.\nThe basement door won\'t budge.')
    return inventory, visited_rooms, phase, basement_found, exit_found

def return_bathroom(inventory, phase, perfume_gone, dead):
    if perfume_gone == True:
        print_narrator('The room is as you left it. There is nothing more for you to do here.')
    else:
        if 'perfume' in inventory:
            print_narrator('The room is as you left it.\nYou have the bottle of perfume in your bag. Select an option:\n1-open it and sniff\n2-pour it down the drain\n3-drink it.')
            bottle = input('>>> ')
            if bottle == '1':
                print_narrator('You open the bottle and sniff it.\nIt\'s a sweet smelling perfume. It smells good.\nYou lean against the sink and breathe it in deeply.\nYou feel yourself sliding to the floor.')
                input('>>> ')
                print_narrator('You feel a warm, safe presence.\nYour eyes are closed, but that\'s okay.\nYou trust this person completely.\nYou always have.')
                print_host('Are you ready to be with me forever? Y/N')
                forever = input('>>> ')
                if forever == 'Y':
                    dead = True
                elif forever == 'N':
                    print_narrator('It takes so much effort, but you manage to shake your head and open your eyes.\nYou are on the floor of the bathroom. The bottle of perfume is gone.')
                    perfume_gone = True
                    inventory.remove('perfume')
                else:
                    print_narrator('You ignore the voice and open your eyes.\nYou are on the floor of the bathroom. The bottle of perfume is in your hand.\nYou put it back in your bag.')
            elif bottle == '2':
                print_narrator('You open the bottle and tip the contents into the sink.')
                if phase <= 1:
                    print_host('What are you doing? Stop!')
                elif phase == 2:
                    print_host('whAt @re you d0ing? STO-!')
                elif phase >= 3:
                    print_host('.h.t @-e y*u do1.g? S---!')
                phase +=1
                print_narrator('The bottle is empty. You leave it on the counter.')
                perfume_gone = True
                inventory.remove('perfume')
            elif bottle == '3':
                print_narrator('You open the bottle and bring it to your lips.\nThere is an overwhelmingly strong sweet smell as you down it in one go.\nThe world starts to turn black.')
                dead = True
        if 'perfume' not in inventory:
            print_narrator('The room is as you left it, but you never searched the cabinet.')
            search = input('Search cabinet? Y/N\n>>> ')
            if search == 'Y':
                print_narrator('You open the cabinet and find a small rectangular glass bottle full of clear liquid.\nSelect an option:\n1-put it in your bag\n2-open it and sniff\n3-pour it down the drain\n4-drink it')
                bottle = input('>>> ')
                if bottle == '1':
                    print_narrator('It looks like perfume. You put the bottle in your bag.')
                    inventory.append('perfume')
                elif bottle == '2':
                    print_narrator('You open the bottle and sniff it.\nIt\'s a sweet smelling perfume. It smells good.\nYou lean against the sink and breathe it in deeply.\nYou feel yourself sliding to the floor.')
                    input('>>> ')
                    print_narrator('You feel a warm, safe presence.\nYour eyes are closed, but that\'s okay.\nYou trust this person completely.\nYou always have.')
                    print_host('Are you ready to be with me forever? Y/N')
                    forever = input('>>> ')
                    if forever == 'Y':
                        dead = True
                    elif forever == 'N':
                        print_narrator('It takes so much effort, but you manage to shake your head and open your eyes.\nYou are on the floor of the bathroom. The bottle of perfume is gone.')
                        perfume_gone = True
                    else:
                        print_narrator('You ignore the voice and open your eyes.\nYou are on the floor of the bathroom. The bottle of perfume is in your hand.\nYou put it in your bag.')
                        inventory.append('perfume')
                elif bottle == '3':
                    print_narrator('You open the bottle and tip the contents into the sink.')
                    if phase <= 1:
                        print_host('What are you doing? Stop!')
                    elif phase == 2:
                        print_host('whAt @re you d0ing? STO-!')
                    elif phase >= 3:
                        print_host('.h.t @-e y*u do1.g? S---!')
                    phase +=1
                    print_narrator('The bottle is empty. You leave it on the counter.')
                    perfume_gone = True
                elif bottle == '4':
                    print_narrator('You open the bottle and bring it to your lips.\nThere is an overwhelmingly strong sweet smell as you down it in one go.\nThe world starts to turn black.')
                    dead = True
    return inventory, phase, perfume_gone, dead

def return_bedroom(inventory, picture_found):
    if picture_found == True:
        if 'pocketknife' in inventory:
            print_narrator('The room is as you left it. You remember the pencil scratches on the desk.\nYou go back to take another look, but they\'re gone.')
        elif 'pocketknice' not in inventory:
            print_narrator('The room is as you left it. You remember the pencil scratches on the desk.\nYou go back to take another look, but they\'re gone.\nAs you close the drawer, something small and heavy falls to the floor.\nIt\'s a silver pocketknife and it has an ornately embossed \'K\' on it.\nYou put it in your bag.')
            inventory.append('pocketknife')
        input('...\n>>> ')
    elif picture_found == False:
        print_narrator('The room is as you left it. You realize you didn\'t search the dresser.')
        search = input('Search dresser? Y/N\n>>> ')
        if search == 'Y':
            print_narrator('You open each drawer of the dresser.\nThey\'re filled with clothes.\nIn the bottom drawer, you find an old photo.\nIt\'s almost completely faded away but you think it\'s a photo of two pairs of footprints beside each other in sand.\nYou put it in your bag.')
            inventory.append('picture')
            picture_found == True
        if 'pocketknife' in inventory:
            print_narrator('You remember the pencil scratches on the desk.\nYou go back to take another look, but they\'re gone.')
        elif 'pocketknice' not in inventory:
            print_narrator('You remember the pencil scratches on the desk.\nYou go back to take another look, but they\'re gone.\nAs you close the drawer, something small and heavy falls to the floor.\nIt\'s a silver pocketknife and it has an ornately embossed \'K\' on it.\nYou put it in your bag.')
            inventory.append('pocketknife')
        input('...\n>>> ')
    else:
        print_narrator('The room is as you left it. There\'s nothing else for you to do here.')
    return inventory, picture_found

def return_living(inventory):
    if 'key' in inventory:
        print_narrator('The room is as you left it with the overturned piano, broken coffee table and slashed couch.\nThis is where you found the key.')
    elif 'key' not in inventory:
        print_narrator('The room is as you left it with the overturned piano, broken coffee table and slashed couch.')
        search = input('Search? Y/N\n>>> ')
        if search == 'Y':
            print_narrator('Gingerly avoiding the broken glass, you move towards the couch.\nAs your footsteps clear the dust, you notice a spot of carpet that is dark, matted brown.\nYou walk around that spot, reach into the stuffing of the couch and find a key.\nYou put it in your bag.')
            inventory.append('key')
        input('>>> ')
    return inventory

def return_dining():
    print_narrator('Everything in the dining room has been burnt black or reduced to ash.\nIt doesn\'t feel very stable in here. Better go somewhere else.')
    input('>>> ')

def return_basement(inventory, phase, exit_found):
    if 'pocketknife' in inventory:
        print_narrator('The basement is as you left it.\nUse the pocketknife to cut the zip ties on the bulkhead doors? Y/N')
        cut = input('>>> ')
        if cut == 'Y':
            exit_found = True
            return inventory, phase, exit_found
        else:
            if phase <= 1:
                print_host('Yes. Stay with me.')
            elif phase == 2:
                print_host('yes. sT@y w1th me.')
            else:
                print_host('-.die.')
                pass
    elif 'pocketknife' not in inventory:
        print_narrator('The basement is as you left it.\nThe zip ties are tied tight. Better find a way to cut them.')
        if phase <= 1:
            print_host('Yes. Stay with me.')
        elif phase == 2:
            print_host('yes. sT@y w1th me.')
        else:
            print_host('-.die.')
        print_narrator('You leave the basement.')
        input('>>> ')
    return inventory, phase, exit_found

if __name__ == '__main__':
    main()