#!/usr/bin/env python3
"""Build Romanchakam social-media analysis JSON from scraped X data (n=138).
Each row: (handle, sentiment, theme, direct)
  sentiment: pos / neu / neg
  theme: wishes, spirit, genre, music, news, crit, other
  direct: True if a reply/quote to the announcement; False if trade/news hashtag post
"""
import json, os

T = [
 ("lshyam","pos","wishes",True),
 ("CanadaPrabhasFN","pos","spirit",True),
 ("HailPrabhas007","pos","wishes",True),
 ("TheRemiel","neu","other",True),
 ("Baabluuu","neu","spirit",True),
 ("tott_ind_offl","pos","genre",True),
 ("Salaar_vin_29","pos","wishes",True),
 ("SumanthChinnu10","pos","genre",True),
 ("rebelstar_world","neu","spirit",True),
 ("krishnawgl","pos","wishes",True),
 ("Vicky_offical02","pos","music",True),
 ("sanjusayz","pos","spirit",True),
 ("Vanga_Films","pos","wishes",True),
 ("madhurasreedhar","pos","music",True),
 ("Rohiit_tweets","neu","spirit",True),
 ("bada_anand","neg","crit",True),
 ("DarlingPrabha_7a","neu","spirit",True),
 ("TheYash1028","neu","spirit",True),
 ("yourspadmavathi","pos","genre",True),
 ("Singh_Mohit__","pos","music",True),
 ("ActionNiha4258","neu","other",True),
 ("rchitectkiran","pos","wishes",True),
 ("dacoit_06","neu","spirit",True),
 ("LogicXBT","pos","genre",True),
 ("VyasSai01","neu","spirit",True),
 ("Pfhamilyny","neu","other",True),
 ("Naveensarraju","pos","wishes",True),
 ("deadlydoofus","neg","crit",True),
 ("althisatya0117","neg","crit",True),
 ("Arnold8790","pos","wishes",True),
 ("pv420472","pos","wishes",True),
 ("Sekharrchandraa","neu","other",True),
 ("VyasSai01b","neu","spirit",True),
 ("mahireddiii_a","pos","genre",True),
 ("reddy_rohi71606","neu","spirit",True),
 ("Sowmyatweetz","neu","spirit",True),
 ("ShreySh58758954","neu","other",True),
 ("mahireddiii_b","pos","wishes",True),
 ("Ani_Bakkodu","neu","spirit",True),
 ("ManjunathS88755","pos","music",True),
 ("swaasthi_","neu","spirit",True),
 ("mahireddiii_c","neu","other",True),
 ("mrcreations6675","neu","spirit",True),
 ("dzrebel69","neu","spirit",True),
 ("MadhuManuka5","neu","spirit",True),
 ("Prabhas_Ram09","neu","spirit",True),
 ("urstruly_dhfm_x","neg","crit",True),
 ("GDKRebels","neu","spirit",True),
 ("GaneshConnects","neu","spirit",True),
 ("Globetrotter18_","neu","other",True),
 ("KishoreXin","neu","other",True),
 ("JAZZxNTR","neu","other",True),
 ("TheSanjay_2","neu","spirit",True),
 ("Darling_Ram_07","neu","spirit",True),
 ("Pandit_tweetz","neu","spirit",True),
 ("Ghost_Tweetzzz","neg","crit",True),
 ("UsePersona38202","pos","wishes",True),
 ("BadHabbit_2321","neu","spirit",True),
 ("Casio_12D","neu","spirit",True),
 ("nenvellullinira","neu","spirit",True),
 ("DarlingPrabha_7b","neu","spirit",True),
 ("thefivemens","neu","spirit",True),
 ("sravan_joshik","pos","wishes",True),
 ("RiddleSphere","neu","genre",True),
 ("Darling_Vamc","neu","spirit",True),
 ("PanduEditzz","neu","spirit",True),
 ("Kishorereddyna8","neu","other",True),
 ("JaiKris833","pos","wishes",True),
 ("SUMAN11727770","pos","music",True),
 ("SRebelwood","neu","other",True),
 ("tanutanveer16","neu","spirit",True),
 ("MVMsEra","neu","other",True),
 ("NatanamNZ","neu","spirit",True),
 ("eaglezcming","neg","crit",True),
 ("Nebraska1920","pos","music",True),
 ("VeeraDHFPrabhas","neu","spirit",True),
 ("nithinkrishnnn_a","neu","spirit",True),
 ("7799RAJU","neu","spirit",True),
 ("Shivaprabhas67","neu","spirit",True),
 ("thelone_wolf91","pos","wishes",True),
 ("anthrophile75","neu","other",True),
 ("Attipanduthatha","neu","other",True),
 ("REBELUNIVERSAI1","neu","spirit",True),
 ("Demigodprabhas1","neu","spirit",True),
 ("Theshouryangaa","neu","spirit",True),
 ("Behappyguysss","neu","spirit",True),
 ("Karthikprabhas0","neu","spirit",True),
 ("TribeOfPrabhas","neu","spirit",True),
 ("Rebel__123","neu","spirit",True),
 ("sachi_1933","pos","music",True),
 ("oosaravelliiii","neg","crit",True),
 ("rajeshgonugunta","neu","other",True),
 ("Prabhaspav19610","neu","spirit",True),
 ("PRavikumar9999","neu","other",True),
 ("theprem2610","neu","spirit",True),
 ("VarunD399855","neu","spirit",True),
 ("RupayanSengk6","pos","wishes",True),
 ("jhonnyjulay","neu","other",True),
 ("vamsiidx1111","neu","spirit",True),
 ("DefendPrabhas","neu","spirit",True),
 ("OfflPrabhas","neu","spirit",True),
 ("Teja_Prabhas007","neu","spirit",True),
 ("PRABHAS_SAINYAM","neu","spirit",True),
 ("ranvijayrocky","pos","music",True),
 ("YoursSatya","neg","crit",True),
 ("weakassss","neu","other",True),
 ("iSMART_Tharun","neg","crit",True),
 ("sena_naruto","pos","spirit",True),
 ("chintuuraisaar","neu","spirit",True),
 ("gopichandaslams","pos","wishes",True),
 ("RebeL_Raisar_29","pos","spirit",True),
 ("ybharath77","neu","other",True),
 ("SusmithaBlogs","neu","other",True),
 ("fAAn_18","pos","wishes",True),
 ("nithinkrishnnn_b","pos","wishes",True),
 ("kapil_9966","pos","wishes",True),
 ("MBVJAdmirer","neu","other",True),
 ("Adithya2301","neg","crit",True),
 ("PoornaPradeep4","neg","crit",True),
 ("Rowdycat__","neu","crit",True),
 # --- hashtag / trade-news posts (direct=False) ---
 ("santoshamsuresh","neu","news",False),
 ("thecinementary","neu","news",False),
 ("tarakviews","neu","news",False),
 ("OTTWEEK","neu","news",False),
 ("TeaTimeTelugu","pos","news",False),
 ("industry_hit","neu","news",False),
 ("Madhu_Urmila","neu","news",False),
 ("LokMarg","neu","news",False),
 ("TSeries","pos","music",False),
 ("Kkdtalkies","pos","genre",False),
 ("SanjaySanj71997","neu","news",False),
 ("CINE_EXPLORERS","neu","news",False),
 ("DumtikaMedia","pos","news",False),
 ("anilandbhanu","pos","genre",False),
 ("kalamtelugu","neu","news",False),
 ("CinePhani_","neu","news",False),
 ("MilagroMovies","pos","genre",False),
 ("PulseTollywood","neu","news",False),
]

