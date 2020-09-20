#Affichage du tableau
import codecs, os, tkinter#, tkFont#, ascii
# helv36 = tkFont.Font ( family="cambria",size=16 )#,weight="bold"
list1=["### Decoding Table\n","'\x00'     #  0x00 -> NULL\n","'\x01'     #  0x01 -> START OF HEADING\n","'\x02'     #  0x02 -> START OF TEXT\n","'\x03'     #  0x03 -> END OF TEXT\n","'\x04'     #  0x04 -> END OF TRANSMISSION\n","'\x05'     #  0x05 -> ENQUIRY\n","'\x06'     #  0x06 -> ACKNOWLEDGE\n","'\x07'     #  0x07 -> BELL\n","'\x08'     #  0x08 -> BACKSPACE\n","'\t'       #  0x09 -> HORIZONTAL TABULATION\n","'\\n'       #  0x0A -> LINE FEED\n","'\x0b'     #  0x0B -> VERTICAL TABULATION\n","'\x0c'     #  0x0C -> FORM FEED\n","'\r'       #  0x0D -> CARRIAGE RETURN\n","'\x0e'     #  0x0E -> SHIFT OUT\n","'\x0f'     #  0x0F -> SHIFT IN\n","'\x10'     #  0x10 -> DATA LINK ESCAPE\n","'\x11'     #  0x11 -> DEVICE CONTROL ONE\n","'\x12'     #  0x12 -> DEVICE CONTROL TWO\n","'\x13'     #  0x13 -> DEVICE CONTROL THREE\n","'\x14'     #  0x14 -> DEVICE CONTROL FOUR\n","'\x15'     #  0x15 -> NEGATIVE ACKNOWLEDGE\n","'\x16'     #  0x16 -> SYNCHRONOUS IDLE\n","'\x17'     #  0x17 -> END OF TRANSMISSION BLOCK\n","'\x18'     #  0x18 -> CANCEL\n","'\x19'     #  0x19 -> END OF MEDIUM\n","'\x1a'     #  0x1A -> SUBSTITUTE\n","'\x1b'     #  0x1B -> ESCAPE\n","'\x1c'     #  0x1C -> FILE SEPARATOR\n","'\x1d'     #  0x1D -> GROUP SEPARATOR\n","'\x1e'     #  0x1E -> RECORD SEPARATOR\n","'\x1f'     #  0x1F -> UNIT SEPARATOR\n","' '        #  0x20 -> SPACE\n","'!'        #  0x21 -> EXCLAMATION MARK\n","""'"'        #  0x22 -> QUOTATION MARK\n""","'#'        #  0x23 -> NUMBER SIGN","\n'$'        #  0x24 -> DOLLAR SIGN\n","'%'        #  0x25 -> PERCENT SIGN\n","'&'        #  0x26 -> AMPERSAND\n",""""'"        #  0x27 -> APOSTROPHE\n""","'('        #  0x28 -> LEFT PARENTHESIS\n","')'        #  0x29 -> RIGHT PARENTHESIS\n","'*'        #  0x2A -> ASTERISK","\n'+'        #  0x2B -> PLUS SIGN\n","','        #  0x2C -> COMMA\n","'-'        #  0x2D -> HYPHEN-MINUS\n","'.'        #  0x2E -> FULL STOP\n","'/'        #  0x2F -> SOLIDUS\n","'0'        #  0x30 -> DIGIT ZERO\n","'1'        #  0x31 -> DIGIT ONE\n","'2'        #  0x32 -> DIGIT TWO\n","'3'        #  0x33 -> DIGIT THREE\n","'4'        #  0x34 -> DIGIT FOUR\n","'5'        #  0x35 -> DIGIT FIVE\n","'6'        #  0x36 -> DIGIT SIX\n","'7'        #  0x37 -> DIGIT SEVEN\n","'8'        #  0x38 -> DIGIT EIGHT\n","'9'        #  0x39 -> DIGIT NINE\n","':'        #  0x3A -> COLON\n","';'        #  0x3B -> SEMICOLON\n","'<'        #  0x3C -> LESS-THAN SIGN\n","'='        #  0x3D -> EQUALS SIGN\n","'>'        #  0x3E -> GREATER-THAN SIGN\n","'?'        #  0x3F -> QUESTION MARK\n","'@'        #  0x40 -> COMMERCIAL AT\n","'A'        #  0x41 -> LATIN CAPITAL LETTER A\n","'B'        #  0x42 -> LATIN CAPITAL LETTER B\n","'C'        #  0x43 -> LATIN CAPITAL LETTER C\n","'D'        #  0x44 -> LATIN CAPITAL LETTER D\n","'E'        #  0x45 -> LATIN CAPITAL LETTER E\n","'F'        #  0x46 -> LATIN CAPITAL LETTER F\n","'G'        #  0x47 -> LATIN CAPITAL LETTER G\n","'H'        #  0x48 -> LATIN CAPITAL LETTER H\n","'I'        #  0x49 -> LATIN CAPITAL LETTER I\n","'J'        #  0x4A -> LATIN CAPITAL LETTER J\n","'K'        #  0x4B -> LATIN CAPITAL LETTER K\n","'L'        #  0x4C -> LATIN CAPITAL LETTER L\n","'M'        #  0x4D -> LATIN CAPITAL LETTER M\n","'N'        #  0x4E -> LATIN CAPITAL LETTER N\n","'O'        #  0x4F -> LATIN CAPITAL LETTER O\n","'P'        #  0x50 -> LATIN CAPITAL LETTER P\n","'Q'        #  0x51 -> LATIN CAPITAL LETTER Q\n","'R'        #  0x52 -> LATIN CAPITAL LETTER R\n","'S'        #  0x53 -> LATIN CAPITAL LETTER S\n","'T'        #  0x54 -> LATIN CAPITAL LETTER T\n","'U'        #  0x55 -> LATIN CAPITAL LETTER U\n","'V'        #  0x56 -> LATIN CAPITAL LETTER V\n","'W'        #  0x57 -> LATIN CAPITAL LETTER W\n","'X'        #  0x58 -> LATIN CAPITAL LETTER X\n","'Y'        #  0x59 -> LATIN CAPITAL LETTER Y\n","'Z'        #  0x5A -> LATIN CAPITAL LETTER Z\n'['        #  0x5B -> LEFT SQUARE BRACKET\n","'\\'       #  0x5C -> REVERSE SOLIDUS\n","']'        #  0x5D -> RIGHT SQUARE BRACKET\n","'^'        #  0x5E -> CIRCUMFLEX ACCENT\n","'_'        #  0x5F -> LOW LINE\n","'`'        #  0x60 -> GRAVE ACCENT\n","'a'        #  0x61 -> LATIN SMALL LETTER A\n","'b'        #  0x62 -> LATIN SMALL LETTER B\n","'c'        #  0x63 -> LATIN SMALL LETTER C\n","'d'        #  0x64 -> LATIN SMALL LETTER D\n","'e'        #  0x65 -> LATIN SMALL LETTER E\n","'f'        #  0x66 -> LATIN SMALL LETTER F\n","'g'        #  0x67 -> LATIN SMALL LETTER G\n","'h'        #  0x68 -> LATIN SMALL LETTER H\n","'i'        #  0x69 -> LATIN SMALL LETTER I\n","'j'        #  0x6A -> LATIN SMALL LETTER J\n","'k'        #  0x6B -> LATIN SMALL LETTER K\n","'l'        #  0x6C -> LATIN SMALL LETTER L\n","'m'        #  0x6D -> LATIN SMALL LETTER M\n","'n'        #  0x6E -> LATIN SMALL LETTER N\n","'o'        #  0x6F -> LATIN SMALL LETTER O\n","'p'        #  0x70 -> LATIN SMALL LETTER P\n","'q'        #  0x71 -> LATIN SMALL LETTER Q\n","'r'        #  0x72 -> LATIN SMALL LETTER R\n","'s'        #  0x73 -> LATIN SMALL LETTER S\n","'t'        #  0x74 -> LATIN SMALL LETTER T\n","'u'        #  0x75 -> LATIN SMALL LETTER U\n","'v'        #  0x76 -> LATIN SMALL LETTER V\n","'w'        #  0x77 -> LATIN SMALL LETTER W\n","'x'        #  0x78 -> LATIN SMALL LETTER X\n","'y'        #  0x79 -> LATIN SMALL LETTER Y\n","'z'        #  0x7A -> LATIN SMALL LETTER Z\n","'{'        #  0x7B -> LEFT CURLY BRACKET\n","'|'        #  0x7C -> VERTICAL LINE\n","'}'        #  0x7D -> RIGHT CURLY BRACKET\n","'~'        #  0x7E -> TILDE\n","'\x7f'     #  0x7F -> DELETE\n","'\u20ac'   #  0x80 -> EURO SIGN\n","'\ufffe'   #  0x81 -> UNDEFINED\n","'\u201a'   #  0x82 -> SINGLE LOW-9 QUOTATION MARK\n","'\u0192'   #  0x83 -> LATIN SMALL LETTER F WITH HOOK\n","'\u201e'   #  0x84 -> DOUBLE LOW-9 QUOTATION MARK\n","'\u2026'   #  0x85 -> HORIZONTAL ELLIPSIS\n","'\u2020'   #  0x86 -> DAGGER\n","'\u2021'   #  0x87 -> DOUBLE DAGGER\n","'\u02c6'   #  0x88 -> MODIFIER LETTER CIRCUMFLEX ACCENT\n","'\u2030'   #  0x89 -> PER MILLE SIGN\n","'\u0160'   #  0x8A -> LATIN CAPITAL LETTER S WITH CARON\n","'\u2039'   #  0x8B -> SINGLE LEFT-POINTING ANGLE QUOTATION MARK\n","'\u0152'   #  0x8C -> LATIN CAPITAL LIGATURE OE\n","'\ufffe'   #  0x8D -> UNDEFINED\n","'\u017d'   #  0x8E -> LATIN CAPITAL LETTER Z WITH CARON\n","'\ufffe'   #  0x8F -> UNDEFINED\n","'\ufffe'   #  0x90 -> UNDEFINED\n","'\u2018'   #  0x91 -> LEFT SINGLE QUOTATION MARK\n","'\u2019'   #  0x92 -> RIGHT SINGLE QUOTATION MARK\n","'\u201c'   #  0x93 -> LEFT DOUBLE QUOTATION MARK\n","'\u201d'   #  0x94 -> RIGHT DOUBLE QUOTATION MARK\n","'\u2022'   #  0x95 -> BULLET\n","'\u2013'   #  0x96 -> EN DASH\n","'\u2014'   #  0x97 -> EM DASH\n","'\u02dc'   #  0x98 -> SMALL TILDE\n","'\u2122'   #  0x99 -> TRADE MARK SIGN\n","'\u0161'   #  0x9A -> LATIN SMALL LETTER S WITH CARON\n","'\u203a'   #  0x9B -> SINGLE RIGHT-POINTING ANGLE QUOTATION MARK\n","'\u0153'   #  0x9C -> LATIN SMALL LIGATURE OE\n","'\ufffe'   #  0x9D -> UNDEFINED\n","'\u017e'   #  0x9E -> LATIN SMALL LETTER Z WITH CARON\n","'\u0178'   #  0x9F -> LATIN CAPITAL LETTER Y WITH DIAERESIS\n","'\xa0'     #  0xA0 -> NO-BREAK SPACE\n","'\xa1'     #  0xA1 -> INVERTED EXCLAMATION MARK\n","'\xa2'     #  0xA2 -> CENT SIGN\n","'\xa3'     #  0xA3 -> POUND SIGN\n","'\xa4'     #  0xA4 -> CURRENCY SIGN\n","'\xa5'     #  0xA5 -> YEN SIGN\n","'\xa6'     #  0xA6 -> BROKEN BAR\n","'\xa7'     #  0xA7 -> SECTION SIGN\n","'\xa8'     #  0xA8 -> DIAERESIS\n","'\xa9'     #  0xA9 -> COPYRIGHT SIGN\n","'\xaa'     #  0xAA -> FEMININE ORDINAL INDICATOR\n","'\xab'     #  0xAB -> LEFT-POINTING DOUBLE ANGLE QUOTATION MARK\n","'\xac'     #  0xAC -> NOT SIGN\n","'\xad'     #  0xAD -> SOFT HYPHEN\n","'\xae'     #  0xAE -> REGISTERED SIGN\n","'\xaf'     #  0xAF -> MACRON\n","'\xb0'     #  0xB0 -> DEGREE SIGN\n","'\xb1'     #  0xB1 -> PLUS-MINUS SIGN\n","'\xb2'     #  0xB2 -> SUPERSCRIPT TWO\n","'\xb3'     #  0xB3 -> SUPERSCRIPT THREE\n","'\xb4'     #  0xB4 -> ACUTE ACCENT\n","'\xb5'     #  0xB5 -> MICRO SIGN\n","'\xb6'     #  0xB6 -> PILCROW SIGN\n","'\xb7'     #  0xB7 -> MIDDLE DOT\n","'\xb8'     #  0xB8 -> CEDILLA\n","'\xb9'     #  0xB9 -> SUPERSCRIPT ONE\n","'\xba'     #  0xBA -> MASCULINE ORDINAL INDICATOR\n","'\xbb'     #  0xBB -> RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK\n","'\xbc'     #  0xBC -> VULGAR FRACTION ONE QUARTER\n","'\xbd'     #  0xBD -> VULGAR FRACTION ONE HALF\n","'\xbe'     #  0xBE -> VULGAR FRACTION THREE QUARTERS\n","'\xbf'     #  0xBF -> INVERTED QUESTION MARK\n","'\xc0'     #  0xC0 -> LATIN CAPITAL LETTER A WITH GRAVE\n","'\xc1'     #  0xC1 -> LATIN CAPITAL LETTER A WITH ACUTE\n","'\xc2'     #  0xC2 -> LATIN CAPITAL LETTER A WITH CIRCUMFLEX\n","'\xc3'     #  0xC3 -> LATIN CAPITAL LETTER A WITH TILDE\n","'\xc4'     #  0xC4 -> LATIN CAPITAL LETTER A WITH DIAERESIS\n","'\xc5'     #  0xC5 -> LATIN CAPITAL LETTER A WITH RING ABOVE\n","'\xc6'     #  0xC6 -> LATIN CAPITAL LETTER AE\n","'\xc7'     #  0xC7 -> LATIN CAPITAL LETTER C WITH CEDILLA\n","'\xc8'     #  0xC8 -> LATIN CAPITAL LETTER E WITH GRAVE\n","'\xc9'     #  0xC9 -> LATIN CAPITAL LETTER E WITH ACUTE\n","'\xca'     #  0xCA -> LATIN CAPITAL LETTER E WITH CIRCUMFLEX\n","'\xcb'     #  0xCB -> LATIN CAPITAL LETTER E WITH DIAERESIS\n","'\xcc'     #  0xCC -> LATIN CAPITAL LETTER I WITH GRAVE\n","'\xcd'     #  0xCD -> LATIN CAPITAL LETTER I WITH ACUTE\n","'\xce'     #  0xCE -> LATIN CAPITAL LETTER I WITH CIRCUMFLEX\n","'\xcf'     #  0xCF -> LATIN CAPITAL LETTER I WITH DIAERESIS\n","'\xd0'     #  0xD0 -> LATIN CAPITAL LETTER ETH\n","'\xd1'     #  0xD1 -> LATIN CAPITAL LETTER N WITH TILDE\n","'\xd2'     #  0xD2 -> LATIN CAPITAL LETTER O WITH GRAVE\n","'\xd3'     #  0xD3 -> LATIN CAPITAL LETTER O WITH ACUTE\n","'\xd4'     #  0xD4 -> LATIN CAPITAL LETTER O WITH CIRCUMFLEX\n","'\xd5'     #  0xD5 -> LATIN CAPITAL LETTER O WITH TILDE\n","'\xd6'     #  0xD6 -> LATIN CAPITAL LETTER O WITH DIAERESIS\n","'\xd7'     #  0xD7 -> MULTIPLICATION SIGN\n","'\xd8'     #  0xD8 -> LATIN CAPITAL LETTER O WITH STROKE\n","'\xd9'     #  0xD9 -> LATIN CAPITAL LETTER U WITH GRAVE\n","'\xda'     #  0xDA -> LATIN CAPITAL LETTER U WITH ACUTE\n","'\xdb'     #  0xDB -> LATIN CAPITAL LETTER U WITH CIRCUMFLEX\n","'\xdc'     #  0xDC -> LATIN CAPITAL LETTER U WITH DIAERESIS\n","'\xdd'     #  0xDD -> LATIN CAPITAL LETTER Y WITH ACUTE\n","'\xde'     #  0xDE -> LATIN CAPITAL LETTER THORN\n","'\xdf'     #  0xDF -> LATIN SMALL LETTER SHARP S\n","'\xe0'     #  0xE0 -> LATIN SMALL LETTER A WITH GRAVE\n","'\xe1'     #  0xE1 -> LATIN SMALL LETTER A WITH ACUTE\n","'\xe2'     #  0xE2 -> LATIN SMALL LETTER A WITH CIRCUMFLEX\n","'\xe3'     #  0xE3 -> LATIN SMALL LETTER A WITH TILDE\n","'\xe4'     #  0xE4 -> LATIN SMALL LETTER A WITH DIAERESIS\n","'\xe5'     #  0xE5 -> LATIN SMALL LETTER A WITH RING ABOVE\n","'\xe6'     #  0xE6 -> LATIN SMALL LETTER AE\n","'\xe7'     #  0xE7 -> LATIN SMALL LETTER C WITH CEDILLA\n","'\xe8'     #  0xE8 -> LATIN SMALL LETTER E WITH GRAVE\n","'\xe9'     #  0xE9 -> LATIN SMALL LETTER E WITH ACUTE\n","'\xea'     #  0xEA -> LATIN SMALL LETTER E WITH CIRCUMFLEX\n","'\xeb'     #  0xEB -> LATIN SMALL LETTER E WITH DIAERESIS\n","'\xec'     #  0xEC -> LATIN SMALL LETTER I WITH GRAVE\n","'\xed'     #  0xED -> LATIN SMALL LETTER I WITH ACUTE\n","'\xee'     #  0xEE -> LATIN SMALL LETTER I WITH CIRCUMFLEX\n","'\xef'     #  0xEF -> LATIN SMALL LETTER I WITH DIAERESIS\n","'\xf0'     #  0xF0 -> LATIN SMALL LETTER ETH\n","'\xf1'     #  0xF1 -> LATIN SMALL LETTER N WITH TILDE\n","'\xf2'     #  0xF2 -> LATIN SMALL LETTER O WITH GRAVE\n","'\xf3'     #  0xF3 -> LATIN SMALL LETTER O WITH ACUTE\n","'\xf4'     #  0xF4 -> LATIN SMALL LETTER O WITH CIRCUMFLEX\n","'\xf5'     #  0xF5 -> LATIN SMALL LETTER O WITH TILDE\n","'\xf6'     #  0xF6 -> LATIN SMALL LETTER O WITH DIAERESIS\n","'\xf7'     #  0xF7 -> DIVISION SIGN\n","'\xf8'     #  0xF8 -> LATIN SMALL LETTER O WITH STROKE\n","'\xf9'     #  0xF9 -> LATIN SMALL LETTER U WITH GRAVE\n","'\xfa'     #  0xFA -> LATIN SMALL LETTER U WITH ACUTE\n","'\xfb'     #  0xFB -> LATIN SMALL LETTER U WITH CIRCUMFLEX\n","'\xfc'     #  0xFC -> LATIN SMALL LETTER U WITH DIAERESIS\n","'\xfd'     #  0xFD -> LATIN SMALL LETTER Y WITH ACUTE\n","'\xfe'     #  0xFE -> LATIN SMALL LETTER THORN\n","'\xff'     #  0xFF -> LATIN SMALL LETTER Y WITH DIAERESIS"]
mazes="""#================================================================================légende=========================================================\n#0 --> .   11 --> A  22 --> L  33 --> Y  44 --> j  55 --> u  66 --> ²  77 --> ^  88 --> ∝  99 --> ←   110 --> ⋈  121 --> ⊠  132 --> ⊙  143 --> ⋖\n#1 --> 1   12 --> B  23 --> O  34 --> Z  45 --> k  56 --> v  67 --> *  78 --> ¨  89 --> ∀  100 --> ↑  111 --> ⨀  122 --> ⊡  133 --> ⊛  144 --> ⋗\n#2 --> @   13 --> C  24 --> P  35 --> a  46 --> l  57 --> w  68 --> µ  79 --> ¤  90 --> ≡  101 --> →  112 --> ⨂  123 --> ⊞  134 --> ⊚  145 --> ≑\n#3 --> M   14 --> D  25 --> Q  36 --> b  47 --> m  58 --> x  69 --> ù  80 --> °  91 --> ≪  102 --> ↓  113 --> ⨁  124 --> ⋉  135 --> †  146 --> ≒\n#4 --> $   15 --> E  26 --> R  37 --> c  48 --> n  59 --> y  70 --> %  81 --> +  92 --> ≫  103 --> ⋮   114 --> ⨄  125 --> ⋊  136 --> ‡  147 --> ≓\n#5 --> £   16 --> F  27 --> S  38 --> d  49 --> o  60 --> z  71 --> !  82 --> ≤  93 --> ≅  104 --> ⋯  115 --> ⨃  126 --> ⋇  137 --> ⨂  148 --> ⊲\n#6 --> ∆   17 --> G  28 --> T  39 --> e  50 --> p  61 --> ~  72 --> §  83 --> ≥  94 --> ≈  105 --> ⋰  116 --> ∔  127 --> ⊝  138 --> △  149 --> ⊳\n#7 --> N   18 --> H  29 --> U  40 --> f  51 --> q  62 --> (  73 --> :  84 --> ∓  95 --> ℉  106 --> ⋱  117 --> ∸  128 --> ⊕  139 --> ⋘  150 --> ⊴\n#8 --> €   19 --> I  30 --> V  41 --> g  52 --> r  63 --> )  74 --> ?  85 --> ∞  96 --> ℃  107 --> ∎  118 --> ⋒  129 --> ⊖  140 --> ⋙  151 --> ⊵\n#9 --> |   20 --> J  31 --> W  42 --> h  53 --> s  64 --> _  75 --> <  86 --> ±  97 --> ∇  108 --> ∅  119 --> ⋓  130 --> ⊗  141 --> ≦  152 --> ⋐\n#10 --> -  21 --> K  32 --> X  43 --> i  54 --> t  65 --> &  76 --> >  87 --> ≠  98 --> √  109 --> ∑  120 --> ⊟  131 --> ⊘  142 --> ≧  153 --> ⋑\n#                                                                               154 --> ❤\n#==============================================================================fin légende======================================================="""
os=os.getcwd()
print (os)
def maze(t,nb_ligne, nb_colonne):
    print()
    for y in range(nb_ligne):
        for x in range(nb_colonne):
            valeur=t[y][x]
            if valeur ==0:
                print(".", end=" ")
            elif valeur==1:
                print(t[y][x], end=" ")
            elif valeur==2:
                print("@", end=" ")
            elif valeur==3:
                print("M", end=" ")
            elif valeur==4:
                print("$", end=" ")
            elif valeur==5:
                print("£", end=" ")
            elif valeur==6:
                print("∆", end=" ")
            elif valeur==7:
                print("N", end=" ")
            elif valeur==8:
                print("€", end=" ")
            elif valeur==9:
                print("|", end=" ")
            elif valeur== 10:
                print("-", end=" ")
            elif valeur==11:
                print("A", end=" ")
            elif valeur==12:
                print("B", end=" ")
            elif valeur==13:
                print("C", end=" ")
            elif valeur==14:
                print("D", end=" ")
            elif valeur==15:
                print("E", end=" ")
            elif valeur==16:
                print("F", end=" ")
            elif valeur==17:
                print("G", end=" ")
            elif valeur==18:
                print("H", end=" ")
            elif valeur==19:
                print("I", end=" ")
            elif valeur==20:
                print("J", end=" ")
            elif valeur==21:
                print("K", end=" ")
            elif valeur==22:
                print("L", end=" ")
            elif valeur==23:
                print("O", end=" ")
            elif valeur==24:
                print("P", end=" ")
            elif valeur==25:
                print("Q", end=" ")
            elif valeur==26:
                print("R", end=" ")
            elif valeur==27:
                print("S", end=" ")
            elif valeur==28:
                print("T", end=" ")
            elif valeur==29:
                print("U", end=" ")
            elif valeur==30:
                print("V", end=" ")
            elif valeur==31:
                print("W", end=" ")
            elif valeur==32:
                print("X", end=" ")
            elif valeur==33:
                print("Y", end=" ")
            elif valeur==34:
                print("Z", end=" ")
            elif valeur==35:
                print("a", end=" ")
            elif valeur==36:
                print("b", end=" ")
            elif valeur==37:
                print("c", end=" ")
            elif valeur==38:
                print("d", end=" ")
            elif valeur==39:
                print("e", end=" ")
            elif valeur==40:
                print("f", end=" ")
            elif valeur==41:
                print("g", end=" ")
            elif valeur==42:
                print("h", end=" ")
            elif valeur==43:
                print("i", end=" ")
            elif valeur==44:
                print("j", end=" ")
            elif valeur==45:
                print("k", end=" ")
            elif valeur==46:
                print("l", end=" ")
            elif valeur==47:
                print("m", end=" ")
            elif valeur==48:
                print("n", end=" ")
            elif valeur==49:
                print("o", end=" ")
            elif valeur==50:
                print("p", end=" ")
            elif valeur==51:
                print("q", end=" ")
            elif valeur==52:
                print("r", end=" ")
            elif valeur==53:
                print("s", end=" ")
            elif valeur==54:
                print("t", end=" ")
            elif valeur==55:
                print("u", end=" ")
            elif valeur==56:
                print("v", end=" ")
            elif valeur==57:
                print("w", end=" ")
            elif valeur==58:
                print("x", end=" ")
            elif valeur==59:
                print("y", end=" ")
            elif valeur==60:
                print("z", end=" ")
            elif valeur==61:
                print("~", end=" ")
            elif valeur==62:
                print("(", end=" ")
            elif valeur==63:
                print(")", end=" ")
            elif valeur==64:
                print("_", end=" ")
            elif valeur==65:
                print("&", end=" ")
            elif valeur==66:
                print("²", end=" ")
            elif valeur==67:
                print("*", end=" ")
            elif valeur==68:
                print("µ", end=" ")
            elif valeur==69:
                print("ù", end=" ")
            elif valeur==70:
                print("%", end=" ")
            elif valeur==71:
                print("!", end=" ")
            elif valeur==72:
                print("§", end=" ")
            elif valeur==73:
                print(":", end=" ")
            elif valeur==74:
                print("?", end=" ")
            elif valeur==75:
                print("<", end=" ")
            elif valeur==76:
                print(">", end=" ")
            elif valeur==77:
                print("^", end=" ")
            elif valeur==78:
                print("¨", end=" ")
            elif valeur==79:
                print("¤", end=" ")
            elif valeur==80:
                print("°", end=" ")
            elif valeur==81:
                print("+", end=" ")
            elif valeur==82:
                print("≤", end=" ")
            elif valeur==83:
                print("≥", end=" ")
            elif valeur==84:
                print("∓", end=" ")
            elif valeur==85:
                print("∞", end=" ")
            elif valeur==86:
                print("±", end=" ")
            elif valeur==87:
                print("≠", end=" ")
            elif valeur==88:
                print("∝", end=" ")
            elif valeur==89:
                print("∀", end=" ")
            elif valeur==90:
                print("≡", end=" ")
            elif valeur==91:
                print("≪", end=" ")
            elif valeur==92:
                print("≫", end=" ")
            elif valeur==93:
                print("≅", end=" ")
            elif valeur==94:
                print("≈", end=" ")
            elif valeur==95:
                print("℉", end=" ")
            elif valeur==96:
                print("℃", end=" ")
            elif valeur==97:
                print("∇", end=" ")
            elif valeur==98:
                print("√", end=" ")
            elif valeur==99:
                print("←", end=" ")
            elif valeur==100:
                print("↑", end=" ")
            elif valeur==101:
                print("→", end=" ")
            elif valeur==102:
                print("↓", end=" ")
            elif valeur==103:
                print("⋮", end=" ")
            elif valeur==104:
                print("⋯", end=" ")
            elif valeur==105:
                print("⋰", end=" ")
            elif valeur==106:
                print("⋱", end=" ")
            elif valeur==107:
                print("∎", end=" ")
            elif valeur==108:
                print("∅", end=" ")
            elif valeur==109:
                print("∑", end=" ")
            elif valeur==110:
                print("⋈", end=" ")
            elif valeur==111:
                print("⨀", end=" ")
            elif valeur==112:
                print("⨂", end=" ")
            elif valeur==113:
                print("⨁", end=" ")
            elif valeur==114:
                print("⨄", end=" ")
            elif valeur==115:
                print("⨃", end=" ")
            elif valeur==116:
                print("∔", end=" ")
            elif valeur==117:
                print("∸", end=" ")
            elif valeur==118:
                print("⋒", end=" ")
            elif valeur==119:
                print("⋓", end=" ")
            elif valeur==120:
                print("⊟", end=" ")
            elif valeur==121:
                print("⊠", end=" ")
            elif valeur==122:
                print("⊡", end=" ")
            elif valeur==123:
                print("⊞", end=" ")
            elif valeur==124:
                print("⋉", end=" ")
            elif valeur==125:
                print("⋊", end=" ")
            elif valeur==126:
                print("⋇", end=" ")
            elif valeur==127:
                print("⊝", end=" ")
            elif valeur==128:
                print("⊕", end=" ")
            elif valeur==129:
                print("⊖", end=" ")
            elif valeur==130:
                print("⊗", end=" ")
            elif valeur==131:
                print("⊘", end=" ")
            elif valeur==132:
                print("⊙", end=" ")
            elif valeur==133:
                print("⊛", end=" ")
            elif valeur==134:
                print("⊚", end=" ")
            elif valeur==135:
                print("†", end=" ")
            elif valeur==136:
                print("‡", end=" ")
            elif valeur==137:
                print("⨂", end=" ")
            elif valeur==138:
                print("△", end=" ")
            elif valeur==139:
                print("⋘", end=" ")
            elif valeur==140:
                print("⋙", end=" ")
            elif valeur==141:
                print("≦", end=" ")
            elif valeur==142:
                print("≧", end=" ")
            elif valeur==143:
                print("⋖", end=" ")
            elif valeur==144:
                print("⋗", end=" ")
            elif valeur==145:
                print("≑", end=" ")
            elif valeur==146:
                print("≒", end=" ")
            elif valeur==147:
                print("≓", end=" ")
            elif valeur==148:
                print("⊲", end=" ")
            elif valeur==149:
                print("⊳", end=" ")
            elif valeur==150:
                print("⊴", end=" ")
            elif valeur==151:
                print("⊵", end=" ")
            elif valeur==152:
                print("⋐", end=" ")
            elif valeur==153:
                print("⋑", end=" ")
            elif valeur==154:
                print("❤",end=" ")
        print()
