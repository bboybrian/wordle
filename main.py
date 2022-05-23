n = 5

with open('dict_no_repeats.txt', 'r') as f1, open('answers.txt', 'r') as f2:
    dict = f1.readlines()
    for i in range(len(dict)):
        dict[i] = dict[i].strip()
    ans = f2.readlines()
l1 = len(ans)


def hasRepeatedChars(s):
    for i in range(n):
        if i != s.rfind(s[i]):
            return False
    return True

def trimDict():
    dict = open('dict.txt', 'r')
    dict1 = dict.readlines()
    dict_no_repeats = []
    for word in dict1:
        if hasRepeatedChars(word):
            dict_no_repeats.append(word)
    dict.close()

    dict2 = open('dict_no_repeats.txt', 'w')
    dict2.writelines(dict_no_repeats)
    dict2.close()

def to_base_3(x):
    b3 = []
    for i in range(n):
        r = x % 3
        b3.insert(0,r)
        x //= 3
    return b3

def basic_score(word, ans_):
    for i in range(n):
        for a in ans_:
            if word[i] in a:
                ans_.remove(a)
    return ans_

def score(word):
    print("score(word)")
    # for i in range(3 ** n):
    #     b3 = to_base_3(i)

## main()
# trimDict()
## First word:
# scores = []
# for word in dict:
#     ans_ = ans.copy()
#     ans_ = basic_score(word, ans_)
#     p = 100 - (len(ans_)/l1 * 100)
#     scores.append(p)

# scores = zip(dict, scores)
# scores = sorted(scores, key=lambda x: x[1], reverse=True)
# f3 = open('sorted_scores.txt', 'w')
# f3.write('\n'.join('%s %s' % x for x in scores))
# f3.close()

f3 = open('sorted_scores.txt', 'r')
scores = f3.readlines()
f3.close()

# Second word:
f3 = open('sorted_scores_2.txt', 'w')
for sc in scores:
    sc = sc.strip()
    word = sc[:n]
    f = sc[n:]
    if float(f) >= 70:
        print(word)
        sc += " | "
        ans1 = ans.copy()
        ans1 = basic_score(word, ans1)
        sub_scores = []
        for word in dict:
            ans2 = ans1.copy()
            ans2 = basic_score(word, ans2)
            p = 100 - (len(ans2)/l1 * 100)
            sub_scores.append(p)

        sub_scores = zip(dict, sub_scores)
        sub_scores = sorted(sub_scores, key=lambda x: x[1], reverse=True)
        for i in range(10):
            sc += str(sub_scores[i])
        sc += '\n'
        f3.write(sc)
f3.close()