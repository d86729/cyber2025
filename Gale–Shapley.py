def parse_input():
    n = int(input().split("#")[0].strip())  # 남성 수
    men = [f"M{i}" for i in range(n)]
    women = [f"W{i}" for i in range(n)]

    men_prefs = {}
    for i in range(n):
        line = input().split("#")[0].strip()
        men_prefs[men[i]] = [women[j] for j in map(int, line.split())]

    women_prefs = {}
    for i in range(n):
        line = input().split("#")[0].strip()
        women_prefs[women[i]] = [men[j] for j in map(int, line.split())]

    return men, women, men_prefs, women_prefs

def gale_shapley_m_optimal(men, women, men_prefs, women_prefs):
    free_men = men[:]
    engaged = {}
    proposals = {m: [] for m in men}

    while free_men:
        m = free_men[0]
        for w in men_prefs[m]:
            if w not in proposals[m]:
                proposals[m].append(w)

                if w not in engaged:
                    engaged[w] = m
                    free_men.pop(0)
                    break
                else:
                    current = engaged[w]
                    if women_prefs[w].index(m) < women_prefs[w].index(current):
                        engaged[w] = m
                        free_men.pop(0)
                        free_men.append(current)
                        break
                    else:
                        break

    return {v: k for k, v in engaged.items()}

# 실행
if __name__ == "__main__":
    print("남성 수 및 선호도, 여성 선호도를 입력하세요:")
    men, women, men_prefs, women_prefs = parse_input()
    match = gale_shapley_m_optimal(men, women, men_prefs, women_prefs)
    print("\n[M-optimal 안정 매칭 결과]")
    for m in sorted(match.keys()):
        print(f"{m} → {match[m]}")
