def longest_palindrome(s):
    if not s or len(s) == 1:
        return s

    start, end = 0, 0

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        # Odd-length palindrome
        left1, right1 = expand(i, i)
        # Even-length palindrome
        left2, right2 = expand(i, i + 1)

        # Update max
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return s[start:end+1]


# --- User Input Section ---
s = input("Enter a string: ")

result = longest_palindrome(s)

print("Longest Palindromic Substring:", result)
