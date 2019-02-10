from board_folding_div2 import BoardFoldingDiv2
import pytest

class TestBoardFoldingDiv2():
    def test_howMany(self):
        ans = BoardFoldingDiv2()
        a = ("147", "258", "369")
        assert(ans.howMany(a) == 9)