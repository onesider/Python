import docx
import re
from selenium import webdriver
from bs4 import BeautifulSoup
import pyscreenshot  # Pillow 패키지 설치해야함.
from urllib import parse
import time

# 이행진단결과를 담을 배열
# targe_list = []
web_target_list = []
mobile_target_list = []
etc_target_list = []
vul_list = []
pentest_target = ['웹(Web', '모바일(Mobile)']
vul_check_list = [
    ['버퍼 오버플로우', 'BO', 'X'],
    ['포맷스트링', 'FS', 'X'],
    ['LDAP 인젝션', 'LI', 'X'],
    ['운영체제 명령 실행', 'OC', 'X'],
    ['SQL 인젝션', 'SI', 'X'],
    ['SSI 인젝션', 'SS', 'X'],
    ['Xpath 인젝션', 'XI', 'X'],
    ['디렉터리 인덱싱', 'DI', 'O'],
    ['정보 누출', 'IL', 'O'],
    ['악성 콘텐츠', 'CS', 'X'],
    ['크로스사이트 스크립팅', 'XS', 'O'],
    ['약한 문자열 강도', 'BF', 'X'],
    ['불충분한 인증', 'IA', 'X'],
    ['취약한 패스워드 복구', 'PR', 'X'],
    ['크로스사이트 리퀘스트 변조(CSRF)', 'CF', 'X'],
    ['세션 예측', 'SE', 'X'],
    ['불충분한 인가', 'IN', 'X'],
    ['불충분한 세션 만료', 'SC', 'X'],
    ['세션 고정', 'SF', 'X'],
    ['자동화 공격', 'AU', 'X'],
    ['프로세스 검증 누락', 'PV', 'O'],
    ['파일 업로드', 'FU', 'X'],
    ['관리자 페이지 노출', 'AE', 'O'],
    ['경로 추적', 'PT', 'X'],
    ['위치 공개', 'PL', 'O'],
    ['데이터 평문 전송', 'SN', 'X'],
    ['쿠키변조', 'CC', 'O']
]

try:
    doc = docx.Document ('test3.docx')
except Exception as e:
    print("파일이 존재하지 않는듯? -> "+str(e))

# 테스트용 함수들..


def table_info(table_num, row_num):
    # 실구동때는 사용하지 않음 특정 테이블의 정보를 보고싶을때 사용하면 됨.
    # talbe_name = 테이블의 인덱스 / row_num 줄번호
    print("*" * 30)
    print('줄수 : ' + str(len(doc.tables[table_num].rows)))
    print('칸수 : ' + str(len(doc.tables[table_num].columns)))
    print("*" * 30)
    for num in range(len(doc.tables[table_num].row_cells(row_num))):
        print(doc.tables[table_num].row_cells(row_num)[num].text.replace('\n', ''))


def state_info():
    # 실구동때는 사용하지 않으나 대상별 정보를 출력하는 용도로 사용함.
    print ("웹 대상 갯수 : " + str(len(web_target_list)))
    print ("=" * 200)
    for i in range(len(web_target_list)):
        print(web_target_list[i][0], web_target_list[i][1])
        for ii in range(len(web_target_list[i])):
            if ii > 1:
                print(web_target_list[i][ii])
            else:
                pass
        print('='*200)
    print ("=" * 30)
    print ("모바일 대상 개수 : " + str(len(mobile_target_list)))
    print ("모바일 대상 리스트 : " + str(mobile_target_list))
    print ("=" * 30)
    print ("etc 대상 개수 : " + str(len(etc_target_list)))
    print ("etc 대상 리스트 : " + str(etc_target_list))
    print ("=" * 30)


def vul_table_search(doc, str1):
    # 실구동에 사용하지 않음. 테스트 용도로 만들어 둔듯함.
    # 삭제해도 될듯??
    vul_table_list = []
    for table in doc.tables:
        if str1 == table.row_cells(0)[0].text:
            vul_table_list.append(table)
        else:
            pass
    return vul_table_list


