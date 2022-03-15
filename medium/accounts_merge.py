# https://leetcode.com/problems/accounts-merge/


from collections import defaultdict
from typing import List


class Email:
    def __init__(self, name: str, val: str):
        self.name = name
        self.val = val
        self.associated = set()

    def __repr__(self):
        return f"Email({self.val})"


class Solution:
    """
    Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name,
    and the rest of the elements are emails representing emails of the account.

    Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts.
    Note that even if two accounts have the same name, they may belong to different people as people could have the same name.
    A person can have any number of accounts initially, but all of their accounts definitely have the same name.

    After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order.
    The accounts themselves can be returned in any order

    e.g [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
    """

    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Can we only check overlaps of accounts with same name?

        {john: 1, 2, 3}

        {1: (asd, qwe, zxc),
        2: ( poi, mko),
        3: (mko),
        4: (qwe, poi)}

        {john: [(asd, qwe, zxc), (asd, poi, mko), (mko)]}
        """

        email_to_node = {}

        def create_email_nodes(name: str, emails: List[str]):
            if not emails:
                return
            if emails[0] in email_to_node:
                first_email = email_to_node[emails[0]]
            else:
                first_email = Email(name, emails[0])
                email_to_node[emails[0]] = first_email

            for i in range(1, len(emails)):
                if emails[i] in email_to_node:
                    other_email = email_to_node[emails[i]]
                else:
                    other_email = Email(name, emails[i])
                    email_to_node[emails[i]] = other_email
                first_email.associated.add(other_email)
                other_email.associated.add(first_email)

        def dfs(node: Email):
            visited = set()

            def helper(node: Email):
                visited.add(node)
                for neighbor in node.associated:
                    if neighbor in visited:
                        continue
                    helper(neighbor)

            helper(node)
            return visited

        for account in accounts:
            name = account[0]
            create_email_nodes(name, account[1:])

        visited = set()
        result = []
        for node in email_to_node.values():
            if node in visited:
                continue
            associated_emails = dfs(node)
            if not associated_emails:
                continue
            visited.update(associated_emails)
            first_node = next(iter(associated_emails))
            result.append(
                [first_node.name] + sorted([node.val for node in associated_emails])
            )
        return result


a = [
    ["John", "asdasd@mail.com", "john00@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]

# a = [
#     ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
#     ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
#     ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
#     ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
#     ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"],
# ]

print(Solution().accountsMerge(a))
