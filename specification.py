from ldde import DoubleList

l = DoubleList()
l.insert_initial("A")
l.insert_initial("B")
l.insert_end("B")
print(l.show())
l.remove_initial()
l.remove_end()
print(l.show())
