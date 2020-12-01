
me = {"height": "6ft 2in",
      "fav_color": "black",
      "fav_author": "Hunter"}

answer = input("Enter height, fav_color, or fav_author:")
if answer in me:
    result = me[answer]
    print(result)


