import hmac

# HMAC_KEY为生成消息摘要的密钥
HMAC_KEY = b'&^DRE45!@lpDF!25Tm2='

message = "春天，你好".encode("utf-8")
# 对message按SHA256算法生成摘要
sign = hmac.new(HMAC_KEY, message, "SHA256").hexdigest()
print(sign)