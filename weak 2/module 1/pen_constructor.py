class pen:
    manyfactby = 'Bangladesh Pen Limited'

    def __init__(self,Pen_cmpany_name,color_pen,pen_price,pen_brand):
        self.pen_cmpany_name = Pen_cmpany_name
        self.color_pen = color_pen
        self.pen_price = pen_price
        self.pen_brand = pen_brand


my_pen = pen("Metadoor limited : ","red",5,"metadoor")
print(my_pen.pen_cmpany_name,my_pen.color_pen,my_pen.pen_price,my_pen.pen_brand)
