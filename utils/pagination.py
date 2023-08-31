"""

自定义的分页组件，以后如果想要使用这个分页组件，你需要做以下几件事：



在视图函数中：

    def pretty_list(request):

        # 1.检索符合条件的数据

        queryset = models.PrettyNum.objects.all()

        # 2.实例化分页对象

        page_obj = Pagination(request, queryset)

        # 3.传递到前端页面的参数

        context = {

            'queryset': page_obj.page_queryset,  # 分完页的数据

            'page_string': page_obj.html()       # 生成的页码

        }

        return render(request, 'pretty_list.html', context)



在HTML页面中：



        {% for obj in queryset %}

            {{obj.xxx}}

        {% endfor %}



        <ul class="pagination">

            {{ page_string }}

        </ul>

"""

from django.utils.safestring import mark_safe





class pagination(object):

    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):

        '''



        :param request: 请求的对象

        :param queryset: 符合查询条件的分页数据

        :param page_size:每页显示多少条数据

        :param page_param:在url中传递的获取分页的参数，例如：/pretty/list/?page=2

        :param plus:显示当前页的前或后几页(页码)

        '''



        import copy

        query_dict = copy.deepcopy(request.GET)

        query_dict._mutable = True



        # 封装query_dict

        self.query_dict = query_dict

        # 封装page_param

        self.page_param = page_param

        # 接收传入的当前页码

        page = request.GET.get(page_param, "1")

        # 确保page为数字

        if page.isdecimal():

            page = int(page)

        else:

            page = 1

        # 封装page

        self.page = page

        # 封装每页数据条数page_size

        self.page_size = page_size

        # 封装计算生成的起止页码

        self.start = (page - 1) * page_size  # 起始值

        self.end = page * page_size  # 结束值

        # 封装queryset

        self.page_queryset = queryset[self.start:self.end]



        # 计算数据表符合筛选条件的总数据条数

        total_count = queryset.count()

        # 设总页码total_page_count，余数div，计算总页码数

        total_page_count, div = divmod(total_count, page_size)

        # 若有余数，则总页码数+1

        if div:

            total_page_count += 1

        # 封装总数据条数total_page_count

        self.total_page_count = total_page_count

        # 封装plus

        self.plus = plus



    def html(self):

        # 计算：当前页码及其前后5页的页码

        if self.total_page_count <= 2 * self.plus + 1:

            # 数据表中的数据比较少（不足11个页码）

            start_page = 1

            end_page = self.total_page_count

        else:

            # 数据表中的数据比较少（超过11个页码）

            # 当前页小于5

            if self.page <= self.plus:

                start_page = 1

                end_page = 2 * self.plus + 1

            else:

                # 当前页大于5

                # 若当前页+plus > 总页码

                if (self.page + self.plus) > self.total_page_count:

                    start_page = self.total_page_count - 2 * self.plus

                    end_page = self.total_page_count

                else:

                    start_page = self.page - self.plus

                    end_page = self.page + self.plus

        # 后端生成分页字符串

        # 定义列表，存放生成的分页项li元素字符串

        page_str_list = []

        # 上一页

        if self.page > 1:

            self.query_dict.setlist(self.page_param, [self.page - 1])

            # 生成上一页li字符串

            prev = '<li><a href="?{}"><span aria-hidden="true">《</span></a></li>'.format(self.query_dict.urlencode())

            # 添加到列表中

            page_str_list.append(prev)

        # 页码

        for i in range(start_page, end_page + 1):

            # 将li字符串格式化，赋值给ele

            if i == self.page:

                self.query_dict.setlist(self.page_param, [i])

                ele = '<li class="active"><a href="?{0}">{1}</a></li>'.format(self.query_dict.urlencode(), i)

            else:

                self.query_dict.setlist(self.page_param, [i])

                ele = '<li><a href="?{0}">{1}</a></li>'.format(self.query_dict.urlencode(), i)

            # 添加到列表中

            page_str_list.append(ele)

        # 下一页

        if self.page < self.total_page_count:

            self.query_dict.setlist(self.page_param, [self.page + 1])

            # 生成上一页li字符串

            prev = '<li><a href="?{}"><span aria-hidden="true">》</span></a></li>'.format(self.query_dict.urlencode())

            # 添加到列表中

            page_str_list.append(prev)

        # 完成列表元素的拼接，赋值给page_string

        page_string = mark_safe(''.join(page_str_list))  # 将分页字符串使用mark_safe()包裹一下

        return page_string