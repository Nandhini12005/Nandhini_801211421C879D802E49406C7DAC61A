'''Implement a class called player that represents a cricket player the playerclass should be have a 
method called play() which prints "the player is playing cricket.Derive a two classes,Batsman and
Bowler,from the player class. override the play()method in each derived class to print" The batsman.
is batting"and"The bowler is bowling", respectively,write a program to create subjects or both the
Batsman and bowler classes and call the play() method  for each object.'''


#define the bass class player
class player:
        def play (self):
           print("The player is playing cricket.")

#define the derived class batsman
class Batsman (player):
    def play (self):
      print("The batsman is batting.")

#define the derived class bowler
class Bowler(player):
  def play(self):
    print("the bowler is bowling.")

#create objects of batsman and bowler class
batsman = Batsman()
bowler = Bowler()

#call the play() method for each objects
batsman.play()
bowler.play()