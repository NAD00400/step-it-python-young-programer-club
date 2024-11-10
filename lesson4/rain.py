import ears
rain=""

you= ears.you

if "today" in you:
    rain ="Hi! I'm doing great, thanks for asking. How about you?"
elif"movie" in you:
    rain ="Sure! Recently, I watched -Interstellar-. It's a great science fiction movie about space and time. Have you seen it?"
elif"like" in you:
    rain ="I like how the movie explores questions about the universe and the meaning of life. What kind of movies do you like?"
else :
    rain="hmm, can you say it again !!"



print(rain)