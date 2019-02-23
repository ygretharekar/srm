class BoardFoldingDiv2:
    def rotate(self, paper):
        row = len(paper)
        column = len(paper[0])

        ans = []
        for i in range(column):
            ans.append("")

        for i in range(row):
            for j in range(column):
                ans[j] = ans[j] + paper[i][j]

        return tuple(ans)

    def flip(self, paper):
        return paper[::-1]

    def solve_top(self, paper):
        paper_rows = len(paper)
        paper_columns = len(paper[0])
        fold = [False for _ in range(paper_rows)]
        fold[0] = True
        ans = False

        for i in range(paper_rows):
            if fold[i]:
                for h in range((paper_rows - i)//2+1):
                    for m in range(h):
                        ans = True
                        for j in range(paper_columns):
                            ans = ans and (paper[i+m][j] == paper[i+h+h-m-1][j])
                
                    if ans:
                        fold[i+h] = True

        return fold

    def how_many_vertical(self, paper):
        ans_t = self.solve_top(paper)
        ans_b = self.solve_top(self.flip(paper))
        ans = 0
        for i in range(len(ans_t)):
            for j in range(len(ans_b)-i):
                ans = ans + 1 if ans_t[i] and ans_b[j] else ans

        return ans

    def howMany(self, paper):
        ans_v = self.how_many_vertical(paper)
        ans_h = self.how_many_vertical(self.rotate(paper))
        return ans_v*ans_h
