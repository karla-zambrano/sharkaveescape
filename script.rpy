define f = Character("Finn")
define o = Character("Dr. Octopun")
def lightroom():
  label leftroom:
    scene r4_skeleton with fade
    f "AH!" with vpunch
    f "That sent a chill down my spine."
    f "Oh, my! You have a deadly grip on this. It must be important"
  menu:
    "Snatch the paper from the dead man.":
      jump readdeadmansnote
    
  label readdeadmansnote:
    scene deadmansnote with fade
    f "Re-morse...some sort of code."
    menu:
      "Put note down":
        scene r4_skeleton with fade  
        visitedlightroom = true 



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
    scene r3_lightordark with fade
    f "Huh... the path splits up here."
    if visitedlightroom == false:
      scene r3_lightordark with vpunch
      f "EEEEE! Is that light I see?! I think that could be my exit." #if we have time, slow down vpunch
      menu: 
        "Go left towards the light":
          lightroom():
        "Go right towards the dark":
          jump darkroom
    else: 
      menu: 
        "Go right towards the dark":
        jump darkroom
   
label darkroom:
  scene r5_stuckrock with fade
  if visitedlightroom == true:
    jump 
  
  menu rechooseroom:
    "Go back to other room":
      jump rightroom














    

return
