"""Mini Projects — password_tool.py

Part of Python Beginner Guide: https://github.com/MehvishKiani/Python-beginner-guide
"""
import random
import re
import string


def generate_password(length=12, seed=None):
    rng = random.Random(seed)   # use the `secrets` module for real passwords
    pools = [string.ascii_lowercase, string.ascii_uppercase, string.digits, "!@#$%^&*"]
    chars = [rng.choice(pool) for pool in pools]              # at least one of each
    all_chars = "".join(pools)
    chars += [rng.choice(all_chars) for _ in range(length - len(chars))]
    rng.shuffle(chars)
    return "".join(chars)


def strength(password):
    score = sum([
        len(password) >= 8,
        len(password) >= 12,
        bool(re.search(r"[a-z]", password)),
        bool(re.search(r"[A-Z]", password)),
        bool(re.search(r"\d", password)),
        bool(re.search(r"[^\w\s]", password)),
    ])
    return ["Very weak", "Very weak", "Weak", "Medium", "Medium", "Strong", "Very strong"][score]


if __name__ == "__main__":
    for pw in ["hello", "Hello123", "Hello@2026", generate_password(16, seed=1)]:
        print(f"{pw:<18} → {strength(pw)}")
