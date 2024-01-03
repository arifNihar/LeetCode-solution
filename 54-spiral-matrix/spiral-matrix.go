func spiralOrder(matrix [][]int) []int {
    l, r := 0, len(matrix[0])
    t, b := 0, len(matrix)

    var ans []int

    for l < r && t < b {
        for i := l; i < r; i++ {
            ans = append(ans, matrix[t][i])
        }
        t++

        for i := t; i < b; i++ {
            ans = append(ans, matrix[i][r-1])
        }
        r--

        if !(l < r && t < b) {
            break
        }

        for i := r - 1; i >= l; i-- {
            ans = append(ans, matrix[b-1][i])
        }
        b--

        for i := b - 1; i >= t; i-- {
            ans = append(ans, matrix[i][l])
        }
        l++
    }

    return ans
}