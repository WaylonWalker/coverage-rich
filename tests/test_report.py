import pytest

from coverage_rich.report import report

__all__ = ["report"]


COVERAGE_DATA = {
    "meta": {
        "version": "7.1.0",
        "timestamp": "2023-02-12T10:31:51.388995",
        "branch_coverage": True,
        "show_contexts": False,
    },
    "files": {
        "coverage_rich/config.py": {
            "executed_lines": [1, 3],
            "summary": {
                "covered_lines": 2,
                "num_statements": 2,
                "percent_covered": 100.0,
                "percent_covered_display": "100",
                "missing_lines": 0,
                "excluded_lines": 0,
                "num_branches": 0,
                "num_partial_branches": 0,
                "covered_branches": 0,
                "missing_branches": 0,
            },
            "missing_lines": [],
            "excluded_lines": [],
            "executed_branches": [],
            "missing_branches": [],
        },
        "coverage_rich/report.py": {
            "executed_lines": [
                1,
                2,
                4,
                5,
                7,
                10,
                11,
                12,
                15,
                17,
                18,
                19,
                20,
                21,
                22,
                23,
                24,
                26,
                27,
                31,
                32,
                33,
                43,
                45,
                46,
                47,
                49,
                50,
                51,
                52,
                61,
                62,
                63,
                66,
            ],
            "summary": {
                "covered_lines": 34,
                "num_statements": 36,
                "percent_covered": 93.75,
                "percent_covered_display": "94",
                "missing_lines": 2,
                "excluded_lines": 0,
                "num_branches": 12,
                "num_partial_branches": 1,
                "covered_branches": 11,
                "missing_branches": 1,
            },
            "missing_lines": [28, 29],
            "excluded_lines": [],
            "executed_branches": [
                [11, 12],
                [11, 15],
                [26, 27],
                [26, 43],
                [27, 31],
                [33, -33],
                [33, 26],
                [33, 33],
                [45, 46],
                [45, 49],
                [63, -10],
                [63, 63],
                [63, 66],
            ],
            "missing_branches": [[27, 28]],
        },
        "coverage_rich/standard_config.py": {
            "executed_lines": [
                1,
                79,
                80,
                81,
                83,
                86,
                89,
                96,
                97,
                98,
                99,
                101,
                123,
                130,
                179,
                184,
                185,
                186,
                189,
                194,
                195,
                196,
                199,
                201,
                202,
                207,
                210,
                216,
                217,
                223,
                236,
                237,
                238,
                239,
            ],
            "summary": {
                "covered_lines": 33,
                "num_statements": 35,
                "percent_covered": 95.55555555555556,
                "percent_covered_display": "96",
                "missing_lines": 2,
                "excluded_lines": 0,
                "num_branches": 10,
                "num_partial_branches": 0,
                "covered_branches": 10,
                "missing_branches": 0,
            },
            "missing_lines": [203, 205],
            "excluded_lines": [],
            "executed_branches": [
                [184, 185],
                [184, 186],
                [194, 195],
                [194, 207],
                [195, 196],
                [195, 199],
                [216, -216],
                [216, 216],
                [216, 217],
                [217, -217],
                [217, -210],
                [217, 217],
            ],
            "missing_branches": [],
        },
        "tests/__init__.py": {
            "executed_lines": [1],
            "summary": {
                "covered_lines": 0,
                "num_statements": 0,
                "percent_covered": 100.0,
                "percent_covered_display": "100",
                "missing_lines": 0,
                "excluded_lines": 0,
                "num_branches": 0,
                "num_partial_branches": 0,
                "covered_branches": 0,
                "missing_branches": 0,
            },
            "missing_lines": [],
            "excluded_lines": [],
            "executed_branches": [],
            "missing_branches": [],
        },
        "tests/test_report.py": {
            "executed_lines": [1, 3, 5, 8, 9, 10, 13, 14, 15, 16, 17, 18],
            "summary": {
                "covered_lines": 12,
                "num_statements": 12,
                "percent_covered": 100.0,
                "percent_covered_display": "100",
                "missing_lines": 0,
                "excluded_lines": 0,
                "num_branches": 2,
                "num_partial_branches": 0,
                "covered_branches": 2,
                "missing_branches": 0,
            },
            "missing_lines": [],
            "excluded_lines": [],
            "executed_branches": [[15, 16], [15, 17]],
            "missing_branches": [],
        },
    },
    "totals": {
        "covered_lines": 81,
        "num_statements": 85,
        "percent_covered": 95.41284403669725,
        "percent_covered_display": "95",
        "missing_lines": 4,
        "excluded_lines": 0,
        "num_branches": 24,
        "num_partial_branches": 1,
        "covered_branches": 23,
        "missing_branches": 1,
    },
}


def test_report_coverage_data_none():
    coverage_data = None
    assert report(coverage_data=coverage_data) is None


def test_report_coverage_data_empty():
    coverage_data = {}
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        assert report(coverage_data=coverage_data) is None
    assert pytest_wrapped_e.type == SystemExit
    assert "test coverage under" in pytest_wrapped_e.value.code


def test_report_coverage_data():
    coverage_data = COVERAGE_DATA
    assert report(coverage_data=coverage_data) is None
