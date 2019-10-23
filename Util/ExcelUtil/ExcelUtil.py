# -*- coding: utf-8 -*-
"""
author:
本代码主要封装了几个操作Excel数据的方法
"""
import xlrd

def getAllRowsBySheetIndex(sheetIndex, xlsFilePath):
    """
    获取行视图
    根据Sheet序号获取该Sheet包含的所有行，返回值类似[ ['a', 'b', 'c'], ['1', '2', '3'] ]
    sheetIndex指示sheet的索引，0表示第一个sheet，依次类推
    xlsFilePath是Excel文件的相对或者绝对路径
    """
    workBook = xlrd.open_workbook(xlsFilePath)
    table = workBook.sheets()[sheetIndex]

    rows = []
    rowNum = table.nrows # 总共行数
    rowList = table.row_values
    for i in range(rowNum):
        rows.append(rowList(i)) # 等价于rows.append(i, rowLists(i))

    return rows


def getRow(sheetIndex, rowIndex, xlsFilePath):
    """
    获取某个Sheet的指定序号的行
    sheetIndex从0开始
    rowIndex从0开始
    """
    rows = getAllRowsBySheetIndex(sheetIndex, xlsFilePath)
    return rows[rowIndex]


def getAllColsBySheetIndex(sheetIndex, xlsFilePath):
    """
    获取列视图
    根据Sheet序号获取该Sheet包含的所有列，返回值类似[ ['a', 'b', 'c'], ['1', '2', '3'] ]
    sheetIndex指示sheet的索引，0表示第一个sheet，依次类推
    xlsFilePath是Excel文件的相对或者绝对路径
    """
    workBook = xlrd.open_workbook(xlsFilePath)
    table = workBook.sheets()[sheetIndex]

    cols = []
    colNum = table.ncols # 总共列数
    colList = table.col_values
    for i in range(colNum):
        cols.append(colList(i))

    return cols


def getCol(sheetIndex, colIndex, xlsFilePath):
    '''
    获取某个Sheet的指定序号的列
    sheetIndex从0开始
    colIndex从0开始
    '''
    cols = getAllColsBySheetIndex(sheetIndex, xlsFilePath)

    return cols[colIndex]


def getCellValue(sheetIndex, rowIndex, colIndex, xlsFilePath):
    """
    获取指定sheet的指定行列的单元格中的值
    使用方法：getCellValue(0,1,1,xlsFilePath) # 获取第一个sheet第一行第一列的单元格的值.PS:根据需要对输入进行转码。
              如果在使用中，对应的字段需要输入整数，则需要进行转码，如int(getCellValue(0,1,1,xlsFilePath)
    """
    workBook = xlrd.open_workbook(xlsFilePath)
    table = workBook.sheets()[sheetIndex]

    return table.cell(rowIndex, colIndex).value # 或者table.row(0)[0].value或者table.col(0)[0].value

