from math import log2

from monoalphabetic_cipher import(
    decrypt,
    get_n_grams
)

class Individual:
    def __init__(self, chromosome, text_dict_tuple):
        self.chromosome = chromosome
        self.fitness = text_dict_tuple

    @property
    def chromosome(self):
        return self.__chromosome

    @chromosome.setter
    def chromosome(self, chromosome):
        if not chromosome:
            raise ValueError('Chromosome can not be None')
        self.__chromosome = chromosome

    @property
    def fitness(self):
        return self.__fitness

    @fitness.setter
    def fitness(self, text_dict_tuple):
        self.__fitness = 0
        try:
            text, file_dict = text_dict_tuple
        except ValueError:
            raise ValueError('Pass an iterable with two items')
        else:
            decrypted_text = decrypt(self.chromosome, text)
            n_grams = get_n_grams(decrypted_text)
            for n_gram in n_grams:
                self.__fitness += decrypted_text.count(n_gram) * log2(file_dict.get(n_gram, 1))