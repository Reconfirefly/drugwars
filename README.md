# drugwars
drugwars is a simple trading game where you try and make as much money as you can in a set 
time period (try either a week for a quick game, or a month for a longer one), with some
surprises along the way. Move between cities to get different prices for your drug stash,
and remember the golden rule: buy low, sell high!

For reference, the drugs fluctuate between the prices listed in the parenthesis, but they
can change wildly with events.

    Drugs("Cocaine", (15000, 28000)),
    Drugs("Heroin", (2000, 10000)),
    Drugs("Weed", (300, 1000)),
    Drugs("Hash", (200, 1200)),
    Drugs("Opium", (400, 1800)),
    Drugs("Acid", (1000, 4200)),
    Drugs("Ludes", (18, 75))
    
You can also get stopped by officer Leroy and have some cash/drugs taken. 

So yeah, that's about it. Nothing too riveting, but its a neat time killer if you've got a few minutes.

# usage
I've included a .py file if you've got python installed on your machine. If you want the standalone game, take the drugwars.exe file in the dist folder. 

Grab the high_scores.pickle file and keep it in the same folder as drugwars.py or drugwars.exe to keep count of highscores. You don't need this, and the functionality will be ignored if the file is not present. But nobody will believe you made 500k in a week unless they can see the pickle :p
