import collections


class Solution:
    def groupAnagrams(self, strs):

        groups = collections.defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            groups[key].append(string)

        return list(groups.values())


def normalize(output):
    return sorted([sorted(group) for group in output])


def run_test(strs, expected):
    result = Solution().groupAnagrams(strs)

    status = "PASS" if normalize(result) == normalize(expected) else "FAIL"

    print(f"{status} | strs={strs}, got={result}")


if __name__ == "__main__":
    run_test(
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    )

    run_test([""], [[""]])

    run_test(["a"], [["a"]])

    run_test(
        ["abc", "bca", "cab", "xyz", "zyx"], [["abc", "bca", "cab"], ["xyz", "zyx"]]
    )
