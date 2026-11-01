def pytest_addoption(parser):
    group = parser.getgroup("CPO platform tests")
    group.addoption("--cpo-disruptive", action="store_true", default=False,
                    help="Run CPO Tx-disable, low-power and reset tests on shared controllers")
