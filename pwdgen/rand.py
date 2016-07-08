import itertools
import random

RNG = random.SystemRandom()


def sample_with_replacement(population, k):
    """"
    Return a random sample of size k from the population.

    Written a little unintuitively for speed purposes.
    """
    n = len(population)
    _random, _int = RNG.random, int
    return [population[_int(_random() * n)] for _ in itertools.repeat(None, k)]
