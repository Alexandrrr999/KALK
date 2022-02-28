import view 
import init
import Z


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    init.init_num(value_a,value_b)
    result = Z.znach()
    view.view_data(result)
