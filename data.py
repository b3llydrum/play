#! /usr/bin/env python3

''' data to be used by play '''


# operating systems and their emulators
wineList = [
    'fceux',
    'lsnes',
]
osxList = [
    'openemu',
]


# dictionary of consoles and their extensions
extensionDict = {
    'gameboy' : ['.gb'],
    'gameboy_color' : ['.gbc'],
    'gameboy_advance' : ['.gba'],
    'nes' : ['.nes'],
    'snes' : ['.smc',
              '.sfc'
              ],
}


# dictionary of intended consoles
consoleDict = {
    'atari_2600' : ['atari_2600',
                    '2600',
                    'atari'
                    ],
    'atari_5200' : ['atari_5200',
                    '5200',
                    ],
    'atari_7800' : ['atari_7800'
                    '7800',
                    ],
    'gameboy' : ['gb',
                 'gameboy',
                 'game_boy',
                 ],
    'gameboy_color' : ['gbc',
                       'gameboycolor',
                       'gbcolor',
                       'gameboy_color',
                       'game_boy_color',
                       ],
    'gameboy_advance' : ['gba',
                         'gameboyadvance',
                         'gbadvance',
                         'gameboy_advance',
                         'game_boy_advance',
                         ],
    'n64' : ['n64',
             'nintendo64',
             'nintendo_64',
             ],
    'nes' : ['nes',
             'nintendo',
             'nintendo_entertainment_system',
             ],
    'psx' : ['psx',
             'ps1',
             'psone',
             'playstation',
             'playstation_1',
             'playstation_one',
             'play_station',
             ],
    'snes' : ['snes',
              'supernintendo',
              'super_nintendo',
              'super_nes',
              ],
    'sega_32x' : ['32x',
                  'sega_32x',
                  'sega32',
                  'sega32x',
                  '32',
                  ],
    'sega_cd' : ['sega_cd',
                 'segacd',
                 ],
    'sega_genesis' : ['genesis',
                      'sega_genesis',
                      'segagenesis',
                      'sega',
                      ],
}


# dictionary of intended emulators
emulatorDict = {
    'fceux' : ['fceux',
               'fcuex',
               'fcux',
               'fcex',
               ],
    'lsnes' : ['lsnes',
               'lsens',
               'slesn',
               'slens',
               'lsne',
               ],
    'OpenEmu' : ['OpenEmu',
                 'openemu',
                 'oe',
                 'OE',
                 ],
}


# pairs console with its emulator
emulatorConsoleDict = {
    'fceux' : ['nes'],
    'lsnes' : ['snes'],
    'OpenEmu' : ['gameboy',
                 'gameboy_color',
                 'gameboy_advance',
                 'atari_2600',
                 'atari_5200',
                 'atari_7800',
                 'n64',
                 'psx',
                 'sega_32x',
                 'sega_cd',
                 'sega_genesis',
                 ],
}


# list of consoles emulated by OpenEmu
openEmuList = ['gameboy',
               'gameboy_color',
               'gameboy_advance',
               'atari_2600',
               'atari_5200',
               'atari_7800',
               'n64',
               'nes',
               'psx',
               'sega_32x',
               'sega_cd',
               'sega_genesis',
               'snes',
               ]
