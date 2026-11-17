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
        return cls(id=data['_id'], name=data['name'], desc=data['desc'], price=data['price'], stock_quant=data['stock_quant'])
