import umn as model
import view 
import init


def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    init.init_num(value_a,value_b)
    print(init.get_data())
    result = model.umn()
    view.view_data(result)
