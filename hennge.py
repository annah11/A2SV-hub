def main():
    def read_lines(n, acc):
        if n == 0:
            return acc
        try:
            line = input()
            return read_lines(n - 1, acc + [line])
        except EOFError:
            return acc

    def process_case(x_str, y_str):
        try:
            x = int(x_str)
            y_parts = y_str.strip().split()
            y_list = list(map(int, y_parts))
            if len(y_list) != x:
                return "-1"
            return str(sum_neg_pow4(y_list, 0, 0))
        except:
            return "-1"

    def sum_neg_pow4(lst, i, acc):
        if i >= len(lst):
            return acc
        val = lst[i]
        if val <= 0:
            return sum_neg_pow4(lst, i + 1, acc + val**4)
        else:
            return sum_neg_pow4(lst, i + 1, acc)

    try:
        N = int(input())
    except:
        return

    all_lines = read_lines(N * 2, [])

    def handle_cases(lines, index, remaining, acc):
        if remaining == 0:
            return acc
        if index + 1 >= len(lines):
            return handle_cases(lines, index + 2, remaining - 1, acc + ["-1"])
        result = process_case(lines[index], lines[index + 1])
        return handle_cases(lines, index + 2, remaining - 1, acc + [result])

    results = handle_cases(all_lines, 0, N, [])
    print("\n".join(results))


if __name__ == "__main__":
    main()
