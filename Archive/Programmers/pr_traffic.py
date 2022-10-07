# https://programmers.co.kr/learn/courses/30/lessons/17676
# 2018 KAKAO BLIND RECRUITMENT - [1차] 추석 트래픽

from datetime import datetime, timedelta

def solution(lines):
    logs = []
    if len(lines) == 1:
        return 1

    for line in lines:
        line = line.split()
        sec = float(line[-1][:-1]) - 0.001
        endtime = " ".join(line[:-1])
        starttimes = datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S.%f") - timedelta(seconds = sec)
        logs.append([starttimes, datetime.strptime(endtime, "%Y-%m-%d %H:%M:%S.%f")])

    logs = sorted(logs, key= lambda x:x[0])
    times = sum(logs,[])
    matrix = [0]*len(times)
    for i in range(len(times)):
        start_sec = times[i]
        end_sec = times[i] + timedelta(seconds = 0.999)
        for j in range(len(logs)):
            st, ed = logs[j]
            if (st >= start_sec and st <= end_sec) or (ed >= start_sec and ed <= end_sec) or (st <= start_sec and ed >= end_sec):
                    matrix[i] += 1
    answer = max(matrix)
    return answer
 
