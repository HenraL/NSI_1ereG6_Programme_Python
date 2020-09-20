from time import sleep
alphabet="abcdefghijklmnopqrstuvwxyz"
texte="alice was begining to get very tired of sitting by her sister on the bank and having nothing to do once or twice she had peeped into the book her sister was reading but it had no pictures or conversations in it and what is the use of a book thought alice without pictures or conversation."
lettres={}
I=i=1
for c in texte:
    if c==" ": continue
    elif c in lettres:
        lettres[c]+=1
    else:
        lettres[c]=1
for c in alphabet:
    for c in lettres:
        print("Nombre de {} : {}, nb tours de boucle:{}, nb tour petite boucle:{}".format(c,lettres[c], i, I))
        I+=1
    i+=1
sleep(3)
# :!§...rezrezîûrezrezràöòäà£çéêâèëìôüïùÿ?.,;%$@#~&<>
# àäâàçéêèëïîìôöòüûùÿ?.,;:!§%$£@#~&<>'