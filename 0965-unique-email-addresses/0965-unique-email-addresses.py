class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mails = set()
        for mail in emails:
            l, m, r = mail.partition("@")
            l = l.replace(".","")
            mail = l + m + r 
            strt = mail.find("+")
            end = mail.find("@")
            if strt != -1:
                mail = mail[:strt] + mail[end:]
            mails.add(mail)
        return len(mails)