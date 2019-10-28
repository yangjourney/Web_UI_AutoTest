#encoding=utf-8

from Util.KeyWordDriven.KeyWordExcelTool.Excel import *
from Util.KeyWordDriven.KeyWordModule import Action
from Util.KeyWordDriven.KeyWordExcelTool.CaseInfo import *
from Util.KeyWordDriven.KeyWordExcelTool.CaseStepInfo import *
from Util.KeyWordDriven.KeyWordDic.Keyword import *
from Util.KeyWordDriven.KeyWorldTool.LogUtility import *
from Util.KeyWordDriven.KeyWorldTool.EmailUtils import *
import shutil

class RunTests(object):
    """description of class"""
    def __init__(self):
        CreateRunFolder()

    def setUpKeyword(self):
        CreateLoggerFile('log')
        logging.info('******************************************************************')
        logging.info('******************************关键字驱动的log**********************')
        logging.info('******************************************************************')
        # 将测试的excel复制到testresult里面，然后在这里加上测试的结果
        oldname = keyword_excel_path
        newname = os.path.join(ResultFolder.GetRunDirectory(), u"关键字驱动测试用例.xlsx")
        shutil.copyfile(oldname, newname)
        case_file = ParseExcel(newname)
        self.case_file = case_file

    def LoadAndRunTestCases_Keyword(self,type):
        try:
            caseList = self.getAllTestCase_keyword()
            for case in caseList:
                caseStepInfoList = self.getCaseStep(case.sheetName)
                self.log_info('>>>>>>>>>>>>>>>用例(关键字驱动)：'+case.caseName+'('+ case.caseDescribe+')开始执行>>>>>>>>>>>>>>>')
                start = time.time()
                result = self.executeCase(caseStepInfoList)
                end = time.time()
                self.log_info('<<<<<<<<<<<<<<<用例(关键字驱动)：'+case.caseName+'('+ case.caseDescribe+')执行完成<<<<<<<<<<<<<<<')

                #在测试case  sheet页，填写每个case的时间和结果
                self.case_file.get_sheet_by_name('测试用例')
                execute_time = "%.2fs" % (end - start)
                self.case_file.write_cell_content(case.rownum+1,case_usetime+1,execute_time)
                self.case_file.write_cell_content(case.rownum+1,case_result+1, result)

        except Exception as err:
            self.log_info("测试用例运行失败, 以下是错误信息: {}".format(str(err)))
        finally:
            # 发邮件提醒（1 发送，0 不发送）
            if type == 1:
                SendMail_SMTP()
            else:
                pass

    #把None转换成空字符
    def getString(self,str1):
        if str1 is None:
            return ''
        else:
            return str(str1)

    # 遍历"测试用例"这个sheet
    def getAllTestCase_keyword(self):
        self.log_info('getAllTestCase')
        caseList = []

        self.case_file.get_sheet_by_name('测试用例')
        all_rows_list = list(self.case_file.get_all_rows())
        for row in all_rows_list[1:]:

            # 获取动作、定位方式、定位表达式、操作值
            caseNum = self.getString(row[case_no].value)  # 测试case的序号（不重要）
            caseName = self.getString(row[case_name].value)  # 用例名称
            caseDescribe = self.getString(row[case_describe].value)  # 用例描述
            caseDetailSheetSame = self.getString(row[case_detail].value)  # 步骤sheet名
            caseIsNeedDo = self.getString(row[case_NeedToDo].value)  # 用例是否需要执行
            # caseEndTime = self.getString(row[case_usetime].value)  # 执行结束时间
            # caseResult = self.getString(row[case_result].value)  # 结果

            if caseName == '' or caseDescribe == '' or caseDetailSheetSame == '':
                break
            if caseIsNeedDo == 'y' or caseIsNeedDo=='Y':
                rownum = all_rows_list.index(row)
                case = CaseInfo(caseNum,caseName,caseDescribe,caseDetailSheetSame,rownum)
                caseList.append(case)
        return caseList

    def getCaseStep(self,sheetName):
        self.log_info('getCaseStep')
        caseStepList = []

        self.case_file.get_sheet_by_name(sheetName)
        all_rows_list = list(self.case_file.get_all_rows())
        for row in all_rows_list[1:]:
            # 获取动作、定位方式、定位表达式、操作值
            stepNum = self.getString(row[step_no].value)
            stepDescribe = self.getString(row[step_describe].value)
            stepKeyword = self.getString(row[step_keyword].value)
            stepMethod = self.getString(row[step_method].value)
            stepExpression = self.getString(row[step_expression].value)
            stepValue = self.getString(row[step_value].value)
            if stepDescribe == '' or stepKeyword == '':
                break
            rownum = all_rows_list.index(row)
            stepInfo = CaseStepInfo(stepNum,stepDescribe,stepKeyword,stepMethod,stepExpression,stepValue,rownum)
            caseStepList.append(stepInfo)
        return caseStepList

    def executeCase(self,caseStepList):
        # self.log_info('executeCaseStep')
        for step in caseStepList:
            # num 操作步骤序号
            # describe 操作步骤描述
            # keyword 操作步骤的关键词
            # method 定位方式
            # expression 定位表达式
            # value 操作值
            # self.log_info('step.keyword='+step.keyword+',method='+step.method+',expression='+step.expression+',value=' + step.value)
            start = time.time()
            try:
                self.matchKeyword(step)
                # 在case的步骤页面填写每个步骤的时间和结果
                execute_time = "%.2fs" % (time.time() - start)

                self.case_file.write_cell_content(step.rownum + 1, step_time + 1, execute_time)
                self.case_file.write_cell_content(step.rownum + 1, step_result + 1, 'success')

            except Exception as err:
                execute_time = "%.2fs" % (time.time() - start)
                self.case_file.write_cell_content(step.rownum + 1, step_time + 1, execute_time)
                self.case_file.write_cell_content(step.rownum + 1, step_result + 1, 'fail')
                self.case_file.write_cell_content(step.rownum + 1, step_err + 1, str(err))
                self.log_error("执行测试步骤:" + step.describe + "  error: " + str(err))
                Action.close_browser()
                return 'fail'
        return 'success'

    def matchKeyword(self,step):
        self.log_info("-->" + step.describe)
        if step.keyword == open_browser:
            Action.open_browser(step.value)
        elif step.keyword == visit_url:
            Action.visit_url(step.value)
        elif step.keyword == pause:
            Action.pause(step.value)
        elif step.keyword == enter_frame:
            Action.enter_frame(step.method, step.expression)
        elif step.keyword == input_string:
            Action.input_string(step.method, step.expression, step.value)
        elif step.keyword == click:
            Action.click(step.method, step.expression)
        elif step.keyword == close_browser:
            Action.close_browser()
        elif step.keyword == get_screen_shot:
            Action.get_screen_shot(times())
        elif step.keyword == assert_word:
            Action.assert_word(step.value)
        elif step.keyword == assert_wholeurl:
            Action.assert_wholeurl(step.value)
        elif step.keyword == assert_parturl:
            Action.assert_parturl(step.value)
        elif step.keyword == input_select_click:
            Action.input_select_click(step.method, step.expression, step.value)
        elif step.keyword == out_frame:
            Action.out_frame()
        elif step.keyword == ctrl_v:
            Action.ctrl_v(step.value)
        elif step.keyword == tab_key:
            Action.tab_key()
        elif step.keyword == enter_key:
            Action.enter_key()
        else:
            self.log_info("非法关键字：" + step.keyword)

    def log_info(self,info):
        logging.info(str(info))
        print(str(info))

    def log_error(self,info):
        logging.error(str(info))
        print(str(info))

