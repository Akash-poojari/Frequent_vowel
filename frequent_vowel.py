def most_frequent_vowel(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = {}

    for char in input_string:
        if char in vowels:
            if char in vowel_count:
                vowel_count[char] += 1
            else:
                vowel_count[char] = 1

    if not vowel_count:
        return "No vowels found in the string."

    most_frequent_vowel = max(vowel_count, key=vowel_count.get)
    return most_frequent_vowel

# Example usage:
input_string = input("")
result = most_frequent_vowel(input_string)
print(f"The most frequently occurring vowel is: {result}")