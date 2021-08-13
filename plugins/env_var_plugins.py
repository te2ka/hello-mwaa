from airflow.plugins_manager import AirflowPlugin
import os

dirname = os.path.dirname(__file__)
os.environ['PATH'] = os.getenv('PATH') + f':{ dirname }/bin/'

class EnvVarPlugin(AirflowPlugin):
     name = 'env_var_plugin'
