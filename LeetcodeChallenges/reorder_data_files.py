def reorderLogFiles(logs):
    digitLogs= []
    letterLogs= []
    for log in logs:
        words = log.split(' ')
        if words[1].isdigit():
            digitLogs.append(log)
        else:
            letterLogs.append(log)
    letterLogs.sort(key = lambda x: x.split(' ')[0])
    letterLogs.sort(key = lambda x: x.split(' ')[1:])
    letterLogs.extend(digitLogs)
    return letterLogs

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
print(reorderLogFiles(logs))
