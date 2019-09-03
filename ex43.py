from sys import exit 
from random import randint	

class Scene(object):
   
    def enter(self):
        print "This scene is not yet configured. sub-class it and implent enter()."
        exit(1)
        
class Engine(object): 

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        
        while True:
            print "\n------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene): 
    quips = [
    "You died, you kinda suck at this.",
    "Your mom would be proud...if she were smarter.",
    "Such a luser.",
    "I have a small puppy that's better at this."
    ]
    
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print "The Gothon of Planet Percal #25 have invaded your ship and destroyed"
        print "your entire crew. You're the las surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory,"
        print "put it in the bridge and blow the ship up after getting into an"
        print "escape pod." 
        print "\n"
        print "You're running down the central corridor to the Weapons Armory when" 
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "descriptioon end"
        print "Armory and about to pul a weopton to blast you."
        
        action =  raw_input("--->")
        
        if action == "shoot":
            print "Long Descript"
            return 'death'
        elif action == "dodge":
            print "Long Descript" 
            return 'death' 
        elif action == "tell a joke":
            print "descript"
            return  'laser_weapon_armory'
        else: 
            print "DOES NOT COMPUTE"
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    
    def enter(self):
        
        print "Long Descript"
        print "You get to a door that has a 3 digit pin"
        code = "%s%s%s" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("Pin:")
        guesses = 0 
        
        if  guess == "999":
            print 'Cheating scumbag'
            return 'the_bridge'
        else:  
            while guess != code and guesses < 10:
                print "Wrooong Numbaaaa"
                guesses += 1 
                guess = raw_input("Pin:")
           
            if guess == code or guess == "999":
                print "Good Job Buddy"  
                return 'the_bridge'
        
            else: 
                print "You sir are a moron the lock is now closed "
                return 'death'
            
class TheBridge(Scene):

    def enter(self):
        
        print "Descript"
        print "Question"
        
        place = raw_input("---->")
    
        if place == "throw the bomb":
            print "You\'re an idiot" 
            return 'death'
        
        elif place == 'place it':
            print "you place it and dash past while he grabs" 
            return 'escape_pod'
            
        else: 
            print "DOES NOT compute"
            return 'the_bridge'

class EscapePod(Scene):
    
    def enter(self):
        print "You enter room there are 10 escape pod's" 
        print "Which do you choose" 
        
        pod = raw_input("--->")
        right_pod = randint(1,10)
        
        if int(pod) == right_pod:
            print "You win ya mad man"
            return 'finished'
        
        else:
            print "Well ya fucked it right at the end"
            return 'death'
            
            
class Map(object):

    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death()
    }
           
    def __init__(self, start_scene):
        self.start_scene = start_scene 
    
    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


        
        

    
    
          
        