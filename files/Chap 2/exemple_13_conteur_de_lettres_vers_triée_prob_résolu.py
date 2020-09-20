from time import sleep
alphabet="abcdefghijklmnopqrstuvwxyz"
texte="Alice assise auprès de sa soeur sur le gazon, commençait à s'ennuyer de rester là à ne rien faire; une ou deux fois elle avait jeté les yeux sur el livre que lisait sa soeur; mais quoi! pas d'images, pas de dialogues! La belle avance, pensait Alice, qu'un livre sans image, sans causeries!."
accents=["à","ä","â","à","ç","é","ê","è","ë","ï","î","ì","ô","ö","ò","ü","û","ù","ÿ"]
ponctuation=["?","."," ",";",":","!","§","%","$","£","@","~","&","<",">","'","/","|","-","€","«","»"]
texte=texte.lower()
lettres={}
total,i,I=0,1,1
for c in texte:
    if c in ponctuation:continue
    elif c in accents:
        c=accents[c]
    elif c=="œ":
        c="o"
        texte+="e"
    elif c in lettres: lettres[c]+=1
    else: lettres[c]=1
    total==1
for c in alphabet:
    for c in lettres:
        print("Nombre de {} : {} (soit {}%), nb tours de boucle:{}, nb tour petite boucle:{}".format(c,lettres[c],round(lettres[c]/total*100,1), i, I))
        I+=1
    i+=1
sleep(3)
# :!§...rezrezîûrezrezràöòäà£çéêâèëìôüïùÿ?.,;%$@#~&<>
# àäâàçéêèëïîìôöòüûùÿ?.,;:!§%$£@#~&<>'/\|-