#définition du tableau
#t1 9 lignes et 8 colonnes

t_1=[[1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,1],
    [1,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,3,1],
    [1,0,107,1,1,0,0,1],
    [1,0,0,3,0,0,0,1],
    [1,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1]]
t_2=[[1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,1],
    [1,1,1,1,0,0,0,1],
    [1,0,0,1,0,0,0,1],
    [1,0,0,1,0,1,3,1],
    [1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,5,1],
    [1,0,0,0,3,0,4,1],
    [1,1,1,1,1,1,1,1]]
t_3=[[3,0,3,3,3,3,3,3],
    [3,0,0,0,0,0,0,3],
    [3,6,6,6,0,6,6,3],
    [3,6,0,6,0,0,0,3],
    [3,0,0,0,0,6,6,3],
    [3,0,6,6,0,0,0,3],
    [3,0,0,0,6,6,6,3],
    [3,6,6,0,0,0,0,3],
    [3,3,3,3,3,3,0,3]]
t_maze1=[[3,0,3,3,3,3,3,1,3,3,3,1,3,3,3,3,3,3],
         [3,0,3,0,0,0,7,7,3,0,0,0,0,2,0,0,2,3],
         [3,0,0,0,7,0,0,1,0,0,3,1,0,2,2,0,2,3],
         [3,0,7,0,0,7,7,1,0,3,0,1,0,2,0,0,0,3],
         [3,0,0,7,0,0,7,1,0,0,0,1,0,2,0,2,0,3],
         [3,7,0,7,7,0,7,1,3,0,3,1,0,2,0,2,0,3],
         [3,0,0,0,7,0,0,0,0,0,3,1,0,0,0,2,0,3],
         [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,3]]
