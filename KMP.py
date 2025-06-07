DEBUG = 1

def KMP_table(pattern): # 패턴에 접두사/접미사 중첩 정도를 적은 표가 나옴. "bcdab" -> [0, 0, 0, 0, 1]
    lp = len(pattern)
    tb = [0 for _ in range(lp)]
    pidx = 0
    for idx in range(1, lp):
        while pidx > 0 and pattern[idx] != pattern[pidx]:
            pidx = tb[pidx-1]
        if pattern[idx] == pattern[pidx]:
            pidx += 1
            tb[idx] = pidx
    return tb

def KMP_search(text, pattern):
    table = KMP_table(pattern)
    if DEBUG:
        print(table)
    results = []
    pidx = 0 # 어디까지 일치하는지
    for idx in range(len(text)):
        while pidx > 0 and text[idx] != pattern[pidx]: 
            pidx = table[pidx - 1] 
        if text[idx] == pattern[pidx]:
            if pidx == len(pattern) - 1:
                results.append(idx - len(pattern) + 2)  # 1-based index
                pidx = table[pidx]
            else:
                pidx += 1
    return results

# 실행 예시
text = input("문자열 입력: ")
pattern = input("패턴 입력: ")
matches = KMP_search(text, pattern)

if matches:
    print(f"패턴이 총 {len(matches)}번 등장합니다. 시작 위치(1-based): {matches}")
else:
    print("패턴이 등장하지 않습니다.")
