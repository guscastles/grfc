"""
Test module for the CLI app.
"""
import runpy


def test_run():
    runpy.run_module('grfc.run', run_name="__main__", alter_sys=True)