def str_search():
    # 표가 아닌 문자열을 검색할때 사용함. 혹시나 나중에 문자열 검색이 필요함 이함수를 응용해서 사용하면 될듯함.
    # 뎁스는 1, 2, 3, 4 , a2 순서로 나열됨. (이건 문서마다 다를수있음.)
    for i in range (len (doc.paragraphs)):
        if '1' == doc.paragraphs[i].style.style_id and '' != str (doc.paragraphs[i].text).replace ('\n', ''):
            if '상세 결과' == str (doc.paragraphs[i].text).replace ('\n', ''):
                print ('상세 결과 : ' + str (i))
            elif '대응방안' == str (doc.paragraphs[i].text).replace ('\n', ''):
                print ('대응방안 : ' + str (i))
        else:
            continue

    print ('*' * 40)
    for i in range (len (doc.paragraphs)):
        if (i > 210) and (i < 529):
            if '2' == doc.paragraphs[i].style.style_id and '' != str (doc.paragraphs[i].text).replace ('\n', ''):
                print (str (i) + ' : ' + str (doc.paragraphs[i].text).replace ('\n', ''))
            else:
                pass
        else:
            pass

    print ('*' * 40)
    for i in range (len (doc.paragraphs)):
        if (i > 211) and (i < 268):
            if '3' == doc.paragraphs[i].style.style_id and '' != str (doc.paragraphs[i].text).replace ('\n', ''):
                print (str (i) + ' : ' + str (doc.paragraphs[i].text).replace ('\n', ''))
            else:
                pass
        else:
            pass
    print ('*' * 40)
    for i in range (len (doc.paragraphs)):
        if (i > 212) and (i < 225):
            if '4' == doc.paragraphs[i].style.style_id and '' != str (doc.paragraphs[i].text).replace ('\n', ''):
                print (str (i) + ' : ' + str (doc.paragraphs[i].text).replace ('\n', ''))
            else:
                pass
        else:
            pass
    print ('*' * 40)
    for i in range (len (doc.paragraphs)):
        if (i > 212) and (i < 225):
            if 'a2' == doc.paragraphs[i].style.style_id and '' != str (doc.paragraphs[i].text).replace ('\n', ''):
                print (str (i) + ' : ' + str (doc.paragraphs[i].text).replace ('\n', ''))
            else:
                pass
        else:
            pass


# 여기까지 테스트 용함수!


def show_cookie():
    # 단순하게 걍 쿠키 보여주는 용도
    loop_count = 1
    print('쿠키 갯수는 ', len(driver.get_cookies()), '개 입니다.')  # 쿠키 갯수
    for cookie_index in driver.get_cookies():
        print(loop_count, ':', cookie_index.get('name'), '=', cookie_index.get('value'))
        loop_count = loop_count + 1


def screen_shot(param, num):
    # screenshot = pyscreenshot.grab(bbox=(18, 44, 1323, 800))
    # screenshot.show()
    # screenshot.save('/Users/onesider/Downloads/screenshot/screenshot_' + param + '['+str(num) +'].png')
    # 스크린샷 저장 위치를 지정해저야할듯 대상 폴더를 만들고 하위에 취약점 별 폴더를 생성해야할듯함.
    driver.get_screenshot_as_file ('/Users/onesider/Downloads/screenshot/screenshot_' + param + '['+str(num) +'].png')


def set_browser():
    # 진단용 브라우서 설정
    # screen_num = 0;
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-xss-auditor')
    driver = webdriver.Chrome('/Users/onesider/Downloads/01_Mac/chromedriver', chrome_options=options)
    driver.set_window_size(1300, 800)
    driver.implicitly_wait(3)
    return driver
    # driver.get('http://www.google.com')
    pass


