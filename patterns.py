buffer_file = ''

regions = ['U', 'J', 'E', 'G']

# create regex object to match filenames with no tags
# Sim Ant.smc
if console == 'snes':
    purePattern = re.compile(r'[^\]][^\)]\.(smc|sfc)')
else:
    purePattern = re.compile(r'[^\]][^\)]\.({extension})'.format(extension=extension[1:]))

# create regex object to match filenames with [tag1] type tags
# Lagoon (U) [b1].smc
tagPattern = re.compile(r'\[([a-z])+')

# create regex object to match filenames with (U) type region tags
# Rockman X (J) (V1.0) [f1].smc
regionPattern = re.compile(r'\([E|U|G|J]')

# create regex object to match filenames with [!] type tags
# Donkey Kong Country (U) (V1.2) [!].smc
definitivePattern = re.compile(r'\[!\]')
