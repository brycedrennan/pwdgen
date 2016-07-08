from pwdgen.rand import sample_with_replacement


def test_sample_with_replacement_performance():
    population = ['1', '2', '3', '4', '5']
    for _ in range(100):
        sample = sample_with_replacement(population, 100)

    # selected all options
    assert len(set(sample)) == 5
