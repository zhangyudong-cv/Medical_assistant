# LLM API 配置 (兼容 OpenAI 的接口)
LLM_CONFIG = {
    "api_key": "sk-9726d3bd14e94d5398c1677e00625ae6",
    "model_name": "qwen-plus",  # 阿里云百炼推荐模型：qwen-plus 或 qwen-max
    "base_url": "https://dashscope.aliyuncs.com/compatible-mode/v1",
    "temperature": 0.7,
    "max_tokens": 8192,
}

# Mem0 API 配置 (长期记忆服务)
MEM0_CONFIG = {
    "api_key": "m0-cJUJqcVNfwNipd0PqxFIaoMj9epaj6SRSY9dK69A",
}

# Milvus 数据库配置 (远程服务器)
MILVUS_CONFIG = {
    "uri": "http://192.168.100.128:19530",
    "collection_name": "medical_knowledge",
}
