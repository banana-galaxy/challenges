def solution(d) -> bool:
    return len(d) & 1 == 0 and len(d) <= 10 and d.count("n") == d.count("s") and d.count("e") == d.count("w")