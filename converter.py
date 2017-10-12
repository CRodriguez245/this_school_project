cont = 0;
while cont == 0:
  utype = input("Enter the type of conversion you want: (temperature, length, volume)");
  if utype == "temperature":
    F = 0
    C = 1
    K = 2
  
    print("Please enter your conversion in this format: lowercase_unit_from(value,uppercase_unit_to)")
    print("")
    print("Example:")
    print("To convert 45 degrees Fahrenheit to degrees Celsius, type:")
    print("f(45,C)")
  
    def f(value, base):
      if base == F:
          return value
      elif base == C:
          return (value - 32)/1.8
      elif base == K:
          return (value - 32)/1.8 + 273.15
      else:
          print("Error: incorrect format.")
  
    def c(value, base):
      if base == C:
          return value
      elif base == F:
          return (1.8 + value) + 32
      elif base == K:
          return value + 273.15
      else:
          print("Error: incorrect format.")
  
    def k(value, base):
      if base == K:
          return value
      elif base == C:
          return (value - 273.15)
      elif base == F:
          return (value - 273.15) * 1.8 + 32
      else:
          print("Error: incorrect format.")
  elif(utype == "length"):
    print("In progress");
  elif(utype == "volume"):
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
  cont = int(input("Would you like to do another conversion? 0 for yes, 1 for no"))

  