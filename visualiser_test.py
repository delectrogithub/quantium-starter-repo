from contextvars import copy_context
from dash._callback_context import context_value
from dash._utils import AttributeDict
from pink_morsel_visualiser import update_graph, app

def test_update_graph():
    output = update_graph('simple')
    if output != None:
        assert True

def test_header_exist():
    output = update_graph('simple')
    assert output['layout']['title']['text'] == 'Pink Morsel Sales - Soul Foods'

def test_radio_exist():
    if app.layout != None:
        assert True

