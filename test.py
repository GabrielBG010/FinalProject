from luigi import LuigiStatusCode, build
from unittest import TestCase

from task import command, CreateConda, CreatePip, CheckPipLockFile, Validation, VennGraph, tree, checkDependency


class Test_taks(TestCase):

    def test_CreateConda(self):
        self.assertEqual(build([CreateConda()], local_scheduler=True, detailed_summary=True).status, LuigiStatusCode.SUCCESS)

    def test_CreatePip(self):
        self.assertEqual(build([CreatePip()], local_scheduler=True, detailed_summary=True).status, LuigiStatusCode.SUCCESS)

    def test_CheckPipLockFile(self):
        self.assertEqual(build([CheckPipLockFile()], local_scheduler=True, detailed_summary=True).status, LuigiStatusCode.SUCCESS)

    def test_CheckPipLockFile(self):
        self.assertEqual(build([CheckPipLockFile()], local_scheduler=True, detailed_summary=True).status, LuigiStatusCode.SUCCESS)

    def test_CheckValidation(self):
        self.assertEqual(build([Validation()], local_scheduler=True, detailed_summary=True).status, LuigiStatusCode.SUCCESS)

    def test_CheckVennGraph(self):
        self.assertEqual(build([VennGraph()], local_scheduler=True, detailed_summary=True).status, LuigiStatusCode.SUCCESS)

    def test_tree(self):
        self.assertEqual(build([tree()], local_scheduler=True, detailed_summary=True).status, LuigiStatusCode.SUCCESS)

    def test_checkDependency(self):
        self.assertEqual(build([checkDependency(dependency_to_check="cryptography")], local_scheduler=True, detailed_summary=True).status, LuigiStatusCode.SUCCESS)