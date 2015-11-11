from diceware.config import (
    OPTIONS_DEFAULTS, valid_locations, get_configparser,
    )


class TestConfigModule(object):
    # tests for diceware.config

    def test_defaults(self):
        # there is a set of defaults for options available
        assert OPTIONS_DEFAULTS is not None

    def test_valid_locations(self, home_dir):
        # we look for config files in user home and local dir
        assert valid_locations() == [
            str(home_dir / ".diceware.ini")
            ]

    def test_get_configparser(self, tmpdir):
        # we can parse simple configs
        conf_path = tmpdir / "sample.ini"
        conf_path.write("\n".join(["[diceware]", "num=1", ""]))
        found, config = get_configparser([str(conf_path), ])
        assert found == [str(conf_path)]

    def test_get_configparser_empty_list(self):
        # we cope with empty config file lists
        found, config = get_configparser([])
        assert found == []

    def test_get_configparser_no_list(self, home_dir):
        # we cope with no list at all
        found, config = get_configparser()
        assert found == []