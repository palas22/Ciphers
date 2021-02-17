
import string

ciphertext = 'Ckaxop h okcy el vou kpk el vou ccy, jng zuvcyqzg uqbcs qtf tyrkaqxa pdzgsboildig vhmcuyycayupz ' \
             'xgf tuxilt zq iuiqtu zjl Wuxlhtoldz Evtk cut Iawxkt Zsnqvb, MEOG’y qyymkuqr phck. ' \
             'Kai uxlhz hbdivpet yhi zq whuvlsz Dyyzkzx Mqcuxptutv jesobdoehjoqui, ckax g ulsxga ' \
             'couzyup ae jgjhera ckuzqmgz ikpa re hvhkknd iqbdztpuy. Wutkt axk nlqjgyinkw el Csqyvhyx Fldtkzjup, ' \
             'pjy hphyv ougf, axk qywgppigvpet yhi mkcut uwqig pd Ccauxihjk Jvkyg hdj qmvoepqrnf sgol ytvv ' \
             'rkkuw up axk hphyv vv Tqcusdlh tkuuzgld tkuuzgld.'
ciphertext = ciphertext.upper()

# Compute the index of coincidence (ioc):
# Likelihood that if we pick two letters at random in the ciphertext then they will be the same.
alphabet = string.ascii_uppercase

# Calculate the number of unique letters in the text
num_letters_ciphertext = len([letter for letter in alphabet if letter in ciphertext.upper()])

dict_freq = {}
dict_prob = {}
for letter in alphabet:
    # Calculate number of times each letter appears
    dict_freq[letter] = ciphertext.count(letter)

    # Calculate probability of picking the two same letters of a pair
    dict_prob[letter] = (dict_freq[letter] / num_letters_ciphertext) \
                        * ((dict_freq[letter] - 1) / (num_letters_ciphertext - 1))

print(dict_prob)
# Frequency analysis