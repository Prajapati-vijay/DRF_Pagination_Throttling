class Testmiddleware:
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        print("Calling before view is called")
        print("######IP Address####")
        print(request.META.get("HTTP_USER_AGENT"))
        response=self.get_response(request)
        print("Calling after middleware is called")
        return self.process_repsonse(request, response)
    
    def process_repsonse(self, request, response):
        response["DEV_NAME"]="VIJAY_PRAJAPATI" 
        response["CURRENT_USER"]=request.user
        print("Name added in reponse")
        return response