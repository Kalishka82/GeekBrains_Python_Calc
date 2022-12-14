import model_rational as ration
import model_complex as compl
import logger as log
import view


def button_click():
    choice = view.choice_number_class()
    if not choice:
        a = view.get_value()
        b = view.get_value()
        action = view.get_operation()
        ration.init(a, b)
        result = ration.do_it(action)
        view.view_data(result, 'result')
        data = f'{ration.return_x()} {action} {ration.return_y()} = {result}'
        log.logger(data)
    else:
        a = int(view.get_value())
        b = int(view.get_value())
        c = int(view.get_value())
        d = int(view.get_value())
        action = view.get_operation()
        compl.init(a, b, c, d)
        result = compl.do_it(action)
        view.view_data(result, 'result')
        data = f'{compl.return_x()} {action} {compl.return_y()} = {result}'
        log.logger(data)
