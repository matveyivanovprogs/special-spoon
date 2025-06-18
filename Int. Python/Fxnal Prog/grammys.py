from functools import reduce

def filter_length(song):
    if  song[1]>5.0:
        return song
    
def seconds(song):
    duration = song[1]
    minutes = int(duration)
    seconds = (duration - minutes) * 100

    return minutes * 60 + round(seconds)

def total(x,song1):
    return x+song1[1]


# List of songs with their durations (in minutes)
playlist = [('What Was I Made For?', 3.42), ('Just Like That', 5.05), ('Song 3', 6.8), ('Leave The Door Open', 4.02), ('I Can\'t Breath', 4.47), ('Bad Guy', 3.14)]
sL5= filter(filter_length, playlist)
print(list(sL5))
sec = map(seconds, playlist)
print(list(sec))
sum = reduce(total, playlist,0)
print(sum)
