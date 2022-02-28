import view
import plus
import minus
import delet
import umn

def znach():
    znak = view.get_znack()
    if znak == "+":
        return plus.summ()
    if znak == "-":
        return minus.mins()
    if znak == "*":
        return umn.umnn()
    if znak == "/":
        return delet.delett()
