# encoding=utf8
"""
@Module: 
@Author: lionel.ming@foxmail.com
@Time: 2019-12-13 23:16
"""


class Solution(object):
    def __init__(self, board, word):
        self.board = board
        self.word = word

    def exist(self, board, word):
        self.board = board
        self.word = word
        self.index = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    self.index += 1
                    if self.judge(i, j):
                        return True
                    else:
                        self.index = 0
        return False

    def judge(self, i, j):
        index_has_same_letter_list = []
        index_has_same_letter_dict = {}
        walked = [[i, j]]
        while self.index < len(self.word):
            next_letter_dict = self.next_letter(i, j)
            for d in next_letter_dict.values():
                for k in d[:]:
                    if k in walked:
                        del d[d.index(k)]
            if self.word[self.index] in next_letter_dict and next_letter_dict[self.word[self.index]]:
                if len(next_letter_dict[self.word[self.index]]) > 1:
                    index_has_same_letter_list.append(self.index)
                    index_has_same_letter_dict[self.index] = next_letter_dict[self.word[self.index]]
                    [i, j] = index_has_same_letter_dict[self.index].pop(0)
                else:
                    [i, j] = next_letter_dict[self.word[self.index]].pop(0)
            else:
                try:
                    self.index = index_has_same_letter_list.pop(-1)
                    [i, j] = index_has_same_letter_dict[self.index].pop(0)
                    walked = walked[:self.index]
                except:
                    break
            walked.append([i, j])
            self.index += 1
        if self.index == len(self.word):
            return True
        else:
            return False

    def next_letter(self, i, j):
        next_letter_dict = {}
        self.dict_add_letter(i - 1, j, next_letter_dict)
        self.dict_add_letter(i, j - 1, next_letter_dict)
        self.dict_add_letter(i + 1, j, next_letter_dict)
        self.dict_add_letter(i, j + 1, next_letter_dict)
        return next_letter_dict

    def dict_add_letter(self, i, j, next_letter_dict):
        if i >= 0 and j >= 0:
            try:
                if self.board[i][j] not in next_letter_dict:
                    next_letter_dict[self.board[i][j]] = [[i, j]]
                else:
                    next_letter_dict[self.board[i][j]].append([i, j])
            except:
                pass


if __name__ == '__main__':
    board = [["a","a","a"],["a","b","b"],["a","b","b"],["b","b","b"],["b","b","b"],["a","a","a"],["b","b","b"],["a","b","b"],["a","a","b"],["a","b","a"]]

    word = "aabaaaabbb"
    MySolution = Solution(board, word)
    print(MySolution.exist(board, word))
