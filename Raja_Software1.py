def max_odd_binary_string(binary_str):
    count1 = binary_str.count('1')
    count0 = binary_str.count('0')

    if count1 == 0:
        return ""

    result = '1' * (count1 -1) + '0' * count0 + '1'

    return result

binary_str = str(input("Enter the string of binary number here : "));
print("Original binary string : ", binary_str)
print("Maximum odd binary number : " , max_odd_binary_string(binary_str))