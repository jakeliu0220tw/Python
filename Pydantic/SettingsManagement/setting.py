from pydantic import BaseSettings

class Setting(BaseSettings):
    API_BASE: str = 'https://baseapi.ithome.tw'
    DB_HOST: str = 'localhost'
    DB_PORT: int = 5566
    DB_NAME: str = 'unknown'
    TESTING: bool = False
    class Config:
        case_sensitive = True
        env_file = '.env'

class ProdSetting(Setting):
    class Config:
        env_file = 'prod.env'

class TestSetting(Setting):
    class Config:
        env_file = 'test.env'