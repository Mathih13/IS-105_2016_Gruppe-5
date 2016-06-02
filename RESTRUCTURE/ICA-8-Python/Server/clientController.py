from echoclient import Client



c = Client('localhost', 10000)

def sendAndRecieve(message):
    msg = message
    answer = c.send(msg)
    if msg == 'db':
        answer = answer.split(',')
        return answer

    c.close()






