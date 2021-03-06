BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DKGREEN = (0, 100, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
DKGRAY = (64, 64, 64)
LTGRAY = (196, 196, 196)
VERYLTGRAY = (211, 211, 211)
BROWN = (92, 64, 51)
TEAL = (2, 132, 130)
GOLD = (212, 175, 55)
ORANGE = (255, 128, 0)
DARKORANGE = (255, 140, 0)
ROYALBLUE = (65, 105, 225)
FORESTGREEN = (34, 139, 34)
OFFWHITE = (245, 245, 245)

SCOREBOARDTITLE = "Welcome to Fallon Eng Lab Robot Games"
FELTEAMSFILE = "felteams.txt"
LOGOIMAGE = "mustang.png"
SBWIDTH = 1920
SBHEIGHT = 1080
PADDING = 5
SCOREBOARDSIZE = (SBWIDTH, SBHEIGHT)
AREAWIDTH = int(SBWIDTH * 3 / 4) - 6 * PADDING
DEFAULTFONT = 'Arial'



TOPAREAHEIGHT = int(SBHEIGHT / 3)
ORGNAME = "Fallon Engineering Lab"
ORGNAMEFONT = DEFAULTFONT
ORGNAMEFONTSZ = int(AREAWIDTH / 40)
ORGNAMEFONTCLR = BROWN
GAMENAME = "TIME TRIAL"
GAMENAMEFONT = DEFAULTFONT
GAMENAMEFONTSZ = int(AREAWIDTH / 18)
GAMENAMEFONTCLR = DARKORANGE

GAMEAREAHEIGHT = int(SBHEIGHT / 3)
GAMEAREAWIDTH = AREAWIDTH
GAMETEAMWIDTH = GAMEAREAWIDTH - 6 * PADDING
GAMETEAMHEIGHT = int(GAMEAREAHEIGHT * 2 / 3 - 4 * PADDING)
ROUNDHEIGHT = GAMEAREAHEIGHT - GAMETEAMHEIGHT - 4 * PADDING
GAMETEAMFONT = DEFAULTFONT
GAMETEAMFONTSZ = int(GAMETEAMWIDTH / 8)
GAMETEAMFONTCLR = WHITE
GAMETEAMCOLOR = ROYALBLUE
ROUNDFONT = DEFAULTFONT
ROUNDFONTSZ = ROUNDHEIGHT - 10 * PADDING
ROUNDFONTCOLOR = DKGRAY

TEAMAREAHEIGHT = int(SBHEIGHT / 3)
TEAMAREAWIDTH = AREAWIDTH
TEAMBUTTONHEIGHT = int(TEAMAREAHEIGHT / 3 - PADDING)
TEAMFONT = DEFAULTFONT
TEAMFONTSZ = int(TEAMBUTTONHEIGHT / 4.3)
TEAMFONTCLR = BLACK
STATUSFONT = 'Helvetica'
STATUSFONTSZ = int(TEAMBUTTONHEIGHT / 5)
STATUSFONTCLRCOMPLETED = RED
STATUSFONTCLRPLAYING = DKGREEN
SCOREFONT = DEFAULTFONT
SCOREFONTSZ = int(TEAMBUTTONHEIGHT / 5)
SCOREFONTCLR = DKGRAY

CLOCKWIDTH = int(AREAWIDTH / 2)
CLOCKHEIGHT = int(SBHEIGHT / 3) - 8 * PADDING
CLOCKBUTTONWIDTH = int(CLOCKWIDTH / 5) - PADDING
CLOCKBUTTONHEIGHT = int(CLOCKHEIGHT / 2 - PADDING / 2)
CLOCKCOLOR = FORESTGREEN
CLOCKFONT = DEFAULTFONT
CLOCKFONTSZ = int(CLOCKWIDTH / 3)
CLOCKFONTCLR = WHITE
CLKBTNCLR = GOLD
CLKBTNFONT = DEFAULTFONT
CLKBTNFNTSZ = int(CLOCKBUTTONWIDTH / 3)
CLKBTNFNTCLR = WHITE

LDRBRDHEIGHT = SBHEIGHT - 2 * PADDING
LDRBRDWIDTH = SBWIDTH - AREAWIDTH - 2 * PADDING
LDRNAME = "LEADER BOARD"
LDRFONT = DEFAULTFONT
LDRNAMECLR = DKGRAY
LDRFONTCLR = WHITE
LDRCOLOR = GRAY

GAMETIMESECS = 150
teamButton = {}
felteam = {}
gameAreaButton = {}

MAXROUNDS = 3
