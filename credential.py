class Credential:
    """
    class that generates new instances of user credentials
    """

    def __init__(self,app_name,app_username,app_email,app_password):
        self.app_name=app_name
        self.app_username=app_username
        self.app_email=app_email
        self.app_password=app_password
    
    app_list=[]
    
    def savecredentials(self):
        """
        save_user method for saving a user by appending it to the user_list
        """
        Credential.app_list.append(self)

    def delete_credential(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Credential.app_list.remove(self)

    @classmethod
    def find_by_appname(cls,app_name):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for Credential in cls.app_list:
            if Credential.app_name== app_name:
                return Credential
    
    @classmethod
    def display_all_apps(cls):
        """
        method for returing all apps _credential 
        """
        return cls.app_list

    # booleanchecking if userexists
    @classmethod
    def search_app_credentials(cls, app_Name):
        """
        confirm_user method that checks if a password matches a username
        """
        for Credential in cls.app_list:
            if Credential.app_name == True:
                return True
            else:
                return False
        else:
            return False
    