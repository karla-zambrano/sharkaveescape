define f = Character("Finn")
define o = Character("Dr. Octopun")
define u = Character("???")
define m = Character("Mom")

label start:
    scene r1_shipwreck
    f "I've found the famous shipwreck near Miami"
    f "It's my lifelong dream. I really did it. Billy the Marlin will be sooo jealous" #animate "sooo" if possible
    "..."
    scene r1_shipwreck with hpunch 
    scene r1_shipwreck with vpunch
    scene r2_morsecodecave with vpunch
    f "Ouch, I fell through the bottom! ):<"
    f "A huge rock blocked my path out of here. I should find an exit."
    f "Those are weird scratches... What kind of animal could've done that?"
    f "Let's keep moving, Finn. I think there's an entrance here, maybe i'll find treasure!"
    jump paths


label paths: 
    default visitedlightroom = False
    scene r3_lightordark with fade
    f "Huh... the path splits up here."
    if visitedlightroom == False:
      scene r3_lightordark with vpunch
      f "EEEEE! Is that light I see?! I think that could be my exit." #if we have time, slow down vpunch
      menu: 
        "Go left towards the light":
          jump lightroom
        "Go right towards the dark":
          jump darkroom
    else: 
      menu: 
        "Go right towards the dark":
          jump darkroom


label lightroom:
    scene r4_skeleton with fade
    f "AH!" with vpunch
    f "That sent a chill down my spine."
    f "Oh, my! You have a deadly grip on this. It must be important"
    menu:
       "Snatch the paper from the dead man.":
        scene deadmansnote with fade
        f "Re-morse...some sort of code."
        
        menu:
          "Put note down":
            scene r4_skeleton with fade  
            $ visitedlightroom = True
            jump paths
     
   
label darkroom:
  scene r5_stuckrock with fade
  if visitedlightroom == False:
    f "Ugh. A boulder is blocking my path. What should I do? Think, Finn. Think!"
    menu:
        "Go back":
          jump paths
  else:
    jump rockpuzzle

label rockpuzzle:
  f "I think I know what to do now!"
# this is where i put the number puzzle
  $ input = renpy.input("How many rocks should i put here?","",allow="1,2,3,4,5,6,7,8,9,10")
  $ rocksinput = int(input)
  if rocksinput == 8:
    scene r5_stuckrock with vpunch
    "Finn put 8 rocks and the path opened"
    f "Aha! That's solid alright"
    jump octoroom
  else: 
    "That didnt work..."
    jump rockpuzzle

label octoroom:
  scene r6_droctopun with fade
  show dr
  o "Oh-oh! It's nice to fin-ally meet you here!"
  scene r6_droctopun with vpunch
  show dr
  f "ACK!"
  f "Who are you?!"
  o "Well, well. I'm glad you asked, 'cause Dr. Octopun is here to help you with this task"
  f "Is this another puzzle?"
  o "My, aren't you jaw-some! Yes, I'll give you all my sea-crets if you can solve this puzzle:"
  jump octopuzzle

label octopuzzle:
  show dr
  $ input = renpy.input(" How many tickles does it take to make an octopus laugh? ","")
  $ puzzleans = str(input)
  if puzzleans == 'ten-tickles':
    o"Fin-tastic! You got it right!"
    hide dr
    # hide o
    "Dr. Octopun disappeared into thin air... That was weird."
    jump elevator
  else:
     o "Don't be salty, but... You got it wrong."
     o "Would you like to try again?"
     menu:
      "Try again":
        jump octopuzzle

label elevator:
  scene r7_elevator with fade
  f "What... is this?"
  "Finn thinks really hard, it suddenly hits him."
  f "Huh?! This is an elevator?" #right here
  jump elevatorpaths

label elevatorpaths:
  scene r7_elevator
  default visiteddownroom = False #might put this ^
  menu:
    "Go up.":
      jump uproom
    "Go down.":
      jump downroom

label uproom:
  scene r8_passcode with fade
  f "...Another door? What is happening here??"
  if visiteddownroom == True:
    scene closeuppass with fade
    $ input = renpy.input("What is the 4 digit passcode?","")
    $ passcode = str(input)
    if passcode == '1285':
      "Access Granted"
      f "Fin-ally!"
      jump classroom
    else:
      "Incorrect Passcode"
      menu:
        "Try Again":
          jump uproom
  else:
    f "I couldn't possibly know the answer yet. I better get to the bottom of this."
    menu:
      "Go back to elevator":
        jump elevatorpaths


label downroom:
  scene r9_kitchen with fade
  f "Wha- Where am i? Did I make it out?"
  f "The walls.. the floor... They're wet. This doesn't look right."
  "..."
  f "Is that-"
  scene failedtest with vpunch
  f "I failed my final?! But I was going to graduate this semester! Oh no." with vpunch
  f "No. No. No. No. No. No. No. No. No. No. No. No. No. No. No. No. No. No." with hpunch
  f "I need to leave." with vpunch
  $ visiteddownroom = True
  menu:
    "Go back up":
      jump elevatorpaths
  
label classroom:
  scene r10_classroom with fade
  f "Huh?! What?!" with vpunch
  f "This... This doesn't make sense." with hpunch
  f "I don't understand." with vpunch
  f "What is happening? There's no way..." with hpunch
  f "THERE'S NO WAY I FAILED THIS CLASS!" with vpunch
  f "I NEED to leave." with hpunch
  menu:
    "Leave IMMEDIATELY":
      jump hospital

label hospital:  
  scene whitehospital with fade
  u "Finn?? Finn?! Honey, can you hear me?"
  "..."
  u "Doctor, I think he's finally woken up! Doctor!"
  scene r11_hospital with fade
  f "M-Mom?"
  m "Oh thank goodness! Finn, you're awake! Oh, Finn!"
  f "W-What's going on?"
  m "You- (hick) You dont remember?"
  m "Honey, you collapsed."
  f "Huh?"
  m "Oh, I should've seen this coming. Your thesis... It was so important to you..."
  m "You didn't eat or sleep for days... I found you unconcious near our kitchen"
  "..."
  m"I'm such a failure. I let you get this bad. I should've noticed"
  m"I love you, my little Finn. I'm still proud of you no matter what."
   

return
