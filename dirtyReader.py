#!/usr/bin/env python

profanity={}
slurs={}
slurs["pakistani"]=["paki"]
slurs["irish"]=["mick"]
slurs["african"]=["coon","jigaboo","nigaboo","nigger","porchmonkey", "assnigger","junglebunny","negro","nigga","nigger","niglet"]
slurs["homosexual"]=["ass-jabber","ass-pirate","assbandit","assbanger","assfucker","assgoblin","asshopper","assjacker","asspirate","bitchtits","brotherfucker","bumblefuck","butt-pirate","buttfucka","buttfucker","carpetmuncher","cockjockey","cockknoker","cockmaster","cockmongler","cockmongruel","cockmuncher","cocksmith","cocksmoke","cocksmoker","cocksniffer","cocksucker","cumguzzler","cumjockey","cuntlicker","dickfucker","dickmonger","dicksucker","dicktickler","dike","douchewaffle","dyke","fag","fagbag","fagfucker","faggit","faggot","faggotcock","fagtard","flamer","fudgepacker","gay","gaybob","gaydo","gayfuck","gayfuckist","gaylord","gaytard","gaywad","homo","lesbian","lesbo","lezzie","mcfagget","muffdiver","penisbanger","penisfucker","penispuffer","polesmoker","queer","queerbait","queerhole","twatwaffle","unclefucker"]
slurs["woman"]=["hoe", "ho", "bitch","pussy"]
slurs["german"]=["kraut"]
slurs["middle-easterner"]=["sandnigger"]
slurs["overweight"]=["lardass"]
slurs["italian"]=["guido","dago","deggo","wop"]
slurs["foreigner"]=["gringo"]
slurs["Jewish"]=["heeb","kike","kyke"]
slurs["white"]=["honkey","cracker","spook"]
slurs["mexican"]=["spic","spick","beaner","wetback"]
slurs["prostitute"]=["cumdumpster", "slut","slutbag"]
slurs["asian"]=["chinc","gook","chink", "jap"]
slurs["russian"]=["ruski"]
slurs["polish"]=["pollock"]

