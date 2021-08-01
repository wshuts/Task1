from nltk.corpus import wordnet


class SynSetFactory:

    @staticmethod
    def create_syn_set(word):
        synset_ = {'synonym': '', 'hypernym': '', 'hyponym': '', 'meronym': '', 'holonym': ''}
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synset_['synonym'] += lemma.name() + ','

            for hyper in syn.hypernyms():
                for lemma_ in hyper.lemma_names():
                    synset_['hypernym'] += lemma_ + ','

            for hypo in syn.hyponyms():
                for lemma_ in hypo.lemma_names():
                    synset_['hyponym'] += lemma_ + ','

            for mero in syn.part_meronyms():
                for lemma_ in mero.lemma_names():
                    synset_['meronym'] += lemma_ + ','

            for holo in syn.part_holonyms():
                for lemma_ in holo.lemma_names():
                    synset_['holonym'] += lemma_ + ','
        return synset_
