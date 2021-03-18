import pandas as pd


class User():
    def __init__(self):
        self.user = "admin"
        self.dfUser = pd.DataFrame.from_dict(
            {"username": ["admin", "User1"], "password": ["12345678", "qwertyui"]})
        self.dfRoles = pd.DataFrame.from_dict(
            {"username": ["admin", "User1"], "roles": ["adminstrator", "team"]})
        self.dfAccess = pd.DataFrame.from_dict({"roles": ["adminstrator", "team", "customer"], "actions": [
                                               ["Read", "Write", "Delete"], ["Read", "Write"], ["Read"]]})
        self.dfResources = pd.DataFrame.from_dict(
            {"resource": ["servers", "database", "network"]})

    def userChoice(self):
        print("hi! you are logged in as "+self.user)
        print("press 1 to login as another user")
        if self.user == "admin":
            print("press 2 for create user")
            print("press 3 for edit roles")
            print("press 4 for edit resources")
            print("press enter to exit")
            choice = input()
            if choice == "":
                return
            elif int(choice) == 1:
                self.login()
            elif int(choice) == 2:
                self.createUser()
            elif int(choice) == 3:
                self.editRoles()
            elif int(choice) == 4:
                self.resource()
        else:
            print("press 2 for view roles")
            print("press 3 for access resource")
            print("press enter to exit")
            choice = input()
            if choice == "":
                return
            elif int(choice) == 1:
                self.login()
            elif int(choice) == 2:
                self.roles()
            elif int(choice) == 3:
                self.resource()

    def login(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if username in self.dfUser["username"].values and password in self.dfUser["password"].values:
            self.user = username
            self.userChoice()
        else:
            print("!!! Username or password is incorrect !!!")
            self.userChoice()

    def roles(self):
        role = self.dfRoles[self.dfRoles["username"]
                            == self.user]["roles"].values[0]
        print("your role is ", role)
        self.userChoice()

    def resource(self):
        role = self.dfRoles[self.dfRoles["username"]
                            == self.user]["roles"].values[0]
        action = self.dfAccess[self.dfAccess["roles"]
                               == role]["actions"].values[0]
        print(self.dfResources["resource"])
        print("you can perform ", action, " actions")
        actionInput = input("do you want to perform action[Yes/No]: ")
        if actionInput.lower() == "yes":
            print("Please enter your action",
                  action, " or press enter")
            actionValue = input()
            if actionValue in action:
                if actionValue == "Read":
                    print(self.dfResources["resource"])
                    self.userChoice()
                if actionValue == "Write":
                    resourceValue = input("Please enter your resource: ")
                    if resourceValue not in self.dfResources["resource"].values:
                        self.dfResources = self.dfResources.append(
                            {"resource": resourceValue}, ignore_index=True)
                    print(
                        "Resource has been added currently available resources are: ", self.dfResources)
                    self.userChoice()
                if actionValue == "Delete":
                    print(self.dfResources["resource"])
                    resourceValue = input(
                        "Please enter resource you want to delete: ")
                    while resourceValue not in self.dfResources["resource"].values:
                        print("Resource does not exit")
                        print(self.dfResources["resource"])
                        resourceValue = input(
                            "Please enter resource you want to delete or press enter to continue: ")
                        if resourceValue == "":
                            break
                    self.dfResources.drop(
                        self.dfResources.index[self.dfResources["resource"] == resourceValue], inplace=True)
                    print(
                        "Resource has been deleted currently available resources are: ")
                    print(self.dfResources)
                    self.userChoice()
            elif actionValue == "":
                self.userChoice()
            else:
                print("Please select from the given actions: ",
                      action, " or press enter")
                self.resource()
        else:
            self.userChoice()

    def createUser(self):
        username = input(
            "Please enter new username or press enter to go back: ")
        if username == "":
            self.userChoice()
        password = input("Please enter password or press enter to go back: ")
        if password == "":
            self.userChoice()
        print("Please enter user role from the following roles: ",
              self.dfAccess["roles"].values)
        role = input()
        # print(role, "/n")
        # print(self.dfAccess["roles"])
        if role in self.dfAccess["roles"].values:
            while username in self.dfUser["username"].values:
                print("!!! user already exist !!!")
                username = input(
                    "Please enter new username or press enter to go back: ")
                if username == "":
                    self.userChoice()
            self.dfUser = self.dfUser.append(
                {"username": username, "password": password}, ignore_index=True)
            self.dfRoles = self.dfRoles.append(
                {"username": username, "roles": role}, ignore_index=True)
            print("Congrats!!! User has been added, Users are:")
            print(self.dfRoles)
            self.userChoice()
        else:
            print(
                "!!!You have selected invalid role, selecting default role as customer!!!")
            self.dfUser = self.dfUser.append(
                {"username": username, "password": password}, ignore_index=True)
            self.dfRoles = self.dfRoles.append(
                {"username": username, "roles": "customer"}, ignore_index=True)
            print("Congrats!!! User has been added new Users are: ", self.dfRoles)
            self.userChoice()

        pass

    def editRoles(self):
        print("Please enter username from the given list of username or press enter to continue: ",
              self.dfRoles["username"].values)
        username = input()
        if username in self.dfRoles["username"].values:
            print("Please enter user role from the following roles or press enter to continue: ",
                  self.dfAccess["roles"].values)
            role = input()
            if role in self.dfAccess["roles"].values:
                self.dfRoles.loc[(self.dfRoles["username"] ==
                                  username), "roles"] = role
                print("Congrats!!! User Role edited new User Roles are: ")
                print(self.dfRoles)
                self.userChoice()
            elif role == "":
                self.userChoice()
            else:
                print("You have entered incorrect user role")
                self.editRoles()
        elif username == "":
            self.userChoice()
        else:
            print("You have entered incorrect username")
            self.editRoles()


# rbac = User()
# rbac.userChoice()
