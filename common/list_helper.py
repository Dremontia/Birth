class ListHelper:
    """
    列表助手
    """

    @staticmethod
    def skill_info(list_skill, fnuc):
        """
        根据要求在列表中查询符合条件的数据并且依次返回
        :param list_skill: 要查询的列表
        :param fnuc: 查询条件
        :return:生成器对象
        """
        for item in list_skill:
            if fnuc(item):
                yield item

    @staticmethod
    def first_true(list_mom, fnuc):
        """
        根据要求在列表中查询符合条件的数据，并且返回第一个符合条件的数据。
        :param list_mom: 查询目标列表
        :param fnuc: 查询条件
        :return: 单一元素
        """
        for item in list_mom:
            if fnuc(item):
                # yield item
                # break  可以用for阅读
                return item

    @staticmethod
    def count_true(list_mom, fnuc):
        """
        根据要求在列表中查询符合条件的数据，并计算符合条件的数据数量。
        :param list_mom: 查询目标列表
        :param fnuc: 查询条件
        :return: 符合条件的数据数量
        """
        count = 0
        for item in list_mom:
            if fnuc(item):
                count += 1
        return count

    @staticmethod
    def value_sum(list_mom, fnuc):
        """
        自定义类的列表求和
        :param list_mom: 目标列表
        :param fnuc: 自定义对象
        :return: 和
        """
        sum = 0
        for item in list_mom:
            sum += fnuc(item)
        return sum

    @staticmethod
    def max_value(list_mom, fnuc):
        max_value = list_mom[0]
        for item in range(1, len(list_mom)):
            if fnuc(max_value) < fnuc(list_mom[item]):
                max_value = list_mom[item]
        return max_value

    # max_value = 0
    # for item in range(len(list_mom)-1):
    #     if fnuc(item) < fnuc(item+1):
    #         max_value = fnuc(item+1)
    # return max_value

    @staticmethod
    def get_values_list(list_mom, fnuc):
        """
        将想要的列表中数据添加到新的列表中并输出
        :param list_mom: 目标列表
        :param fnuc: 想要获取的数据
        :return: 获取数据列表
        """
        list = []
        for item in list_mom:
            list.append(fnuc(item))
        return list

    @staticmethod
    def get_values_up(list_mom, fnuc):
        """
        按照需求数据将其升序排列
        :param list_mom: 目标列表
        :param fnuc: 所需数据类型
        :return: 返回所需数据升序列表
        """
        for i in list_mom:
            for j in range(len(list_mom)-1):
                if fnuc(list_mom[j]) > fnuc(list_mom[j+1]):
                    list_mom[j],list_mom[j+1]=list_mom[j+1],list_mom[j]
        return list_mom