import cmd
import random
import os
class CLA(cmd.Cmd):
    def preloop(self):
        self.inventory = []
        self.stats = {
         "HP":30,
         "Attack":range(3),
         "Defense":range(3)
        }
        self.locations = ["Vermid Forest","Cralis Town","Dungeon Of Knorr"]
        self.doors = []
        self.current_location = "Vermid Forest"
    prompt = ">"
    intro = "Welcome to the land of Ercas. Explore this world as you complete quests.\nMade by qkuldo. Website:qkuldo.github.io/qkuldo-website"
    def do_stats(self,line):
        print(stats)
    def do_quit(self,line):
        return True
    def do_HELP(self,line):
        print("Commands:\n stats:Shows stats\n quit:Quits game\n headto location:Go to specified location")
    def do_headto(self,location):
        if (location in self.locations and location != self.current_location):
            self.current_location = location
            print(f"You went to \033[1;31m{location}\033[1;37;40m")
        elif (not location in self.locations):
            print("That's not on the map!")
        else:
            print(f"You're already in \033[1;31m{location}\033[1;37;40m!")
game = CLA()
game.cmdloop()
