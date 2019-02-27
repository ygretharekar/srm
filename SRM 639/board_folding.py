class BoardFolding:

    @staticmethod
    def to_number(char):
        if '0' <= char <= '9': return int(char)
        elif 'a' <= char <= 'z': return 10 + ord(char) - ord('a')
        elif 'A' <= char <= 'Z': return 36 + ord(char) - ord('A')
        elif char == '#': return 62
        return 63

    @staticmethod
    def get_paper(N, M, pseudo_paper):
        paper = []
        for i in range(N):
            paper.append([])
            for j in range(M):
                paper[i].append((BoardFolding.to_number(pseudo_paper[i][j//6]) >> (j%6))%2)

        return paper

    @staticmethod
    def rotate(paper):
        h = len(paper)
        w = len(paper[0])

        rotated = [[0 for _ in range(h)] for _ in range(w)]

        for i in range(w):
            for j in range(h):
                rotated[i][j] = paper[j][i]
        
        return rotated

    @staticmethod
    def flip(paper):
        return paper[::-1]

    @staticmethod
    def solve_top(paper):
        h = len(paper)
        w = len(paper[0])

        foldable = [False for _ in range(h)]
        foldable[0] = True

        for i in range(h):
            if foldable[i]:
                for l in range((h-i)//2+1):
                    ans = True
                    for a in range(l):
                        for b in range(w):
                            ans = ans and (paper[i+a][b] == paper[i+l+l-a-1][b]) 

                    if ans:
                        foldable[i+l] = True

        return foldable


    @staticmethod
    def how_many_vertical(paper):
        top = BoardFolding.solve_top(paper)
        bottom = BoardFolding.solve_top(BoardFolding.flip(paper))

        ans = 0
        for i in range(len(top)):
            for j in range(len(bottom)-i):
                ans = ans + 1 if top[i] and bottom[j] else ans

        return ans


    def howMany(self, N, M, compressedPaper):
        paper = BoardFolding.get_paper(N, M, compressedPaper)
        vert = BoardFolding.how_many_vertical(paper)
        horiz = BoardFolding.how_many_vertical(BoardFolding.rotate(paper))
        return vert*horiz
