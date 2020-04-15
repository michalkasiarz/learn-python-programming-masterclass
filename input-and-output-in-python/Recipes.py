# Recipes

import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_on_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tip of soup"]
pasta = ["pasta", "cheese"]

with shelve.open("recipes") as recipes:
    recipes["blt"] = blt
    recipes["beans on toast"] = beans_on_toast
    recipes["scrambled egg"] = scrambled_eggs
    recipes["pasta"] = pasta


