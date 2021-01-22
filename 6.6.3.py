def lettercountinaword(word,letter):
    count=0
    for let in word:
        if let==letter:
            count=count+1
    print('letter ',letter,'count in word ',word,' is ',count)

word='banana'
lettercountinaword(word,'a')
            