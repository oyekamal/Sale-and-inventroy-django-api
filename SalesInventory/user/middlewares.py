
from user_log.models import Log
import json
def my_middleware(get_response):
    print("in middleware is will run only one time")

    def my_function(request):
        print("Middleware run before views")
        print(get_response)
        print("-----before------",request)
        # print(request.headers.get('User-Agent'))
        try:
            print(type(request.body))
            request_d = json.loads(request.body)
            print(request_d)
        except Exception as e:
            request_d = {}
            print("Exception ",e)
            pass
    
        response = get_response(request)


        if request.get_full_path() != "/Log/":
            print("-----after------",request)
            # print(request.headers.get('User-Agent'))
            # print("Middleware run after views")
            # print(request.get_full_path())
            # # print(request.build_absolute_uri())
            # print('type ',request.method)
            # print("user ", request.user.id)
            try:
                print("ype")
                # print(response.content)
                # print(json.loads(response))
                
                response_d = json.loads(response.content)
                # print("\n ====== \n")
                # print(response_d)
                Log.objects.create(request_username=str(request.user), request_method=request.method, request_url= request.get_full_path(), request_data= request_d, response_data= response_d ).save()

            except Exception as e:
                print("Exception ", e)
                pass
                
        return response

    return my_function