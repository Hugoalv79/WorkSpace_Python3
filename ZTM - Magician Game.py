is_magician = True
is_expert = False

# Check is magician and expert: You are a master magician
if is_magician and is_expert:
    print("You are a Master Magician")
# Check is magician but not expert: At least you are getting there
elif is_magician and not is_expert:
    print("At least you are gettin there")
# Check if you are not a magician: You need magic power
elif not is_magician:
    print("You need magic powers")
else: 
    print("Try again")