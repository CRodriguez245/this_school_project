uinput = input("Enter the type of volume you want to convert from (mL, L, floz, qt)");
uinput = uinput.lower();
ninput = float(input("How much?"));
u2input=(input("Enter the type of volume you are converting to."));
u2input = u2input.lower();
if uinput == "ml":
  if u2input == "l":
    print(ninput*.001);
  elif u2input == "floz":
    print(ninput*0.0351950797)
  elif u2input == "qt":
    print(ninput*0.0010566887)
elif uinput == "l":
  if u2input == "ml":
    print(ninput*1000)
  elif u2input == "qt":
    print(ninput*1.0566887074)
  elif u2input == "floz":
    print(ninput*33.814038638)
elif uinput == "floz":
  if u2input == "ml":
    print(ninput*29.573515625)
  elif u2input == "l":
    print(ninput*0.0295735156)
  elif u2input == "qt":
    print(ninput*0.03125)
elif uinput == "qt":
  if u2input == "ml":
    print(ninput*946.3525)
  elif u2input == "l":
    print(ninput*0.9463525)
  elif u2input == "floz":
    print(ninput*32)
    
    
    
  
  