def screen_shot(file_name, file_num):
    screenshot = pyscreenshot.grab(bbox=(18, 44, 1323, 800))
    # screenshot.show()
    screenshot.save('/Users/onesider/Downloads/screenshot/screenshot_' + file_name + '['+str(file_num) +'].png')


def table_search(doc, str1, str2, str3):
    for table in doc.tables:
        if (str1 == table.row_cells(0)[0].text) and (str2 == table.row_cells(0)[1].text) and (str3 == table.row_cells(0)[2].text):
            return table
        else:
            pass


def search_target():
    # 구분(웹/모바일) 대상(서비스명) URL 정보를 수집.
    # 대상표는 무조건 (구분, 대상, URL) 컬럼이 존재해야하고 딱 하나만 있어야함.
    # table_search 함수를 이용해서 가져옴.
    target_table = table_search(doc, '구분', '대상', 'URL')

    # 진단 대상 정보는 web_target_list // 모바일은 mobile_target_list // 기타는 etc_target_list
    for i in range(len(target_table.rows)):
        for ii in range(len(target_table.columns)):
            if '웹(Web)' == target_table.row_cells(i)[0].text:
                target_info = [target_table.row_cells(i)[1].text.replace('\n', ''), target_table.row_cells(i)[2].text.replace('\n', '')]
                web_target_list.append(target_info)
                break
            elif '모바일(Mobile)' == target_table.row_cells(i)[0].text:
                target_info = [target_table.row_cells(i)[1].text, target_table.row_cells(i)[2].text]
                mobile_target_list.append(target_info)
                break
            elif i != 0:
                target_info = [target_table.row_cells(i)[1].text, target_table.row_cells(i)[2].text]
                etc_target_list.append(target_info)
                break


def search_vul():
    # 취약점을 검색
    # table_search 함수를 이용해서 정보를 가져옴.
    # 발견된 취약점 정보를 가져옴. 대상별 발견된 취약점과 개수를 서치.

    vul_table = table_search(doc, '서비스', '발견된 취약점', '개수')
    # 모바일과 etc 리스트에 취약점을 추가하는 반복문은 따로 하나더 만들어야할듯..하나로 처리가 힘들듯..(펑션으로 만들던가.)
    # vul_info 는 [취약점 명, 갯수] 형태로 저장함.
    for i in range(len(web_target_list)):
        for ii in range(len(vul_table.rows)):
            if ii == 0:
                continue
            else:
                if str (web_target_list[i][0]) == vul_table.row_cells (ii)[0].text.replace ('\n', ''):
                    vul_info = [vul_table.row_cells (ii)[1].text.replace ('\n', '').replace(' ',''), int(vul_table.row_cells (ii)[2].text.replace ('건', ''))]
                    # print(vul_info)
                    if 1 <= web_target_list[i].count(vul_info):
                        pass
                    else:
                        # print(web_target_list[i].count(vul_info))
                        web_target_list[i].append(vul_info)


