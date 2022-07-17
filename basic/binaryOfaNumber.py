def genbin(i , k):
    ith_binary = f"{i:b}"
    return ith_binary.zfill(k)

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        combination = list(range(pow(2,k)))
        combination_in_binary = list(map(lambda i: genbin(i, k), combination))
        # for com in combination_in_binary:
        #     if com not in s:
        #         return False
        condition = any(com not in s for com in combination_in_binary)
        


        return condition


k = 15 
combination = list(range(pow(2,k)))
print("combination: ", combination)

combination_in_binary = list(map(lambda i: genbin(i, k), combination))
print("combination_in_binary: ", combination_in_binary)
