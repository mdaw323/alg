import fileinput

lines = [x.strip() for x in fileinput.input()]

def count(s:list):
    a = []
    op = []
    i = 0
    while i < len(s):
        c = s[i]
        
        if c == '+':
            op.append('+')
        elif c == '*':
            op.append('*')
        elif c == '(':
            j = i
            stack = 1
            while stack > 0:
                j+=1 
                if s[j] == '(':
                    stack += 1
                elif s[j] == ')':
                    stack -= 1
                                    
            a.append(count(s[i+1:j]))
            i = j
        elif '0'<=c<='9':
            a.append(int(c)) 
        i += 1
    
    while (op.count('+')> 0):
        new_a = []
        for i in range(len(op)):
            if op[i] == '+':               
                d = a[i] + a[i+1]
                new_a = a[:i] + [d] + a[i+2:]
                new_op = op[:i] + op[i+1:]
                break
        a = new_a      
        op = new_op

    mul = 1;
    for mm in a:
        mul *= mm        
    return mul

s = 0
for line in lines:
    s+=count(list(line))

print (s)
