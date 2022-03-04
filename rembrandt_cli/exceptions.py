class Error(Exception):
    """Base class for other exceptions"""
    pass


class BasicError(Error):
    pass


class NotLoggedInError(Error):
    '''Raised when action requires logged In User and User is not logged in'''
    pass


class PasswordRequirementsError(Error):
    pass


class MissingParametersError(Error):
    pass


class UsernameAlreadyExistsError(Error):
    pass
