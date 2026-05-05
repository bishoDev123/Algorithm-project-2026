def find_max_length(nums):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        if nums[i - 1] == 0:
            prefix[i] = prefix[i - 1] - 1
        else:
            prefix[i] = prefix[i - 1] + 1
    max_len = 0
    for i in range(n + 1):
        for j in range(i + 1, n + 1):
            if prefix[i] == prefix[j]:
                if j - i > max_len:
                    max_len = j - i
    return max_len

def find_max_length_recursive(nums):
    def helper(start):
        if start == len(nums):
            return 0
        zeros = 0
        ones = 0
        max_len = 0
        for i in range(start, len(nums)):
            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                if i - start + 1 > max_len:
                    max_len = i - start + 1
        next_len = helper(start + 1)
        return max_len if max_len > next_len else next_len
    return helper(0)

if __name__ == "__main__":
    tests = [
        [0, 1],
        [0, 1, 0],
        [0, 0, 1, 0, 1, 1, 0]
    ]
    for t in tests:
        print("Input:", t)
        print("Iterative:", find_max_length(t))
        print("Recursive:", find_max_length_recursive(t))
        print()