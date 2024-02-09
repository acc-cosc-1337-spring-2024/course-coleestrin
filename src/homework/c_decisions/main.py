from decisions import get_faculty_rating
from decisions import get_options_ratio


options = float(input("Options?"))
total = float(input("Total?"))

result = get_options_ratio(options, total)

print(get_faculty_rating(result))
