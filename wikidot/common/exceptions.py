# ---
# 基底クラス
# ---

class WikidotException(Exception):
    """独自例外の基底クラス"""

    def __init__(self, message):
        super().__init__(message)


# ---
# セッション関連
# ---

class SessionCreateException(WikidotException):
    """セッションの作成に失敗したときの例外"""

    def __init__(self, message):
        super().__init__(message)


class LoginRequiredException(WikidotException):
    """ログインが必要なメソッドをときの例外"""

    def __init__(self, message):
        super().__init__(message)


# ---
# AMC関連
# ---
class AjaxModuleConnectorException(WikidotException):
    """ajax-module-connector.phpへのリクエストに失敗したときの例外"""

    def __init__(self, message):
        super().__init__(message)


class AMCHttpStatusCodeException(AjaxModuleConnectorException):
    """AMCから返却されたHTTPステータスが200以外だったときの例外"""

    def __init__(self, message, status_code: int):
        super().__init__(message)
        self.status_code = status_code


class WikidotStatusCodeException(AjaxModuleConnectorException):
    """AMCから返却されたデータ内のステータスがokではなかったときの例外

    HTTPステータスが200以外の場合はAMCHttpStatusCodeExceptionを投げる
    """

    def __init__(self, message, status_code: str):
        super().__init__(message)
        self.status_code = status_code


class ResponseDataException(AjaxModuleConnectorException):
    """AMCから返却されたデータが不正だったときの例外"""

    def __init__(self, message):
        super().__init__(message)


# ---
# ターゲットエラー関連
# ---

class NotFoundException(WikidotException):
    """サイトやページ・ユーザが見つからなかったときの例外"""

    def __init__(self, message):
        super().__init__(message)


class ForbiddenException(WikidotException):
    """権限がないときの例外"""

    def __init__(self, message):
        super().__init__(message)
