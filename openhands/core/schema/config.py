from enum import Enum


class ConfigType(str, Enum):
    # For frontend
    AGENT = 'AGENT'
    AGENT_MEMORY_ENABLED = 'AGENT_MEMORY_ENABLED'
    AGENT_MEMORY_MAX_THREADS = 'AGENT_MEMORY_MAX_THREADS'
    AWS_ACCESS_KEY_ID = 'AWS_ACCESS_KEY_ID'
    AWS_REGION_NAME = 'AWS_REGION_NAME'
    AWS_SECRET_ACCESS_KEY = 'AWS_SECRET_ACCESS_KEY'
    BASE_CONTAINER_IMAGE = 'BASE_CONTAINER_IMAGE'
    CACHE_DIR = 'CACHE_DIR'
    CONFIRMATION_MODE = 'CONFIRMATION_MODE'
    DEBUG = 'DEBUG'
    DISABLE_COLOR = 'DISABLE_COLOR'
    E2B_API_KEY = 'E2B_API_KEY'
    FILE_UPLOADS_ALLOWED_EXTENSIONS = 'FILE_UPLOADS_ALLOWED_EXTENSIONS'
    FILE_UPLOADS_MAX_FILE_SIZE_MB = 'FILE_UPLOADS_MAX_FILE_SIZE_MB'
    FILE_UPLOADS_RESTRICT_FILE_TYPES = 'FILE_UPLOADS_RESTRICT_FILE_TYPES'
    LLM_API_KEY = 'LLM_API_KEY'
    LLM_API_VERSION = 'LLM_API_VERSION'
    LLM_BASE_URL = 'LLM_BASE_URL'
    LLM_CACHING_PROMPT = 'LLM_CACHING_PROMPT'
    LLM_CUSTOM_LLM_PROVIDER = 'LLM_CUSTOM_LLM_PROVIDER'
    LLM_DROP_PARAMS = 'LLM_DROP_PARAMS'
    LLM_EMBEDDING_BASE_URL = 'LLM_EMBEDDING_BASE_URL'
    LLM_EMBEDDING_DEPLOYMENT_NAME = 'LLM_EMBEDDING_DEPLOYMENT_NAME'
    LLM_EMBEDDING_MODEL = 'LLM_EMBEDDING_MODEL'
    LLM_MAX_INPUT_TOKENS = 'LLM_MAX_INPUT_TOKENS'
    LLM_MAX_OUTPUT_TOKENS = 'LLM_MAX_OUTPUT_TOKENS'
    LLM_MODEL = 'LLM_MODEL'
    LLM_NUM_RETRIES = 'LLM_NUM_RETRIES'
    LLM_RETRY_MAX_WAIT = 'LLM_RETRY_MAX_WAIT'
    LLM_RETRY_MIN_WAIT = 'LLM_RETRY_MIN_WAIT'
    LLM_TEMPERATURE = 'LLM_TEMPERATURE'
    LLM_TIMEOUT = 'LLM_TIMEOUT'
    LLM_TOP_P = 'LLM_TOP_P'
    LLM_DISABLE_VISION = 'LLM_DISABLE_VISION'
    MAX_ITERATIONS = 'MAX_ITERATIONS'
    RUN_AS_OPENHANDS = 'RUN_AS_OPENHANDS'
    SANDBOX_TIMEOUT = 'SANDBOX_TIMEOUT'
    SANDBOX_USER_ID = 'SANDBOX_USER_ID'
    SECURITY_ANALYZER = 'SECURITY_ANALYZER'
    USE_HOST_NETWORK = 'USE_HOST_NETWORK'
    WORKSPACE_BASE = 'WORKSPACE_BASE'
    WORKSPACE_MOUNT_PATH = 'WORKSPACE_MOUNT_PATH'
    WORKSPACE_MOUNT_PATH_IN_SANDBOX = 'WORKSPACE_MOUNT_PATH_IN_SANDBOX'
    WORKSPACE_MOUNT_REWRITE = 'WORKSPACE_MOUNT_REWRITE'
