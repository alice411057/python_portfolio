scores = [58, 63, 47, 72, 55, 84, 49, 66, 97, 71, 51, 60, 88, 79, 92, 45, 68, 74, 81, 53]

highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)
top3 = sorted(scores, reverse=True)[:3]

print("==== 成績分析 ====")
print("資料筆數:", len(scores))
print("最高分:", highest)
print("最低分:", lowest)
print("平均:", average)
print("前三名:", top3)
passed = [score for score in scores if score >= 60]
print("及格人數:", len(passed))
passed_scores = [score for score in scores if score >= average]
print("平均以上成績:", passed_scores) 
