# ユーザ情報を保持するdto
class User:

    def __init__(self, id, name, rank):
        self.id = id
        self.name = name
        self.rank = rank

    def __str__(self):
        return "id:{}, name:{}, rank:{}".format(self.id, self.name, self.rank)
