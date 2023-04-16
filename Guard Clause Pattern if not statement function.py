paid = True
internet = True
online = True

def go_online():
    if not paid:
        print('User has an outstanding balance')
        return
    if not internet:
        print('Connection cannot be established')
        return
    if not online:
        print('Connection Error')
        return
    if  paid == True:
        internet == True
        online == True
        print('You are connected')
    
go_online()

