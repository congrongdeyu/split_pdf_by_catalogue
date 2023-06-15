import glob  # 导入 glob 库，用于查找 pdf 文件
from collections import OrderedDict  # 导入有序字典
import os
import shutil
import fitz  # 导入 PyMuPDF 库


def split_pdf_by_toc(input_file):
    doc = fitz.open(input_file)  # 打开输入文件
    toc = doc.get_toc()  # 获取目录

    # 获取最大层级的目录
    level_list = []
    for level, title, page in toc:
        level_list.append(level)
    max_level = max(level_list)
    min_level = min(level_list)

    catalogue_list = []
    for index, (level, title, page) in enumerate(toc):  # 遍历目录
        catalogue_list.append([index, level, title, page])
    catalogue_list_len = len(catalogue_list)
    # print(catalogue_list)

    title_dict = OrderedDict()
    for index, level, title, page in catalogue_list:  # 遍历目录
        # print(index, level, title, page)
        if level == min_level:
            title_dict[level] = title  # 把目录层级和目录按照顺序存到有序字典中
        elif index == catalogue_list_len - 1:
            title_dict[level] = title

            # 输出 pdf 文件
            filename = "_".join(title_dict.values())  # 按照目录层级把目录合并成文件名
            output_doc = fitz.open()  # 创建一个新的空白文档
            start_page = page - 1  # 计算开始页面
            if index + 1 < len(toc):  # 如果不是最后一个标题
                end_page = toc[index + 1][2] - 1  # 计算结束页面
            else:  # 如果是最后一个标题
                end_page = doc.page_count - 1  # 结束页面为文档的最后一页
            output_doc.insert_pdf(doc, from_page=start_page, to_page=end_page)  # 插入页面到新文档中
            output_doc.save(f"{filename}.pdf")  # 保存新文档，以标题命名
            output_doc.close()  # 关闭新文档
        elif level == max_level:
            title_dict[level] = title

            # 输出 pdf 文件
            filename = "_".join(title_dict.values())  # 按照目录层级把目录合并成文件名
            output_doc = fitz.open()  # 创建一个新的空白文档
            start_page = page - 1  # 计算开始页面
            if index + 1 < len(toc):  # 如果不是最后一个标题
                end_page = toc[index + 1][2] - 1  # 计算结束页面
            else:  # 如果是最后一个标题
                end_page = doc.page_count - 1  # 结束页面为文档的最后一页
            output_doc.insert_pdf(doc, from_page=start_page, to_page=end_page)  # 插入页面到新文档中
            output_doc.save(f"{filename}.pdf")  # 保存新文档，以标题命名
            output_doc.close()  # 关闭新文档
        elif level == catalogue_list[index + 1][1]:
            title_dict[level] = title

            # 输出 pdf 文件
            filename = "_".join(list(title_dict.values())[:level])  # 按照目录层级把目录合并成文件名
            output_doc = fitz.open()  # 创建一个新的空白文档
            start_page = page - 1  # 计算开始页面
            if index + 1 < len(toc):  # 如果不是最后一个标题
                end_page = toc[index + 1][2] - 1  # 计算结束页面
            else:  # 如果是最后一个标题
                end_page = doc.page_count - 1  # 结束页面为文档的最后一页
            output_doc.insert_pdf(doc, from_page=start_page, to_page=end_page)  # 插入页面到新文档中
            output_doc.save(f"{filename}.pdf")  # 保存新文档，以标题命名
            output_doc.close()  # 关闭新文档
        else:
            title_dict[level] = title
    doc.close()  # 关闭输入文件


pdf_files = glob.glob("*.pdf")  # 获取所有 pdf 文件

python_path = os.getcwd()
# 分割所有找到的 pdf 文件
for pdf_file in pdf_files:
    dir_name = pdf_file.split(".")[0]
    os.makedirs(dir_name)
    shutil.move(pdf_file, dir_name)
    path = os.path.join(os.getcwd(), dir_name)
    os.chdir(path)
    split_pdf_by_toc(pdf_file)  # 调用函数，传入输入文件名
    os.chdir(python_path)
