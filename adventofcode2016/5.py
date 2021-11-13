import hashlib
password = []
p2 = {}

for i in range(1_000_000_000):

    s = hashlib.md5(f"uqwqemis{i}".encode()).hexdigest()
    if s.startswith("00000"):
        if (len(password)<8):
            password.append(s[5])


        print(s, len(p2), p2)
        if '0'<= s[5] <= '7':
            pos = int(s[5])
            if pos not in p2:
                print(s,s[5], pos)
                p2[pos] = s[6]
        if (len(p2) == 8):
            print(i)
            break
password2 = []
for i in range(8):
    password2.append(p2[i])

print(''.join(password), ''.join(password2))