t_maze1_1=[[3,0,3,3,3,3,3,1,3],
         [3,0,3,0,0,0,7,7,3],
         [3,0,0,0,7,0,0,1,0],
         [3,0,7,0,0,7,7,1,0],
         [3,0,0,7,0,0,7,1,0],
         [3,7,0,7,7,0,7,1,3],
         [3,0,0,0,7,0,0,0,0],
         [3,3,3,3,3,3,3,3,3]]
t_maze1_2=[[3,3,1,3,3,3,3,3,3],
           [0,0,0,0,2,0,0,2,3],
           [0,3,1,0,2,2,0,2,3],
           [3,0,1,0,2,0,0,0,3],
           [0,0,1,0,2,0,2,0,3],
           [0,3,1,0,2,0,2,0,3],
           [0,3,1,0,0,0,2,0,3],
           [3,3,3,3,3,3,3,0,3]]
#t_mase2=[[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
ex="o"
print ("Bienvenue dans le programme Maze Maker créé par Henry Letellier \u2122, \xae, \xa9")
while ex=="o" or ex=="o" or ex=="0" or ex=="n" or ex=="N":
    ex=input("Voulez-vous un exemple? [(o)ui/(n)on/(q)uitter]:")
    if ex=="O" or ex=="o" or ex=="0":
        maze(t_1,9,8)
        maze(t_2,9,8)
        maze(t_3,9,8)
        maze(t_maze1,8,18)
        print("{}{}".format(maze(t_maze1_1,8,9),maze(t_maze1_2,8,9)))
    elif ex=="N" or ex=="n":
        show=input("Bienvenue dans la création de labyrinthes\nSi vous êtes nouveau mercie de taper i dans la question qui suivra.\nSi vous voulez créé et/ou afficher un labyrinthe, mercie d'entrer 'maze(<nom_du_labyrinthe>,<nombre_de_ligne>,<nombre_de_colonnes>) dans le fichier nomé ('maze_keper.txt'), (si les lettres '.txt' ne s'affichent pas, cela n'impactera pas le fonctionnement du programme).\nEntrez les coordonnées du labyrinthe à afficher:")
        if show=="i" or show=="I":
            print ("Bienvenue dans l'interface d'aide:\nPour créé un labyrinthe, mercie de bien vouloir suivre les instructions données dans l'aide pour permettre à votre labyrinthe de s'afficher corectement. Pour avoir accès à symboles insérables dans votre labyrinthe, mercie d'ouvrir le fichier nommé 'maze keper.txt', (si les lettres '.txt' ne s'affichent pas, cela n'impactera pas le fonctionnement du programme).\n")
        else:
            print (show)
            try:
                f=open("maze_symbole_legend.txt", "r")
                print (f.read())
                f.close()
                print ("worked")
                print (os)
            except:
                print(mazes)
                print ("fail")
                print (os)
            print (f.read())
            f.close()
            create=input("Voulez-vous créer un nouveau labyrinthe?: [(o)ui/(n)on]")
            if create=="o" or create=="O" or create=="0":
                wri=input("Bienvenue dans la partie création du programme\nEntrez ici le nom du labyrinthe (pas plus de deux lettres):")
                ze=wri
                eza=len(ze)
                if eza==2 or eza==1:
                    io="o"
                    ii=li=1
                    wri+="=["
                    brac="["
                    brac2="],\n"
                    i=0
                    ligne=int(input("De combien de lignes se compose votre labyrinthe?:"))
                    colonee=int(input("De combien de colonnes se compose votre labyrinthe?:"))
                    print("Pour povoir faire votre ligne, entrez un nombre à chaque question qui vous sera posée, à la fin de la création de la ligne, cette dernière sera affichée et vous aurez le choix de la gardée ou non si elle vous plait. (exemple:\nPour une ligne de quatres colone, on rentre le premier nombre dans la première question, le deuxième dans la seconde, le troisième dans la troisième et la quatrième dasn la quatrième question. Par exemple:\nQuel est le caractère n°1 de votre ligne n°1: 1\nQuel est le caractère n°2 de votre ligne n°1: 2\nQuel est le caractère n°3 de votre ligne n°1: 1\nQuel est le caractère n°4 de votre ligne n°1: 2 )\n")
                    while i<ligne:
                        #lene=lenline=input("Quelle est votre ligne n°{}:".format(li))
                        satisfied="n"
                        ceque=""
                        while satisfied=="n" or satisfied=="N":
                            ii=1
                            colonealone=""
                            while ii<colonee+1:
                                coloneee=input("Quel est le caractère n°{} de votre ligne n°{}: {}{}".format(ii, li, ceque, colonealone))
                                if ii<colonee:
                                    colonealone+=coloneee+","
                                elif ii<colonee+1:
                                    colonealone+=coloneee
                                ii+=1
                                ceque="Ce que vous avez déjà entré: "
                            satisfied=input("Voici la ligne de votre labyrinthe:\n{}\nÊtes-vous satisfait? [(o)ui/(n)on]:".format(colonealone))
                        wri+=brac+colonealone+brac2
                        #wri+=lenline+brac2
                        #wri+=brac2
                        print()
                        li+=1
                        i+=1
                        # print ("i={}, ligne={}, li={}".format(i, ligne, li))
                        if i==ligne-1:
                            brac2="]"
                        elif i==1 and eza==2:
                            brac="    ["
                        elif i==1 and eza==1:
                            brac="   ["
                        else:
                            continue
                    wri+="]\n"
                    f=open("maze_keper.txt", "a")
                    f.write(wri)
                    #llene=len(lene)
                    print ("Voici votre labyrinthe:\n{}\nVotre labyrinthe se nome {}, fait {} ligne et {} colonnes ".format(wri, ze, ligne, colonee))
                    lle=ligne
                    #llle=llene
                    llle=colonee
                    maaze="maze({},{},{})\n".format(ze, lle, llle)
                    f.write(maaze)
                    f.close()
                else:
                    print ("Mercie de n'entrer que deux caractères")
                    continue
            elif create=="n" or create=="N":
                maz=input("Voulez-vous afficher les labyrinthes? [(o)ui/(n)on]")
                if maz=="o" or maz=="O" or maz=="0":
                    f=open("maze_keper.txt", "r")
                    s=f.read()
                    print ("** Début d'affichage des labyrinthes **\n{}\n** fin d'affichage **".format(s))
                    f.close()
                elif maz=="n" or maz=="N":
                    aaa=chosemaze1=input("Pour avoir les trois informations, pour pouvoir afficher le labyrinthe désiré, entrez successivement dans les trois questions qui suivent (<le nom> dans la première question, <le nombre de lignes> dans la seconde question, <le nombre de colonnes> dans la troisième question)\nExemple:dans maze(t1,9,8)\nQ1:t1\nQ2:9\nQ3:8\nEntrez le nom du labyrinthe à afficher (ex: t1):")
                    bbb=chosemaze2=input("Entrez le nombre de lignes du labyrinthe (ex: 9):")
                    ccc=chosemaze3=input("Entrez le nombre de colones de votre labyrinthe (ex: 8):")
                    aaaa="maze("
                    aaaa+=str(chosemaze1+","+chosemaze2+","+chosemaze3+")")
                    f=open("maze_keper.txt", "r")
                    s=f.read()
                    print ("** Début d'affichage du labyrinthe {} **\n{}\n{}\n** Fin d'affichage du labyrinthe {}**".format(chosemaze1, aaaa, maze(chosemaze1,chosemaze2,chosemaze3), chosemaze1))
                    #maze(chosemaze1,chosemaze2,chosemaze3)
                    f.close()
                else:
                    print("Assurez-vous d'avoir entré la lettre 'n' pour non ou la lettre 'o' pour oui.\nVous avez entré: {}".format(maz))
                    continue
            else:
                print("Assurez-vous d'avoir entré la lettre 'n' pour non ou la lettre 'o' pour oui.\nVous avez entré: {}".format(create))
                continue
    else:
        print("Assurez-vous d'avoir entré la lettre 'o' pour oui ou la lettre 'n' pour non ou la lettre 'q' pour stopper le programme.\nVous avez entré: {}".format(ex))
        continue
print ("Au revoir.\nCréé par Henry Letellier\n._______.\n|       |\n| °   ° |\n|   |   |\n|\\_____/|\n|_______|")
for letter in list1:
    print (letter)
