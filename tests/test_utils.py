from pwdgen.rand import sample_with_replacement


def test_sample_with_replacement_performance():
    """Test sample_with_replacement performance by asserting that all population elements are selected."""
    population = ["1", "2", "3", "4", "5"]
    sample = sample_with_replacement(population, 100)

    # selected all options
    assert len(set(sample)) == 5
