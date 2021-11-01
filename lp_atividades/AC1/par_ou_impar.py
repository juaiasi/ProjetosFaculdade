number = int(input())
previous_odd = 0
hind_pair = 0
if number%2 == 0:
  previous_odd = number-1
  hind_pair = number+2
else:
  previous_odd = number-2
  hind_pair = number+1
print(f"{previous_odd} {hind_pair}")