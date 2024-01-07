def get_sender(msg: str):
    return msg.split('>')[0].split('<')[1].split(' ')[1]
def get_msg(msg: str):
    return msg.split('>')[1]