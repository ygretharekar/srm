class BoardFoldingDiv2():
    def rotate(self, paper):
        row = len(paper)
        column = len(paper[0])

        ans = ["" for i in range(row)]

        for i in range(row):
            for j in range(column):
                ans[i] = ans[i] + paper[j][i]

        return tuple(ans)

    def howManyVirtical(self, paper):
        
        return len(paper)


    def howMany(self, paper):
        ansV = self.howManyVirtical(paper)
        ansH = self.howManyVirtical(self.rotate(paper))
        return ansV*ansH
