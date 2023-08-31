from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render,redirect


class AuthMiddleware(MiddlewareMixin):
    """中间件1"""
    def process_request(self, request):
        # 获取用户登录的url request.path_info
        # 当用户访问登录url时，返回None
        if request.path_info in ['/login/','/img/code/']:
            return
        # 用户是否登录的判断
        #读取当前访问的用户session信息，赋值给info
        info_dict = request.session.get('info')
        if info_dict:
            return
        return redirect('/login/')

        # print('M1.进来了')
        #return HttpResponse('无权访问')

    # def process_response(self, request, response):
    #     print('M1.走了')
    #     return response

# class M2(MiddlewareMixin):
#     """中间件2"""
#     def process_request(self, request):
#         print('M2.进来了')
#
#     def process_response(self, request, response):
#         print('M2.走了')
#         return response
