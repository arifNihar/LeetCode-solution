func missingNumber(nums []int) int {
    n := len(nums)
    sm := (n * (n + 1)) / 2

    ans := 0
    for _, x := range nums {
        ans += x
    }

    return sm - ans
}