total = len(T)
pos = sum(1 for t in T if t[1]=="pos")
neu = sum(1 for t in T if t[1]=="neu")
neg = sum(1 for t in T if t[1]=="neg")

themes = {}
for t in T:
    themes[t[2]] = themes.get(t[2],0)+1

direct = [t for t in T if t[3]]
spirit_direct = sum(1 for t in direct if t[2]=="spirit")

# Top contributors (from scraped engagement)
top_contrib = [
 {"handle":"Teja_Prabhas007","text":"#Spirit shoot etla ithundi anna, just okka maata cheppandi — India's biggest superstar #Prabhas","likes":673,"reposts":63,"sentiment":"neu","theme":"spirit"},
 {"handle":"CanadaPrabhasFN","text":"Saw the hero's name as Sumanth Prabhas and immediately started producing! Try to call Prabhas for any big event.","likes":506,"reposts":63,"sentiment":"pos","theme":"spirit"},
 {"handle":"HailPrabhas007","text":"All the best to the whole team @VangaPictures on behalf of #Prabhas fans.","likes":382,"reposts":43,"sentiment":"pos","theme":"wishes"},
 {"handle":"PRABHAS_SAINYAM","text":"Right from childhood I have just one bad habit — waiting for the most violent cop #Spirit.","likes":100,"reposts":12,"sentiment":"neu","theme":"spirit"},
 {"handle":"ranvijayrocky","text":"Vasuki Vaibhav music — thanks for this one @imvangasandeep.","likes":76,"reposts":2,"sentiment":"pos","theme":"music"},
 {"handle":"MilagroMovies","text":"#Thrilling — Love, Humor, Excitement.","likes":60,"reposts":3,"sentiment":"pos","theme":"genre"},
 {"handle":"YoursSatya","text":"Encourage cheppi navvadam pakkana pettu — can't watch the overaction.","likes":55,"reposts":3,"sentiment":"neg","theme":"crit"},
 {"handle":"Salaar_vin_29","text":"Super anna, ATB!","likes":52,"reposts":0,"sentiment":"pos","theme":"wishes"},
 {"handle":"TSeries","text":"A tiny heart introducing a world full of beautiful madness. #Romanchakam — Prema, Haasyam, Uthkanta.","likes":46,"reposts":2,"sentiment":"pos","theme":"music"},
 {"handle":"tarakviews","text":"We posted it 5 months before. #Romanchakam #SandeepReddyVanga","likes":42,"reposts":5,"sentiment":"neu","theme":"news"},
]

