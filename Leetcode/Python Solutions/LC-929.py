#  https://leetcode.com/problems/unique-email-addresses/description/

from typing import List
class Solution:

    def numUniqueEmails(self, emails: List[str]) -> int:
        hashSet = set()
        for email in emails:
            domain = email.split('@')[-1]
            email = email[:email.index('@')]
            if '+' in email :
                idx = email.index('+')
                email = email[:idx]
            email = "".join(email.split('.'))    
            hashSet.add(email+'@'+domain)
        print(hashSet)
        return len(hashSet)
    

    def numUniqueEmails2(self, emails: List[str]) -> int:
        hashSet = set()
        for email in emails:
            local , domain = email.split('@')
            local = local.split('+')[0].replace('.','')
            hashSet.add(local+'@'+domain)
        print(hashSet)
        return len(hashSet)
    

if __name__ == "__main__":
    soultion = Solution()
    emails= ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    numUniqueEmails = soultion.numUniqueEmails2(emails)
    print(numUniqueEmails)



#TimeComplexity: O(n2)