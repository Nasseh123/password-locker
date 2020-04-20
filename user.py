class user:
    """
    Class for holding the login and password credentials of a certain user.
    also Its required to enable validations of getting the right users
    """
    def __init__(self,username,password):
        self.username=username
        self.password=password
 
    user_list=[]