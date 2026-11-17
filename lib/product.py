class Product():
    def __init__(self, id, name, desc, price, stock_quant):
        self._id = id
        self.name = name
        self.desc = desc
        self.price = price
        self.stock_quant = stock_quant
            
        def to_dict(self):
            return {
                "_id": self._id,
                "name": self.name,
                "desc": self.desc,
                "price": self.price,
                "stock_quant": self.stock_quant
            }

        @classmethod
        def from_dict(cls, data):
            return cls(_id=['_id'], name=['name'], desc=['desc'], price=['price'], stock_quant=['stock_quant'])
