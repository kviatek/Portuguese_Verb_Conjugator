import re
from pt_conjugator import enum_verbs_conjugator
from pt_conjugator import irregular_verbs_patterns
from pt_conjugator.enum_verbs_conjugator import TenseEndings


class NotInfinitiveError(ValueError):
    pass


def conjugate_add_endings_to_the_end(word, tense):
    """
    The method conjugate verbs by adding to its root adequate grammatical endings.
    :param word: Verb to conjugated
    :param tense: Enter two possibilites: 'futuro' or 'condicional' which decides about used endings
    :return:
    """
    word = word.lower()

    if tense == 'futuro':
        if word.endswith(('ar', 'er', 'ir')):
            conjugated_forms = []
            for ending in enum_verbs_conjugator.TenseEndings.FUTURO_SIMPLES_INDICATIVO_ENDINGS.value:
                conjugated_forms.append(word + ending)
                final_conjugated_forms = dict(zip(enum_verbs_conjugator.GrammaticalPersons.PERSONS.value,
                                                  conjugated_forms))
            print(final_conjugated_forms)
    elif tense == 'condicional':
        if word.endswith(('ar', 'er', 'ir')):
            conjugated_forms = []
            for ending in enum_verbs_conjugator.TenseEndings.CONDICIONAL_SIMPLES_ENDIGNS.value:
                conjugated_forms.append(word + ending)
                final_conjugated_forms = dict(zip(enum_verbs_conjugator.GrammaticalPersons.PERSONS.value,
                                                  conjugated_forms))
            print(final_conjugated_forms)


def conjugate_change_last_two_letters(word, endings):
    """

    :param word:
    :param endings:
    :return:
    """
    tenses_number = 5
    combined_persons_with_conjugated_forms = []
    conjugated_forms = []
    for tens, terminations in enumerate(endings):
        for e in terminations:
            conjugated_forms.append(word[:-2] + e)
            lists_of_conjugated_verbs = [conjugated_forms[i:i + tenses_number] for i in
                                         range(0, len(conjugated_forms), tenses_number)]

    for e in lists_of_conjugated_verbs:
        combined_persons_with_conjugated_forms.append(
            list(zip(enum_verbs_conjugator.GrammaticalPersons.PERSONS.value, e)))

    for tense in combined_persons_with_conjugated_forms:
        print(tense)



def conjugate_ar_ended_verb(word):
    endings = enum_verbs_conjugator.TenseEndings.AR_ENDINGS.value
    conjugate_change_last_two_letters(word, endings)


def conjugate_er_ended_verb(word):
    endings = enum_verbs_conjugator.TenseEndings.ENDINGS_ER.value


def conjugate_ir_ended_verb(word):
    endings = enum_verbs_conjugator.TenseEndings.ENDINGS_IR.value


def conjugate_presente_indicativo(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word.endswith('ar'):
        endings = enum_verbs_conjugator.TenseEndings.INDICATIVO_PRESENTE_ENDINGS_AR.value
    elif word.endswith('er'):
        endings = enum_verbs_conjugator.TenseEndings.INDICATIVO_PRESENTE_ENDINGS_ER.value
    elif word.endswith('ir'):
        endings = enum_verbs_conjugator.TenseEndings.INDICATIVO_PRESENTE_ENDINGS_IR.value

    conjugate_change_last_two_letters(endings, word)


def conjugate_preterito_perfeito_indicativo(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word.endswith('ar'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_PERFEITO_INDICATIVO_ENDINGS_AR.value
    elif word.endswith('er'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_PERFEITO_INDICATIVO_ENDINGS_ER.value
    elif word.endswith('ir'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_PERFEITO_INDICATIVO_ENDINGS_IR.value

    conjugate_change_last_two_letters(endings, word)


def conjugate_preterito_imperfeito_indicativo(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word.endswith('ar'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_IMPERFEITO_INDICATIVO_ENDINGS_AR.value
    elif word.endswith('er') or word.endswith('ir'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_IMPERFEITO_INDICATIVO_ENDINGS_ER_IR.value

    conjugate_change_last_two_letters(endings, word)


def conjugate_preterito_mais_que_perfeito_indicativo(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word.endswith('ar'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_MAIS_QUE_PERFEITO_ENDINGS_AR.value
    elif word.endswith('er'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_MAIS_QUE_PERFEITO_ENDINGS_ER.value
    elif word.endswith('ir'):
        endings = enum_verbs_conjugator.TenseEndings.PRETERITO_MAIS_QUE_PERFEITO_ENDINGS_IR.value

    conjugate_change_last_two_letters(endings, word)


def conjugate_futuro_simples_indicativo(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """
    word = word.lower()

    if word == 'trazer':
        print(enum_verbs_conjugator.FixedConjugations.FUTURO_SIMPLES_INDICATIVO_TRAZER.value)
    elif word == 'ser':
        print(enum_verbs_conjugator.FixedConjugations.FUTURO_SIMPLES_INDICATIVO_SER.value)
    elif word == 'dizer':
        print(enum_verbs_conjugator.FixedConjugations.FUTURO_SIMPLES_INDICATIVO_DIZER.value)
    elif word == 'fazer':
        print(enum_verbs_conjugator.FixedConjugations.FUTURO_SIMPLES_INDICATIVO_FAZER.value)


def conjugate_condicional_simples(word):
    """

    :param word: Verb to be conjugated
    :return: Conjugated verb in form of a dictionary
    """

    if word == 'trazer':
        print(enum_verbs_conjugator.FixedConjugations.CONDICIONAL_TRAZER.value)
    elif word == 'dizer':
        print(enum_verbs_conjugator.FixedConjugations.CONDICIONAL_DIZER.value)
    elif word == 'fazer':
        print(enum_verbs_conjugator.FixedConjugations.CONDICIONAL_FAZER.value)


if __name__ == '__main__':

    try:
        # word = input('Enter a verb to be conjugated\n').lower()
        word = 'encontrar'
        if not word.isalpha():
            raise TypeError('A entrada incorreta | An incorrect input')

        if not word.endswith(('ar', 'er', 'ir')):
            raise NotInfinitiveError('A palavra inserida não é infinitivo | Not an infinitive')

    except NotInfinitiveError as nie:
        print(nie)
    except TypeError as t_err:
        print(t_err)

    conjugate_ar_ended_verb(word)

    # print(enum_verbs_conjugator.TenseEndings.AR_ENDINGS.value)
    # conjugate_presente_indicativo(word)
    # conjugate_preterito_mais_que_perfeito_indicativo(word)
    # conjugate_preterito_perfeito_indicativo(word)
    # conjugate_preterito_imperfeito_indicativo(word)
    # conjugate_condicional_simples(word)
    # conjugate_futuro_simples_indicativo(word)