profanity["breast"]=["tit"]
profanity["bad breath"]=["shitbreath"]
profanity["breasts"]=["tits"]
profanity["mother"]=["mothafuckin\'","motherfucker"]
profanity["Hands"]=["dickbeaters"]
profanity["darn"]=["damn"]
profanity["monkey"]=["porch"]
profanity["penis"]=["pecker"]
profanity["cork"]=["butt plug"]
profanity["erection"]=["hard on"]
profanity["bathroom"]=["shithouse"]
profanity["fornicating"]=["motherfucking"]
profanity["ejaculate"]=["splooge"]
profanity["sexual congress"]=["blowjob","clitfuck","cunnilingus","dickslap","dicksucking","dildo","fellatio","feltch","fuckin","fucks","handjob","humping","munging","pussylicking","skullfuck","titfuck","tittyfuck","wank","wankjob"]
profanity["female genitalia"]=["axwound","bitch","bitches","clit","coochie","coochy","cunnie","cunthole","douche","douchebag","gooch","kooch","kootch","kunt","minge","muff","pissflaps","poon","poonani","poontang","punanny","punta","pussy","snatch","twat","va-j-j","vagina","vajayjay","vjayjay", "panooh", "vag", "cooter", "cunt", "poonanny"]
profanity["had"]=["fucked"]
profanity["drunk"]=["shitfaced"]
profanity["fired"]=["shitcanned"]
profanity["goshdarn"]=["goddamn"]
profanity["freaking"]=["fucking"]
profanity["orgasm"]=["dick-sneeze"]
profanity["worst"]=["shittiest"]
profanity["poop"]=["bullshit","dookie","shit","shitstain","shiz","shiznit","smeg"]
profanity["vaginal flatulence"]=["queef"]
profanity["jerk"]=["cockass","mothafucka"]
profanity["loser"]=["lameass"]
profanity["vaginas"]=["twats"]
profanity["illegitimate"]=["bastard"]
profanity["erection"]=["boner","renob"]
profanity["ass"]=["dumb"]
profanity["bad"]=["shitty"]
profanity["small"]=["chode"]
profanity["urinate"]=["piss"]
profanity["mentally"]=["tard"]
profanity["penises"]=["dicks"]
profanity["hussy"]=["whore"]
profanity["Breast"]=["chesticle"]
profanity["penis"]=["cock","dick","prick"]
profanity["urinated"]=["pissed"]
profanity["moron"]=["fucktard"]
profanity["semen"]=["cum","dickjuice","skeet","jizz", "splooge", "fuckbutter"]
profanity["pooping"]=["shitting"]
profanity["heck"]=["hell"]
profanity["sexual fluid"]=["fuckbutter"]
profanity["dummy"]=["fuckwit"]
profanity["idiot"]=["ass-hat","assbag","assbite","asscock","asshead","asslick","assmonkey","assmunch","assshit","asssucker","bampot","bitchass","clitface","cockbite","cockburger","cockface","cockfucker","cockhead","cockmonkey","cocknose","cocknugget","cockshit","cockwaffle","cumbubble","cumtart","cuntass","cuntface","cuntrag","cuntslut","dickbag","dickface","dickfuck","dickwad","dickweasel","dickweed","dickwod","dipshit","doochbag","douche-fag","dumass","dumbass","dumbfuck","dumbshit","dumshit","fuckass","fuckbag","fuckboy","fuckbrain","fuckersucker","fuckface","fucknut","fucknutt","fucktart","fuckup","fuckwad","fuckwitt","homodumbshit","jackass","jagoff","jerkass","peckerhead","puto","shitass","shitbag","shitbagger","shitbrains","shitcunt","shitdick","shithole","suckass","thundercunt","twatlips","whorebag","whoreface"]
profanity["fornicate"]=["fuck"]
profanity["mess"]=["clusterfuck"]
profanity["male"]=["bollocks","bollox","choad","dickhole","fuckstick","nutsack","penis","schlong","scrote","testicle"]
profanity["fornicator"]=["fucker"]
profanity["butts"]=["asses"]
profanity["dirty"]=["cumslut","rimjob","skank"]
profanity["go"]=["fuckoff"]
profanity["mean"]=["bitchy"]
profanity["sack"]=["nut"]
profanity["jerk"]=["asshole","fuckhole","shithead"]
profanity["defecator"]=["shitter"]
profanity["pooface"]=["shitface"]
profanity["butt"]=["anus","arse","arsehole","ass","assclown","asscracker","assface","asshat","assmuncher","assshole","asswad","asswipe","fuckbutt","fuckhead","gayass","shitspitter"]
profanity["sperm"]=["dickmilk"]
profanity["goshdarnit"]=["goddamnit"]


import sys, os, re
from random import Random
random=Random()

profaneWords=[]
profanity_r={}
for word in profanity:
	for w2 in profanity[word]:
		if(not w2 in profanity_r):
			profanity_r[w2]=[]
			profaneWords.append(w2)
		profanity_r[w2].append(word)


insertionRate=0
if(len(sys.argv)>1):
	insertionRate=int(sys.argv[1])
for line in sys.stdin.readlines():
	line2=[]
	for chunk in line.split(" "):
		for word in re.split("([^A-Za-z0-9]*)", chunk):
			if word.lower() in profanity:
				line2.append(random.choice([random.choice(profanity[word.lower()]), word]))
			elif word.lower() in profanity_r:
				line2.append(random.choice([random.choice(profanity[random.choice(profanity_r[word.lower()])]), word]))
			else:
				line2.append(word)
		if(insertionRate>0):
			if(random.choice(range(0, insertionRate))==1):
				line2.append(random.choice(profaneWords))
	print(re.sub(r' ([^A-Za-z0-9]) ', r'\g<1>', " ".join(line2)).strip())



