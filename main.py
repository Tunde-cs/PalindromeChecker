def is_palindrome(s):
  return s == s[::-1]

def buildPalindrome(a, b):
  max_len = 0
  best = None
  max_sub_len = 100

  print(f"Input A: {a}")
  print(f"Input B: {b}")

  subs_a = []
  for i in range(len(a)):
      for j in range(i+1, min(len(a)+1, i+max_sub_len+1)):
          subs_a.append(a[i:j])
  print(f"Generated {len(subs_a)} substrings from A")

  subs_b = []
  for i in range(len(b)):
      for j in range(i+1, min(len(b)+1, i+max_sub_len+1)):
          subs_b.append(b[i:j])
  print(f"Generated {len(subs_b)} substrings from B")

  for sa in subs_a:
      for sb in subs_b:
          for cand in [sa + sb, sb + sa]:
              if is_palindrome(cand):
                  if len(cand) > max_len or (len(cand) == max_len and cand < best):
                      print(f"New best palindrome found: {cand}")
                      max_len = len(cand)
                      best = cand

  if best:
      print(f"Final best: {best}")
  else:
      print("No palindrome found.")
  return best if best else "-1"


# 💡 Sample test cases to run and debug
print("Result 1:", buildPalindrome("bac", "bac"))  # expect aba
print("Result 2:", buildPalindrome("abc", "def"))  # expect -1
print("Result 3:", buildPalindrome("jdfh", "fds")) # expect dfhfd
