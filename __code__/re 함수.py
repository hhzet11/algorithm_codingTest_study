import re

# 원하는 특정 문자 제거
# a-z, 0-9, \특수문자 : -, _, . 포함함을 의미
new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
# 원하는 특정 문자 외의 나머지 제거
new_id = re.sub('[^a-z0-9\-_.]', '', new_id)
# '.'이 중복될 때 한번만 작성
new_id = re.sub('\.+', '.', new_id)
# '.'가 맨앞뒤에 나올시 제거
new_id = new_id.strip(".")

