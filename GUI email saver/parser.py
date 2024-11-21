import configparser

# config['DEFAULT'] = {'ServerAliveInterval': '45',
#                      'Compression': 'yes',
#                      'CompressionLevel': '9'}
# config['forge.example'] = {}
# config['forge.example']['Users']  = 'hg'
# config['topsecret.server.example'] = {}
# topsecret = config['topsecret.server.example']
# topsecret['Port'] = '50022'     # mutates the parser
# topsecret['ForwardX11'] = 'no'  # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# with open('example.ini', 'w') as configfile:
#   config.write(configfile)

config = configparser.ConfigParser()
config.read('config.ini')

print(config['EXTRA MATCH']['match'].split(','))
original = config['EXTRA MATCH']['match'].split(',')
print(original)
other = 'text'

new = []
new.extend(original)
new.append(other)
print(new)
# skips = config['DEFAULT']['skip'].split(',')
# skip = config['DEFAULT']['skip']
 
# print(skips)