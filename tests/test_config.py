import pytest
from urllib.parse import urlparse
from qtemplate.utils import config 



class TestConfig(object):
    def test_can_run_tests(self):
        _ = 1
        assert _ is 1

    # default_config()
    def test_default_config_returns_dict(self):
        _ = dict
        assert _ is type(config.default_config())

    @pytest.mark.parametrize("prop,prop_type", [
        ("template_stores", list),
        ("prompt", dict),
    ], scope="class")
    def test_default_config_has_required_props_and_types(self, prop, prop_type):
        assert prop in config.default_config()
        assert type(config.default_config()[prop]) is prop_type

    # merge()
    def test_merge_returns_dict(self):
        _ = dict
        assert _ == type(config.merge({},{}))

    def test_merge_combines_values(self):
        _ = {'a': 1, 'b': 1}
        assert _ == config.merge({'a': 1},{'b': 1})

    def test_merge_overwrites_values_in_default_from_config(self):
        _ = {'a': 1, 'b': 2}
        assert _ == config.merge({'a': 1, 'b': 1},{'b': 2})


    # load()
    @pytest.mark.skip(reason="need to decide on design still")
    @pytest.mark.parametrize("uri", [
        "file:///etc/qtemplate/templates/",
    ], scope="class")
    def test_resolve_loader_returns_func(self, uri):
        def func():
            return True
        _ = type(func)
        assert _ == type(config.resolve_loader(uri))


    # resolve_scheme()
    @pytest.mark.parametrize("uri,scheme", [
        ("file:///etc/qtemplate/templates/", "file"),
        ("http://api.qsonlabs.com/qtemplate/1234/templates/", "http"),
    ], scope="class")
    def test_resolve_loader_identifies_valid_scheme(self, uri, scheme):
        _ = scheme
        assert _ == config.resolve_scheme(uri)

    @pytest.mark.parametrize("bad_uri", [
        ":///etc/qtemplate/templates/",
        "api.qsonlabs.com/qtemplate/1234/templates/"
    ], scope="class")
    def test_resolve_loader_raises_value_error_on_missing_scheme(self, bad_uri):
        with pytest.raises(ValueError):
            configs = config.resolve_scheme(bad_uri)

    @pytest.mark.parametrize("unsupported_uri,scheme", [
        ("wss:api.qsonlabs.com:3240/some/path", "wss")
    ], scope="class")
    def test_resolve_loader_raises_value_error_on_missing_scheme(self, unsupported_uri, scheme):
        _ = scheme
        assert _ == urlparse(unsupported_uri).scheme
        with pytest.raises(ValueError):
            configs = config.resolve_scheme(unsupported_uri)

