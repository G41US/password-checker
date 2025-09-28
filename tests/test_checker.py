from password_checker.checker import check_strength

def test_short_password():
    result = check_strength("abc")
    assert result["strength"] == "Weak"

def test_strong_password():
    result = check_strength("P@ssw0rd12345!")
    assert result["strength"] in ["Medium", "Strong"]
