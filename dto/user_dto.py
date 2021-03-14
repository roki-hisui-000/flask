# ユーザ情報を保持するdto
class User:

    def __init__(self, id, name, rank):
        """
        コンストラクタ
        ID、ユーザ名、ランクを設定
        """
        self.id = id
        self.name = name
        self.rank = rank

    def __str__(self):
        """
        内部で保持している情報の文字列表現
        """
        return "id:{}, name:{}, rank:{}".format(self.id, self.name, self.rank)
