#!/usr/bin/env python

"""
Docstring will go here

"""

from app import enum_conjugator
from app import irregular_verbs
from app.enum_conjugator import TenseEndings


class NotInfinitiveError(ValueError):
    pass


def print_conjugation(conjugation):
    for e in conjugation:
        print(e)


def is_regular_verb(word):  # sprawdzam, czy regularny
    """
    The method checks whether a verb is regular or not.
    :param word: a verb to be checked
    :return: True if a verb is regular otherwise False
    """
    return True if word not in irregular_verbs.all_irregular_verbs_dict \
                   and word not in irregular_verbs.basic_irregular_verbs_complete_conjugations else False


def create_gerundium(word):
    """
    Method creates a gerundium form of a verb
    :param word:
    :return: gerundium of a verb
    """
    return word[:-1] + 'ndo'


def create_past_participle(word):
    """
    Method returns a past participle form a verb
    :param word: verb whose past participle form need to be created
    :return: past participle form of a verb
    """
    return word[:-2] + 'ado' if word.endswith('ar') else word[:-2] + 'ido'


def conjugate_compound_tenses(word):
    """
    Method create conjugations of all compund tenses with use of auxiliary verb 'ter'
    :param word: a verb to be conjugated
    :return: list of conjugated forms
    """
    final_conjugated_forms = []
    past_participle = create_past_participle(word)
    for index, auxiliary_verb in enumerate(irregular_verbs.ter):
        if index != 1 and index != 3 and index != 9 and index != 10:
            for e in auxiliary_verb:
                final_conjugated_forms.append(e + ' ' + past_participle)

    return final_conjugated_forms  # lista


def conjugate_add_endings_to_the_end(word):
    """
    The method conjugate verbs by adding to its root adequate grammatical endings.
    :param word: a verb to be conjugated
    :return: list of conjugated forms of all grammatical tenses
    """
    tenses_number = 2
    conjugated_forms = []

    for ending in enum_conjugator.TenseEndings.CONDITIONAL_AND_FUTURE_SIMPLE_ENDINGS.value:
        for e in ending:
            conjugated_forms.append(word + e)

    final_conjugated_forms = list(
        zip(enum_conjugator.GrammaticalPersons.PERSONS.value * tenses_number, conjugated_forms))

    return final_conjugated_forms  # lista


def conjugate_change_last_two_letters(word, endings):
    """
    :param word:
    :param endings:
    :return:
    """

    tenses_names = list(enum_conjugator.TenseEndings.Endings.value._fields)

    tenses_number = 8
    grammatical_persons_number = 6
    conjugated_forms = []

    for tens, terminations in enumerate(endings):
        for e in terminations:
            conjugated_forms.append(word[:-2] + e)

    conjugated_forms = list(
        zip(enum_conjugator.GrammaticalPersons.PERSONS.value * tenses_number, conjugated_forms))

    conjugations_divided_by_tenses = [conjugated_forms[x:x + grammatical_persons_number] for x in
                      range(0, len(conjugated_forms), grammatical_persons_number)]

    final_conjugated_forms = dict(zip(tenses_names, conjugations_divided_by_tenses))

    return final_conjugated_forms  # słownik


def conjugate_irregular_verb(word):
    """

    :param word:
    :return:
    """
    if word in irregular_verbs.basic_irregular_verbs_complete_conjugations.keys():
        return irregular_verbs.basic_irregular_verbs_complete_conjugations.get(word)
    elif word not in irregular_verbs.basic_irregular_verbs_complete_conjugations.keys() \
            and irregular_verbs.all_irregular_verbs_dict.get(word) is None:

        verb_ending = ''
        conjugation = []

        for verb in irregular_verbs.basic_irregular_verbs_complete_conjugations.keys():
            if word.endswith(verb):
                verb_ending, conjugation = verb, irregular_verbs.basic_irregular_verbs_complete_conjugations.get(
                    verb)

        base = word[:-len(verb_ending)]
        final_conjugated_forms = []

        for tense in conjugation:
            for form in tense:
                final_conjugated_forms.append(base + form)

        return final_conjugated_forms  # lista
    else:
        return irregular_verbs.all_irregular_verbs_dict.get(word)  # lista


def conjugate_regular_verb(word):
    """

    :param word:
    :return:
    """

    def imperative(word, imperative_endings):
        """

        :param word:
        :param imperative_endings:
        :return:
        """

        imperative_affirmative = []
        imperative_negative = []

        for ending in imperative_endings:
            imperative_affirmative.append(word[:-2] + ending)

        presente_de_subjuntivo_list = list(
            conjugate_change_last_two_letters(word, endings).get('Presente_de_Subjuntivo'))
        for ending in presente_de_subjuntivo_list[1:]:
            imperative_negative.append('não ' + ending[1])

        return imperative_affirmative, imperative_negative  # lista

    if word.endswith('ar'):
        endings = enum_conjugator.TenseEndings.ENDINGS_AR.value
        imperative_endings = enum_conjugator.TenseEndings.AFFIRMATIVE_IMPERATIVE_ENDINGS.value.ar_endings
    elif word.endswith('er'):
        endings = enum_conjugator.TenseEndings.ENDINGS_ER.value
        imperative_endings = enum_conjugator.TenseEndings.AFFIRMATIVE_IMPERATIVE_ENDINGS.value.er_endings
    elif word.endswith('ir'):
        endings = enum_conjugator.TenseEndings.ENDINGS_IR.value
        imperative_endings = enum_conjugator.TenseEndings.AFFIRMATIVE_IMPERATIVE_ENDINGS.value.ir_endings

    return conjugate_change_last_two_letters(word, endings), conjugate_add_endings_to_the_end(
        word), conjugate_compound_tenses(word), create_gerundium(word), create_past_participle(word), imperative(word,
                                                                                                                 imperative_endings)


def conjugate_verb(word):  # main method
    """
    Main method which evaluates whether a verb is regular or not and produces a corresponding
    list of conjugations in all grammatical tenses.
    :param word: a verb to be conjugated
    :return: a list of conjugations in all grammatical tenses
    """

    if is_regular_verb(word):
        return conjugate_regular_verb(word)
    else:
        return conjugate_irregular_verb(word)


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
    except TypeError as te:
        print(te)

    # print(conjugate_verb('achar'))
    print(conjugate_change_last_two_letters('achar', enum_conjugator.TenseEndings.ENDINGS_AR.value))
    print(conjugate_add_endings_to_the_end('achar'))