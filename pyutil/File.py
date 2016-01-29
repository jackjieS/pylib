import os.path

__author__ = 'xianyu'


class File:
    @staticmethod
    def read(path, encoding="utf_8"):
        try:
            fo = open(path, "r", encoding=encoding)
            content = fo.read()
            fo.close()
            return content
        except IOError as err:
            print(path, err)

    @staticmethod
    def readline(path, encoding="utf_8"):
        try:
            fo = open(path, "r", encoding=encoding)
            for eachline in fo:
                # 去掉行尾结束符
                yield eachline.rstrip()
            fo.close()
        except IOError as err:
            print(path, err)

    @staticmethod
    def write(path, content, encoding="utf_8"):
        try:
            fo = open(path, "w", encoding=encoding)
            fo.write(content)
            fo.close()
        except IOError as err:
            print(path, err)

    @staticmethod
    def writelines(path, lines, encoding="utf_8"):
        try:
            fo = open(path, "w", encoding=encoding)
            for line in lines:
                fo.write(line + os.linesep)
            fo.close()
        except IOError as err:
            print(path, err)


def main():
    path = r"E:\dxzh\Ctrip.AM.Material\Ctrip.AM.JobCommon\TemplateEnum.cs"
    for eachline in File.readline(path):
        print(eachline)
    # File.read()


if __name__ == '__main__':
    main()
