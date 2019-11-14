Screenwidth=1200
Screenheight=1000
Edgecolor=(0,0,0)
Cellcolor=(100,100,100)
Figurecolor=(230,230,230)
Labelcolor=(0,0,0)
Scorecolor=(230,0,0)
Stopcolor=(0,0,230)
Titlecolor=(0,0,255)
Cellwidth=40
Leftwidth=Rightwidth=400
Topwidth=150
Gamewidth=400
Gameheight=800

S_template=[['0110','1100','0000'],['0100','0110','0010']]
Z_template=[['1100','0110','0000'],['0010','0110','0100']]
O_template=[['0110','0110']]
I_template=[['0100','0100','0100','0100'],['0000','1111','0000','0000']]
L_template=[['0100','0100','0110'],['0000','0111','0100'],['0110','0010','0010'],['0000','0001','0111']]
J_template=[['0010','0010','0110'],['0000','0100','0111'],['0110','0100','0100'],['0000','0111','0001']]
T_template=[['0100','1110','0000'],['0100','0110','0100'],['1110','0100','0000'],['0100','1100','0100']]


PIECE={'S':S_template,
       'Z':Z_template,
       'O':O_template,
       'I':I_template,
       'L':L_template,
       'J':J_template,
       'T':T_template}

Type=['S','Z','O','I','L','J','T']

Color={'S':(0,255,128),
       'Z':(255,128,255),
       'O':(255,0,0),
       'I':(255,255,0),
       'L':(0,0,255),
       'J':(128,0,255),
       'T':(255,128,0)}

Wall_blank='-'

TIMER_INTERVAL=1000
