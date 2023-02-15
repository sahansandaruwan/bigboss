def textspam(message):
    try:
        num = message.content[10:]
        num = int(num)
        return num
    except:
        return 0