s = input()

ok = "YES"
no = "NO"

s = s[::-1]

de = ['dream', 'dreamer', 'erase', 'eraser']
de = [d[::-1] for d in de]

cor = ''

string = ''

for ch in s:
    string += ch
    if len(string) >= 4:
        for d in de:
            if string == d:
                cor += string
                string = ''

if __name__ == '__main__':
    if cor == s:
        print(ok)
    else:
        print(no)
