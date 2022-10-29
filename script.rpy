define f = Character("Finn")
define o = Character("Dr. Octopun")

label start:

    scene shipwreck
    f "I've found the famous shipwreck near Miami"
    f "It's my lifelong dream. I really did it."
    "..."
    scene shipwreck with hpunch 
    scene shipwreck with vpunch
  
    scene morsecodecave with vpunch
    f "Ouch, I fell through the bottom ):<"
    f "Those are weird scratches... What kind of animal could've done that?"
    f "I should keep moving"
   # //scene morsecodecave with ?? something to make it beat or pulse
   # f "I feel like the walls are closing in. Am I suffocating?"
    
menu: 
  "Go left towards the light":
    jump leftroom
  "Go right towards the dark":
    jump rightroom

label leftroom:
  scene litcaveroom with fade
  "The outside looks so close but out of reach."
  f "Theres nothing else for me here."
  menu rechooseroom:
    "Go back to other room":
      jump rightroom
     
   
    

label rightroom:
  scene deadmanroom with fade
  f "AH!" with vpunch
  f "What is he holding?"
  menu:
    "Grab what hes holding":
      jump readdeadmansnote

label readdeadmansnote:
  scene deadmansnote with fade
  f "Re-morse...some sort of code."
  menu:
    "Put note down":
      scene  deadmanroom with fade












    

return