def get_vul():
    # 대상 + 취약점 별 갯수 + URL 정보들을 모두 취합..
    vul_search = []
    vul_table_list = vul_table_search(doc, '취약점 발생 위치')
    p = re.compile("http.*")
    num = 0
    vul_search_index = 0
    loop_count = 0

    for i in range(len(vul_table_list)):
        vuls = p.findall(vul_table_list[i].row_cells(1)[0].text)
        vul_search.append(vuls)

    # for i in vul_search:
    #     print(str(num) + ' : ' + str(i) + ' => ' + str(len(i)) + '건')
    #     num = num+1


    for targets in web_target_list:
        for target_vul in targets:
            if type(target_vul) is list:
                for target_vul_count in range(target_vul[1]):
                    if len(vul_search) < loop_count:
                        break
                    elif len(vul_search) > loop_count and len(vul_search[loop_count]) == target_vul[1]:
                        # print('target_vul = ' + str(target_vul))
                        # print('vul_search(취약점 url 리스트) = ' + str(len(vul_search[test])))
                        # print (target_vul)
                        # print('리스트(1) 개수 : '+str(len(vul_search[loop_count])))
                        for count in range(target_vul[1]):
                            # print(str(loop_count) + ' : ' + str(vul_search[loop_count][count]))
                            target_vul.append([vul_search[loop_count][0]])
                        # print(str(target_vul[1]))
                        # print(len(vul_search[test]))
                        if target_vul[1] >= len(vul_search[loop_count]):
                            loop_count = loop_count+1
                        elif target_vul[1] < len(vul_search[loop_count]):
                            loop_count = loop_count+len(vul_search[loop_count])
                        break
                    elif len(vul_search) > loop_count and len(vul_search[loop_count]) < target_vul[1]:
                        # print (target_vul)
                        # print('리스트(2) 개수 : '+str(len(vul_search[loop_count])))
                        for count in range(target_vul[1]):
                            if type(vul_search[loop_count]) is list :
                                for count in range(len(vul_search[loop_count])):
                                    # print(str(loop_count) + ' : ' + str(vul_search[loop_count][count]))
                                    if 1<= count:
                                        vul_url.extend([vul_search[loop_count][count]])
                                    else:
                                        vul_url = [vul_search[loop_count][count]]
                                        target_vul.append (vul_url)
                                    # print("aaa")
                                    # target_vul.append (vul_search[loop_count][0])
                            else:
                                # print(str(loop_count) + ' : ' + str(vul_search[loop_count]))
                                target_vul.append (vul_search[loop_count][0])

                            loop_count = loop_count+1
                        break

                    elif len(vul_search) > loop_count and len(vul_search[loop_count]) > target_vul[1]:
                        # print (target_vul)
                        # print('리스트(3) 개수 : '+str(len(vul_search[loop_count])))
                        # print(str(loop_count) + ' : ' + str(vul_search[loop_count]))
                        if type(vul_search[loop_count]) is list:
                            for count in range(len(vul_search[loop_count])):
                                # print(str(loop_count) + ' : ' + str(vul_search[loop_count][count]))
                                if 1 <= count:
                                    # print(vul_search[loop_count][count])
                                    vul_url.extend([vul_search[loop_count][count]])
                                    # target_vul.append(vul_url)
                                else:
                                    vul_url = [vul_search[loop_count][count]]
                                    target_vul.append(vul_url)
                        else:
                            print('헐? 손봐야할듯?')
                        loop_count = loop_count+1
                        break

                    else:
                        print('왜안되!!'+str(test))
                        break


def set_list(target_list):
    for target_index in target_list:
        if type(target_index) is list:
            for vul in vul_check_list:
                if vul[0].replace(' ', '') == target_index[0]:
                    if vul[1] == 'IL':
                        check_IL(target_index)
                    if vul[1] == 'XS':
                        check_XS(target_index)
                    # print(vul)
                    # print(target_index)


def check_IL(url_list):
    print("*"*200)
    for url in url_list:
        if type(url) is list:
            for url_index in range(len(url)):
                check_url = url[url_index].split()[0]
                print(check_url)
                # driver.get('http://gw.withsecurity.co.kr')
                # 스크린샷은 나중에...
                # driver.get(check_url)


def check_XS(url_list):
    # print("*"*200)
    loop_count = 0
    for url in url_list:
        if type(url) is list:
            for url_index in range(len(url)):
                check_url = url[url_index].split()[0]
                print(check_url)
                # print(loop_count)
                driver.get('http://gw.withsecurity.co.kr')
                screen_shot('XS',loop_count)
                time.sleep(2)
                loop_count = loop_count+1


search_target()
search_vul()
get_vul()
state_info()

# 메뉴에서 대상을 지정한다는 가정을깔고 도메인에 해당하는 리스트를 인자로 넘김
driver = set_browser()
set_list(web_target_list[0])


# set_vul()

