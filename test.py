import fitz # 导入 PyMuPDF 库
import glob
from collections import OrderedDict

pdf_files = glob.glob("*.pdf")  # 获取所有 pdf 文件

# 分割所有找到的 pdf 文件
for pdf_file in pdf_files:
    doc = fitz.open(pdf_file)  # 打开输入文件

    toc = doc.get_toc()  # 获取目录
    print(toc)

    # 获取最大层级的目录
    level_list = []
    for level, title, page in toc:
        level_list.append(level)
    max_level = max(level_list)
    min_level = min(level_list)
    # print(max_level)

    title_dict = OrderedDict()
    for index, (level, title, page) in enumerate(toc):  # 遍历目录
        # print(index, level, title, page)
        if level != max_level:
            title_dict[level] = title
            # print(title_dict)
        else:
            title_dict[level] = title
            print(title_dict)
            # print(title_dict)
            # filename = "_".join(title_dict.values())
            # # print(filename)
            # output_doc = fitz.open()  # 创建一个新的空白文档
            # start_page = page - 1  # 计算开始页面
            # if index + 1 < len(toc):  # 如果不是最后一个标题
            #     end_page = toc[index + 1][2] - 1 # 计算结束页面
            # else:  # 如果是最后一个标题
            #     end_page = doc.page_count - 1  # 结束页面为文档的最后一页
            # output_doc.insert_pdf(doc, from_page=start_page, to_page=end_page)  # 插入页面到新文档中
            # output_doc.save(f"{filename}.pdf")  # 保存新文档，以标题命名
            # output_doc.close()  # 关闭新文档

    doc.close()  # 关闭输入文件