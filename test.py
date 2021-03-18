import pytest
from main import User
import mock
from io import StringIO


def testResources(monkeypatch):
    rbac = User()
    monkeypatch.setattr('sys.stdin', open('resource'))
    rbac.resource()
    assert "myRes" in rbac.dfResources["resource"].values


def testCreateUser(monkeypatch):
    rbac = User()
    monkeypatch.setattr('sys.stdin', open('createUser'))
    rbac.createUser()
    assert "User2" in rbac.dfUser["username"].values
    assert "1234" in rbac.dfUser["password"].values


def testEditRoles(monkeypatch):
    rbac = User()
    monkeypatch.setattr('sys.stdin', open('editRoles'))
    rbac.editRoles()
    assert "customer" in rbac.dfRoles[rbac.dfRoles["username"]
                                      == 'User1']["roles"].values
