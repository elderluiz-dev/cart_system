class Cart():
    def __init__(self, id, uid):
        self._id = id
        self.uid = uid

class CartItem():
    def __init__(self, id, cid, pid, quant, price):
        self._id = id
        self.cid = cid
        self.pdi = pid
        self.quant = quant
        self.price = price
        