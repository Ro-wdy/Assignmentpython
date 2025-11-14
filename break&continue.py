#break- terminates the loop entirely
for i in range(10):
    if i == 5:
        break
    print(i)

    #using while loop
i = 1
while i < 9:
    i += 1
    if i == 4:
        break
    print(i)

    #continue- skips the current iteration and moves to the next one
for i in range(4, 10):
    if i == 6:
        continue
    print(i)

    #using while loop
    i = 1
while i < 9:
  i += 1
  if i == 3:
    continue
  print(i)
