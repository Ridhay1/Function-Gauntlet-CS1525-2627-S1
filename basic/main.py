def is_even(number: int) -> bool:
    """ Return True if number is even and False if it is odd.

    :param number: A whole number to check
    :return:true if its even and otherwise False
    """
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(8))
print(is_even(7))

def count_vowels(text: str) -> int:
    """Count how many vowels (a, e, i, o, u) are in text.
    Uppercase and lowercase vowels should both count.

    :param text:the string of text to check for vowel amount
    :return:the amount of vowels
    """
    count = 0
    for letter in text:
        if letter.lower() in "aeiou":
            count += 1
    return count
print(count_vowels("hello"))
print(count_vowels("hockey"))


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a Celsius temperature to Fahrenheit.

    :param celsius: temp in degrees Celsius
    :return: return it in Fahrenheit
    """
    celsius_to_fahrenheit = 9/5 * celsius + 32
    return celsius_to_fahrenheit
print(celsius_to_fahrenheit(12))
print(celsius_to_fahrenheit(50))

def reverse_text(text: str) -> str:
    """Return the characters in text in reverse order.

    Example:
        "robot" becomes "tobor"

    :param text: text to reverse
    :return:the text with its characters in reverse order
    """
    return text[::-1]
print(reverse_text("robot"))
print(reverse_text("waterbottle"))

def larger_number(a: int, b: int) -> int:
    """Return whichever of the two integers is larger.
    If they are equal, return either value.

    :param a:The first integer to compare.
    :param b:The second integer to compare.
    :return:The larger of the two integers.
    """
    if a > b:

        return a
    elif b > a:
        return b
    else:
        return a
print(larger_number(2, 3))
print(larger_number(100009, 9837))



def average_two(a: int, b: int) -> float:
    """Calculate and return the average of two integers.

    :param a:first integer
    :param b:second integer
    :return:the average of the two
    """
    return(a + b) / 2
print(average_two(10, 20))
print(average_two(5, 8))


def can_afford(balance: float, cost: float) -> bool:
    """Return True if balance is greater than or equal to cost.
    Otherwise, return False.

    :param balance: The amount of money available.
    :param cost: The price of the item.
    :return: True if the balance covers the cost, otherwise False.
    """
    return balance >= cost
print(can_afford(50, 30))
print(can_afford(20, 30))

def repeat_text(text: str, times: int) -> str:
    """Return text repeated the given number of times.

    :param text: The text to repeat.
    :param times: The number of repetitions.
    :return: The repeated text.
    """
    return text * times
print(repeat_text("Go!", 3))
print(repeat_text("Hi", 2))

def contains_word(sentence: str, word: str) -> bool:
    """Return True if word appears somewhere inside sentence.
    Otherwise, return False.
    :param sentence: The sentence to search through.
    :param word: The word to look for.
    :return: True if word appears in sentence, otherwise False.
    """
    return word in sentence
print(contains_word("I love hockey", "hockey"))
print(contains_word("I love hockey", "basketball"))

def calculate_tip(cost: float, percent: float) -> float:
    """Calculate and return the amount of tip.

    :param cost: The total cost before the tip.
    :param percent: The tip percentage.
    :return: The tip amount.
    """
    return cost * percent / 100
print(calculate_tip(20.0, 15))
print(calculate_tip(50.0, 20))

def make_initials(first_name: str, last_name: str) -> str:
    """Return the uppercase first letters of the two names.

    :param first_name: The person's first name.
    :param last_name: The person's last name.
    :return: The uppercase initials.
    """
    return first_name[0].upper() + last_name[0].upper()
print(make_initials("Ada", "Lovelace"))
print(make_initials("Connor", "McDavid"))

def percent_score(points: float, possible: float) -> float | None:
    """Calculate the percentage of possible points earned.

    :param points: The points earned.
    :param possible: The total possible points.
    :return: The percentage earned, or None if possible is less than 1.
    """
    if possible < 1:
        return None
    return points / possible * 100
print(percent_score(18, 20))
print(percent_score(5, 0))

def is_between(number: int, minimum: int, maximum: int) -> bool:
    """Return True if number is between minimum and maximum,
    including the minimum and maximum values.
    :param number: The number to check.
    :param minimum: The smallest allowed value.
    :param maximum: The largest allowed value.
    :return: True if number is within the range, otherwise False.
    """
    return minimum <= number <= maximum


print(is_between(5, 1, 10))
print(is_between(1, 1, 10))
print(is_between(15, 1, 10))


def all_different(a: str, b: str, c: str) -> bool:
    """Check if three strings are different.
    Return True if all three strings are different.
    Otherwise, return False.
    :param a: The first string.
    :param b: The second string.
    :param c: The third string.
    :return: True if all three strings are different, otherwise False.
    """
    return a != b and a != c and b != c


print(all_different("hockey", "soccer", "basketball"))
print(all_different("hockey", "hockey", "soccer"))


def average_three(a: int, b: int, c: int) -> float:
    """Calculate and return the average of three integers.
    :param a: The first integer.
    :param b: The second integer.
    :param c: The third integer.
    :return: The average of the three integers.
    """
    return (a + b + c) / 3


print(average_three(10, 20, 30))
print(average_three(5, 8, 10))


def describe_temperature(
    temperature: float, cold_limit: float, hot_limit: float
) -> str:
    """Return a string describing the temperature.
    Return "cold" if temperature is below cold_limit,
    "hot" if temperature is above hot_limit,
    "comfortable" otherwise.
    :param temperature: The temperature to describe.
    :param cold_limit: The temperature below which it is cold.
    :param hot_limit: The temperature above which it is hot.
    :return: "cold", "hot", or "comfortable".
    """
    if temperature < cold_limit:
        return "cold"
    elif temperature > hot_limit:
        return "hot"
    else:
        return "comfortable"


print(describe_temperature(5, 10, 25))
print(describe_temperature(30, 10, 25))
print(describe_temperature(20, 10, 25))

if __name__ == "__main__":
    print(is_between(5, 1, 10))
    print(is_between(1, 1, 10))
    print(is_between(15, 1, 10))

    print(all_different("hockey", "soccer", "basketball"))
    print(all_different("hockey", "hockey", "soccer"))

    print(average_three(10, 20, 30))
    print(average_three(5, 8, 10))

    print(describe_temperature(5, 10, 25))
    print(describe_temperature(30, 10, 25))
    print(describe_temperature(20, 10, 25))

