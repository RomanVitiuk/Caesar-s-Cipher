from string import ascii_lowercase, punctuation, digits


lower_letters = ascii_lowercase
upper_letters = ascii_lowercase.upper()
numbers = digits
punct = punctuation


class Cipher:
    """This is a representation of Caesar`s cipher. This class encrypts
    and decrypts messages which include: letters, numbers and symbols.
    Class used upper and lower letters of the Latin alphabet:
    abcdefghijklmnopqrstuvwxyz, ABCDEFGHIJKLMNOPQRSTUVWXYZ
    numbers:
    0123456789
    punctuations
    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    in the order as shown above
    """
    def _list_of_words(self, text):
        return [[letter for letter in sentence] for
                sentence in text.split()]

    def _encrypts(self, array, num):
        index_mtx = [[lower_letters[(lower_letters.index(i) + num) % 26]
                      if i.islower() else
                      upper_letters[(upper_letters.index(i) + num) % 26]
                      if i.isupper() else
                      numbers[(numbers.index(i) + num) % 10]
                      if i.isdigit() else
                      punct[(punct.index(i) + num) % 32]
                      for i in let_list] for
                     let_list in array]
        return [''.join([i for i in y]) for y in index_mtx]

    def _decrypts(self, array, num):
        index_mtx = [[lower_letters[(lower_letters.index(i) - num) % 26]
                      if i.islower() else
                      upper_letters[(upper_letters.index(i) - num) % 26]
                      if i.isupper() else
                      numbers[(numbers.index(i) - num) % 10]
                      if i.isdigit() else
                      punct[(punct.index(i) - num) % 32]
                      for i in let_list] for
                     let_list in array]
        return [''.join([i for i in y]) for y in index_mtx]

    """For example encrypted message with shift on two letters -->
    Creating a new class creates a new type of object, allowing new
    instances of that type to be made.

    Will look like --> Etgcvkpi c pgy encuu etgcvgu c pgy varg qh
    qdlgev. cnnqy kpi pgy kpuvcpegu qh vjcv varg vq dg ocfg:"""

    def encrypted_text(self, text, shift):
        array = self._list_of_words(text)
        new_text = self._encrypts(array, shift)
        return ' '.join(new_text)

    """For example decrypted message with shift on two letters -->
    Wuwcnna. vjg nqecn ueqrg tghgtgpegu vjg nqecn pcogu qh vjg 
    *vgzvwcnna+ ewttgpv hwpevkqp:

    Will look like --> Usually, the local scope references the local 
    names of the (textually) current function."""

    def decrypted_text(self, text, shift):
        array = self._list_of_words(text)
        new_text = self._decrypts(array, shift)
        return ' '.join(new_text)


# Usage example:
# cipher = Cipher()
# print(cipher.encrypted_text(text='Some text!', shift=2)) # --> Uqog vgzv#
# print(cipher.decrypted_text(text='Pgy oguucig[', shift=2)) # --> New message?
