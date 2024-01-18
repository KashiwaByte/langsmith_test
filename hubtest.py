from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# 默认情况下，load_dotenv() 不会覆盖已经在环境中的变量。
# 如果你需要覆盖，可以传递 override=True 参数。
load_dotenv()

# 现在你可以像访问任何其他环境变量一样访问这些变量
import os

tracing_v2 = os.getenv('LANGCHAIN_TRACING_V2')
endpoint = os.getenv('LANGCHAIN_ENDPOINT')
api_key = os.getenv('LANGCHAIN_API_KEY')
project = os.getenv('LANGCHAIN_PROJECT')

from langchain import hub
obj = hub.pull("pptt1212/comparison-aspect")
print(obj)
template=obj.template
print(template)