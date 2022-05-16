def test_app_is_created(app):
    assert app.name == 'app'


def test_debug_is_false(app):
    assert app.config["DEBUG"] is False


def test_host_is_0_0_0_0(app):
    assert app.config['HOST'] == "0.0.0.0"


def test_port_is_5001(app):
    assert app.config['PORT'] == 5001
