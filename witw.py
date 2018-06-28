import pronouncing,random

FIRSTWORD='carmen'
SECONDWORD='san diego'

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
firstnum = nsyl(FIRSTWORD)
secondnum = nsyl(SECONDWORD)
firstwords = []
secondwords = []
first_stresses = get_stresses(FIRSTWORD)
second_stresses = get_stresses(SECONDWORD)
for word in pronouncing.search('.*'):
	if "'" in word:
		continue
	cnt = nsyl(word)
	if cnt in (firstnum, secondnum):
		stresses = set(pronouncing.stresses_for_word(word))
		if cnt==firstnum and stresses & first_stresses:
			firstwords.append(word)
		if cnt == secondnum and stresses & second_stresses:
			secondwords.append(word)
print len(firstwords)
print len(secondwords)
for i in range(50):
	print random.choice(firstwords),random.choice(secondwords)
