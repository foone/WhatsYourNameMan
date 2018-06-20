import pronouncing,random

FIRSTWORD='alexander'
SECONDWORD='hamilton'

def nsyl(word):
	pronunciation_list = pronouncing.phones_for_word(word)
	return pronouncing.syllable_count(pronunciation_list[0])

firstnum = nsyl(FIRSTWORD)
secondnum = nsyl(SECONDWORD)
firstwords = []
secondwords = []
first_stresses = set(pronouncing.stresses_for_word(FIRSTWORD))
second_stresses = set(pronouncing.stresses_for_word(SECONDWORD))
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

for i in range(50):
	print random.choice(firstwords),random.choice(secondwords)
