import logging

# 기본적으로 std out 에 보내는 로그 ..... 
# logging.basicConfig(level=logging.DEBUG, format="%(asctime)s [%(levelname)s] %(message)s")

# logging.debug("debug 레벨.... 개발자만 보는 거")
# logging.info('info 레벨.... 사용자에게 알려는 줌')
# logging.warning('warning 레벨....  ')
# logging.error('error 레벨....  ')
# logging.critical('critical 레벨....  ')

################################
# 터미널과 파일에 모두 남기기
# 로거 객체를 만들고 로거에 핸들러를 add하면, 로거 객체에 쓰는 메시지가 핸들러로 간다.... 
logFormatter =  logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 스트림 -> std out 
streamHandler = logging.StreamHandler()
streamHandler.setFormatter(logFormatter)
logger.addHandler(streamHandler)

# 파일
from datetime import datetime

filename = datetime.now().strftime("mylog_%Y%m%d_%H%M%S.log")
fileHandler = logging.FileHandler(filename,encoding='utf-8')
fileHandler.setFormatter(logFormatter)
logger.addHandler(fileHandler)

logger.info("인포 레벨의 로그 메시지를 씁니다.")