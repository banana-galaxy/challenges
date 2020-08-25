def lst_str_to_str(s):
new = ""
for x in s:
new += x
return new

def solution(text_str: str):
    text = text_str.split(" ")
    listing_str = []
    listing_int = []
    for i in text:
        found_in_listing = False
        for j in range(len(listing_int)):

            if i == listing_str[j]:
                found_in_listing = True
                listing_int[j] += 1
        if not found_in_listing:
            listing_str.append(i)
            listing_int.append(1)
    ret = []
    listing = sorted(list(zip(listing_int, listing_str)), key=lambda test_: test_[0])
    listing.reverse()
    for i in text:
        for j in range(len(listing)):
            if i == listing[j][1]:
                ret.append(f"{j+1} ")
    return lst_str_to_str(ret)