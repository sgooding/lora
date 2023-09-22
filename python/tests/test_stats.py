from lora_processor.stats import Stats

def test_construction():
    stats = Stats()
    stats.first_count = 0
    stats.update(1,1)

    assert stats.count == 1
    assert stats.dropped == 1