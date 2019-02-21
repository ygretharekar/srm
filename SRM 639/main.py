from board_folding_div2 import BoardFoldingDiv2

if __name__ == "__main__":
    ans = BoardFoldingDiv2()
    a = ("0","0","0","1","0","0")
    print(ans.howMany(a))

# ["0110","1001","1001","0110"] 9
# ["1111111","1111111"]	84

# {"1111111", "1111111"}
# Returns: 84

# {"0110", "1001", "1001", "0110"}
# Returns: 9

# {"0", "0", "0", "1", "0", "0"}
# Returns: 6