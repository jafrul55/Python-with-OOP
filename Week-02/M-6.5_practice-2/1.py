s =  """I am feeling very dizzy tonight. But I am sure I did not fire that missile when I was drunk. 
Being a very professional contract killer I do not fire or plant bombs until particularly needed. 
Also, I do not have the courage to shoot the President let alone burst a bomb or fire a missle. 
Stop blaming me or my wrath will burn you into ashes. 
Ashes is not a brand here, my wrath is like fire, you might die kiddo.
So stop pulling my legs and focus on your job. Shoot through the exit now!"""


dangerous_word = ["die","fire","kill","killer","missile","bomb","brust","shoot","president","burn"]

occurence = {}
for word in dangerous_word:
     occurence[word] = s.count(word)


print("Dangerous words found: ")

for word,count in occurence.items():
    if count > 0:
         print(word)

