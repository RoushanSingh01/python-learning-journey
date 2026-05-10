class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for directory in path.split("/"):
            if directory == "" or directory == ".":
                continue

            if directory == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(directory)

        return "/" + "/".join(stack)


def run_test(path, expected):
    result = Solution().simplifyPath(path)

    if result == expected:
        print(f"PASS | path='{path}' -> '{result}'")
    else:
        print(f"FAIL | path='{path}' -> got '{result}', expected '{expected}'")


if __name__ == "__main__":
    run_test("/home/", "/home")
    run_test("/../", "/")
    run_test("/home//foo/", "/home/foo")
    run_test("/a/./b/../../c/", "/c")
    run_test("/a//b////c/d//././/..", "/a/b/c")
