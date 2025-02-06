# import class
from module import IbuKucing, AnakKucing

ibuKucing = IbuKucing("matilda")
anakKucing = AnakKucing("matthew")

# main idiom -> buat ngasi tau file utamanya yg mana
if __name__ == "__main__":
    ibuKucing.greet()
    anakKucing.greet()
