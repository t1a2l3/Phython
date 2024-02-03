command=""
started=False
while True:
    command=input('> ').lower()
    if command=='start':
        if started:
            print('car is alreday stared..')
        else:
            started=True
            print('car started...')
   
    elif command=='stop':
        if not started:
            print('car is already stopped..')
        else:
            started=False
            print('car stopped...')
    elif command=='help':
        print('''
     start-to start game
     stop-to stop the game
     quiet--to exit

        ''')
    elif command=='quiet':
        break
    else:
        print('sorry i dont understand')

        

        

        

