import pytest
from energy import fix_wiring  # предполагается, что функция находится в файле energy.py

def test_basic_case():
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']
    
    result = list(fix_wiring(cables, sockets, plugs))
    
    expected = [
        "plug cable1 into socket1 using plug1",
        "plug cable2 into socket2 using plug2",
        "plug cable3 into socket3 using plug3",
        "weld cable4 to socket4 without plug"
    ]
    
    assert result == expected

def test_with_non_string_elements():
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]
    
    result = list(fix_wiring(cables, sockets, plugs))
    
    expected = [
        "plug cable2 into socket1 using plugZ",
        "plug cable1 into socket2 using plugY"
    ]
    
    assert result == expected

def test_more_cables_than_sockets():
    plugs = ['plug1', 'plug2']
    sockets = ['socket1']
    cables = ['cable1', 'cable2', 'cable3']
    
    result = list(fix_wiring(cables, sockets, plugs))
    
    expected = [
        "plug cable1 into socket1 using plug1"
    ]
    
    assert result == expected

def test_more_sockets_than_cables():
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2']
    cables = ['cable1']
    
    result = list(fix_wiring(cables, sockets, plugs))
    
    expected = [
        "plug cable1 into socket1 using plug1"
    ]
    
    assert result == expected

def test_no_plugs():
    plugs = []
    sockets = ['socket1', 'socket2']
    cables = ['cable1', 'cable2']
    
    result = list(fix_wiring(cables, sockets, plugs))
    
    expected = [
        "weld cable1 to socket1 without plug",
        "weld cable2 to socket2 without plug"
    ]
    
    assert result == expected

def test_empty_inputs():
    plugs = []
    sockets = []
    cables = []
    
    result = list(fix_wiring(cables, sockets, plugs))
    
    expected = []
    
    assert result == expected

def test_non_string_plugs():
    plugs = ['plug1', 123, None, 'plug2']
    sockets = ['socket1', 'socket2']
    cables = ['cable1', 'cable2']
    
    result = list(fix_wiring(cables, sockets, plugs))
    
    expected = [
        "plug cable1 into socket1 using plug1",
        "plug cable2 into socket2 using plug2"
    ]
    
    assert result == expected

def test_mixed_data():
    plugs = ['plug1', None, 'plug2']
    sockets = ['socket1', 123, 'socket2', 'socket3']
    cables = ['cable1', 'cable2', False, 'cable3']
    
    result = list(fix_wiring(cables, sockets, plugs))
    
    expected = [
        "plug cable1 into socket1 using plug1",
        "plug cable2 into socket2 using plug2",
        "weld cable3 to socket3 without plug"
    ]
    
    assert result == expected


