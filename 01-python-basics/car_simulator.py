print("""
Car Simulator
type help, for instructions
""")
command = ""
car_started = False

while True:
      command = input("> ").lower()

      if command == "start":
              if car_started:
                  print("""Car has alr3ady started dude... 
""")
              else:
                 car_started = True
                 print("""Car has Started....
""")

      elif command == "stop":
                if not car_started:
                   print("""its not like its moving or anything
""")
                else:
                     car_started = False
                     print("""Car has stopped
""")

      elif command == "help":
              print ("""
Start - gets the car moving
Stop - stops the car
Status - Check whether car is running
restart - Restart engine
help - help
quit - surely you know this one
              """)

      elif command == "quit":
           print ("The car will always remember you!!")
           break

      elif command == "status":
            if car_started:
                print ("car running")
            else:
                print ("car not running")

      elif command == "restart":
                 if car_started:
                     car_started = False
                     car_started = True
                     print(""" why you had to restart the engine beats me, but its done.
""")
                     continue
                 else:
                     print("""cant restart a car that has parked.
""")

      else:
             print(" Wrong Command")