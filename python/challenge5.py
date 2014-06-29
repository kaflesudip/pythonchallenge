import pickle
f = open('banner.p', 'rb')
output = pickle.load(f)

data = []
for item in output:
    for each_item in item:
        data.append(each_item[0] * each_item[1])
    data.append('\n')
print (''.join(data))
# http://www.pythonchallenge.com/pc/def/channel.html