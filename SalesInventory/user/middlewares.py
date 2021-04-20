
from user_log.models import Log
def my_middleware(get_response):
    print("in middleware is will run only one time")

    def my_function(request):
        print("Middleware run before views")
        print(get_response)
        print("-----before------",request)
        # print(request.headers.get('User-Agent'))
 
        response = get_response(request)
        if request.get_full_path() != "/Log/":
            print("-----after------",request)
            print(request.headers.get('User-Agent'))
            print("Middleware run after views")
            print(request.get_full_path())
            # print(request.build_absolute_uri())
            print('type ',request.method)
            print("user ", request.user.id)
            Log.objects.create(request_username=str(request.user), request_method=request.method, request_url= request.get_full_path()).save()

        return response

    return my_function