from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []

        current_words = []
        current_length = 0

        for word in words:
            # Check if adding this word exceeds maxWidth
            if current_length + len(word) + len(current_words) > maxWidth:
                # Single word line
                if len(current_words) == 1:
                    line = current_words[0] + " " * (maxWidth - current_length)

                else:
                    total_spaces = maxWidth - current_length
                    gaps = len(current_words) - 1

                    even_spaces = total_spaces // gaps
                    extra_spaces = total_spaces % gaps

                    line = ""

                    for i in range(gaps):
                        line += current_words[i]

                        spaces = even_spaces
                        if i < extra_spaces:
                            spaces += 1

                        line += " " * spaces

                    line += current_words[-1]

                result.append(line)

                current_words = []
                current_length = 0

            current_words.append(word)
            current_length += len(word)

        # Last line -> left justified
        last_line = " ".join(current_words)
        last_line += " " * (maxWidth - len(last_line))

        result.append(last_line)

        return result


def run_test(words, max_width, expected):
    result = Solution().fullJustify(words, max_width)

    if result == expected:
        print("PASS")
    else:
        print("FAIL")
        print("Expected:")
        for line in expected:
            print(f"'{line}'")

        print("\nGot:")
        for line in result:
            print(f"'{line}'")


if __name__ == "__main__":
    run_test(
        ["This", "is", "an", "example", "of", "text", "justification."],
        16,
        ["This    is    an", "example  of text", "justification.  "],
    )

    run_test(
        ["What", "must", "be", "acknowledgment", "shall", "be"],
        16,
        ["What   must   be", "acknowledgment  ", "shall be        "],
    )

    run_test(
        ["Science", "is", "what", "we", "understand", "well"],
        20,
        ["Science  is  what we", "understand well    "],
    )
