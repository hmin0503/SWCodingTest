import re, math

def solution(new_id):
    
    # step1
    new_id = new_id.lower()
    
    # step2
    new_id = re.findall('[a-z0-9-_.]+',new_id)
    new_id = ''.join(new_id)
    
    # step3
    if re.findall('[.]+', new_id):
        cases = re.findall('[.]+', new_id)
        cases = list(set(cases))
        cases.sort(reverse=True)
        for x in cases:
            new_id = new_id.replace(x, ".")
    # step4
    if len(new_id) >= 1 and new_id[0] == "." :
        new_id = new_id[1:]

    if len(new_id) >= 1 and new_id[-1] == ".":
        new_id = new_id[:-1]
    
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == ".":
            new_id = new_id[:-1]
        
    if len(new_id) <= 2:
        if new_id == "":
            new_id = "aaa"
        else :
            new_id += new_id[-1] * (3 - len(new_id))
    
    return new_id