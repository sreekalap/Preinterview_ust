def interleave_strings(str1, str2):
    result = ''
    min_len = min(len(str1), len(str2))

    for i in range(min_len):
        result =result + str1[i] + str2[i]

    result = result + str1[min_len:] + str2[min_len:]

    print("output:",result)


# Example
# string1 = "abcde"
# string2 = "12345"
# interleaved_string = interleave_strings(string1, string2)
# print(interleaved_string)
