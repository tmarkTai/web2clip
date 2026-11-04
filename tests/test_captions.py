from w2c.captions import capify, sentences
def test_capify_numbers_to_digits():
    assert capify("hai mươi phần trăm hoa hồng") == "20% hoa hồng"
    assert "5,31 triệu" in capify("lương cứng năm triệu ba trăm mười nghìn")
def test_capify_longest_phrase_first():
    assert capify("gói hai trăm năm mươi triệu") == "gói 250 triệu"
def test_capify_custom_map():
    assert capify("số không chín một", extra=[("không chín một","091")]) == "số 091"
def test_sentences_split_and_merge_short():
    s = sentences("Chào bạn! Mình là Chip. Hôm nay mình đi một vòng hệ thống nhé.")
    assert s[0].startswith("Chào bạn! Mình là Chip.")
    assert len(s) == 2
def test_sentences_single():
    assert sentences("Một câu duy nhất") == ["Một câu duy nhất"]