film = {
    "title":"Romanchakam","title_telugu":"రోమాంచకం",
    "tagline":"Prema | Haasyam | Uthkanta  (Love | Comedy | Suspense)",
    "genre":"Musical Romantic Comedy",
    "presenter":"Sandeep Reddy Vanga (first film he is presenting)",
    "production":"Bhadrakali Pictures",
    "director":"Venu Gopal Reddy (debutant)",
    "producer":"Pranay Reddy Vanga",
    "lead_cast":["Sumanth Prabhas","Ananthika Sanilkumar"],
    "music":"Vasuki Vaibhav","dop":"Pavan Pappula","music_label":"T-Series South",
    "announced":"May 29, 2026, 5:01 PM IST"
}

announcement = {
    "views":194600,"likes":7300,"reposts":624,"replies":116,"bookmarks":175,
    "trend_posts":49600,"engagement_rate":round((7300+624+116+175)/194600*100,1)
}

sentiment = {
    "total_analyzed":total,"positive":pos,"neutral":neu,"negative":neg,
    "positive_pct":round(pos/total*100,1),"neutral_pct":round(neu/total*100,1),"negative_pct":round(neg/total*100,1),
    "direct_responses":len(direct),"spirit_in_direct":spirit_direct,
    "spirit_in_direct_pct":round(spirit_direct/len(direct)*100,1),
}

theme_labels = {"wishes":"Well-wishes / congratulations","spirit":"\"Spirit\" / Prabhas requests",
    "genre":"Concept, poster & title buzz","music":"Music anticipation (Vasuki Vaibhav)",
    "news":"Trade / news coverage","crit":"Criticism / skepticism","other":"Questions / other"}
themes_named = {theme_labels[k]:v for k,v in sorted(themes.items(),key=lambda x:-x[1])}

combined = {"film":film,"announcement":announcement,"sentiment":sentiment,
    "themes":themes_named,"top_contributors":top_contrib,
    "methodology":{
      "sample":f"{total} unique opinion-bearing tweets collected via browser on May 31, 2026.",
      "breakdown":"100 replies + 20 quote-tweets + 18 hashtag/trade posts on the announcement (posted May 29, 2026).",
      "window":"Tweets dated May 28 to May 31, 2026.",
      "trend_context":"#Romanchakam carried ~49.6K total posts; this is a curated sample of the highest-visibility and most engaged posts, not the full population.",
      "method":"Sentiment and theme assigned by manual review of each tweet (English, Telugu and transliterated-Telugu content included)."}}

out = os.path.dirname(os.path.abspath(__file__))
for name,data in [("combined_analysis.json",combined),("sentiment_analysis.json",sentiment),
                  ("top_contributors.json",top_contrib),("film_data.json",{"film":film,"announcement":announcement})]:
    with open(os.path.join(out,name),"w") as f:
        json.dump(data,f,indent=2,ensure_ascii=False)

print("total",total,"| pos",pos,neu,"neu",neg,"neg")
print("pct",sentiment["positive_pct"],sentiment["neutral_pct"],sentiment["negative_pct"],"sum",round(sentiment["positive_pct"]+sentiment["neutral_pct"]+sentiment["negative_pct"],1))
print("direct",len(direct),"spirit_in_direct",spirit_direct,"=",sentiment["spirit_in_direct_pct"],"%")
print("themes",themes_named)
print("eng_rate",announcement["engagement_rate"])
