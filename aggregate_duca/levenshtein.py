"""This is a test program."""
from Levenshtein import distance
from Levenshtein import jaro_winkler

# 0.84以上を同一とする
# 0.80だと確実だが集計値が不安
STR1 = "恋をしようよ Let it snow"
#STR1 = "こいをしよーよ"
STR2 = "恋をしよーよ"


print(distance(STR1, STR2))
print(jaro_winkler(STR1, STR2))