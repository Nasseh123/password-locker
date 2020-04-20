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
