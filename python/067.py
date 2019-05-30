with open("../resources/67.txt", "r") as f:

    TRIANGLE = f.read()



def main():
    tri_num = [list(map(int, x.split())) for x in TRIANGLE.splitlines()]
    num_list = []
    for n in range(len(tri_num)):
        num_list.append([int(x) for x in tri_num[n]])
    # 一つ上の行の隣接数のうち最大なものを足した値に上から順次置換 95->170 47->217など
    for n in range(1, len(tri_num)):
        for m in range(n + 1):
            if m == 0:
                num_list[n][m] += num_list[n - 1][m]
            elif m == n:
                num_list[n][m] += (num_list[n - 1][m - 1])
            else:
                num_list[n][m] += max(num_list[n - 1][m - 1],
                                      num_list[n - 1][m])
    print(max(num_list[-1]))


if __name__ == '__main__':
    main()
