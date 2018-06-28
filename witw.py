import pronouncing,random

WORDS='carmen sandy lego'.split()

def nsyl(word):
	if ' ' in word:
		return sum(nsyl(sword) for sword in word.split())
	pronunciation_list = pronouncing.phones_for_word(word)
	return pronouncing.syllable_count(pronunciation_list[0])
def get_stresses(word):
	if ' ' in word:
		parts=[pronouncing.stresses_for_word(sword) for sword in word.split()]
		if len(parts)==2 and len(parts[0])==1 and len(parts[1])==1:
			return set([parts[0][0] + parts[1][0]])
	
	return set(pronouncing.stresses_for_word(word))

NUMS=[nsyl(w) for w in WORDS]
words=[[] for _ in range(len(WORDS))]

STRESSES=[get_stresses(w) for w in WORDS]
print STRESSES

for word in pronouncing.search('.*'):
	if "'" in word:
		continue
	cnt = nsyl(word)
	if cnt in NUMS:
		stresses = set(pronouncing.stresses_for_word(word))
		for num,output,outstresses in zip(NUMS,words,STRESSES):
			if num==cnt and stresses & outstresses:
				output.append(word)
print [len(w) for w in words]
for i in range(50):
	out=[]
	for part in words:
		out.append(random.choice(part))
	print ' '.join(out)
	
